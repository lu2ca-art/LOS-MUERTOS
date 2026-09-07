#!/usr/bin/env python3
"""
Gestor Vila — Control Server
Local-only HTTP server (127.0.0.1) that lets agent-status.html trigger real
commands on this machine instead of just showing copy-paste prompts.

Run it:
  python3 squads/gestor-vila/control-server.py

Then open:
  http://127.0.0.1:8787/agent-status.html

Everything here is triggered MANUALLY — one click, one run. There is no
scheduler, no cron, no auto-run. Runs are scoped per project (see
projects.json / STEP_DEFS below) so different projects — or independent
steps within the same project — can run at the same time; the same
project+step can't run twice concurrently. See the note at the bottom for
which agents run via a fast deterministic script (Vini) vs. a real Claude
Code subprocess (Hugo, Briefing, Cris, Vito, Renata, Rodrigo), and why
Paulo/Ana/Carmen are excluded.
"""

import http.server
import json
import os
import random
import re
import socketserver
import subprocess
import sys
import threading
import time
import unicodedata
import urllib.parse

SQUAD_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(os.path.dirname(SQUAD_DIR))
MEDIA_BASE = (
    "/Users/lu2ca/Library/Mobile Documents/com~apple~CloudDocs/"
    "LOS MUERTOS MIDIA/ mídia"
)
EDIT_SCRIPT = os.path.join(REPO_DIR, "skills", "video-editor", "scripts", "edit.py")
OUTPUT_DIR = os.path.join(SQUAD_DIR, "output")
LOG_PATH = os.path.join(OUTPUT_DIR, "execution-log.json")
STATS_PATH = os.path.join(OUTPUT_DIR, "execution-stats.json")
PROJECTS_PATH = os.path.join(OUTPUT_DIR, "projects.json")
PORT = 8787
CLAUDE_TIMEOUT_SEC = 480

# Runs are keyed by "<projectId>:<agentId>" (standalone agents — Hugo, Vini —
# use "_standalone:<agentId>" since they aren't part of a project checklist).
# Two DIFFERENT keys can run concurrently; the SAME key can't run twice at
# once. The dashboard polls /api/status (now a list) to reflect this.
FILE_LOCK = threading.Lock()  # guards execution-log.json / execution-stats.json / projects.json
RUN_LOCK = threading.Lock()  # guards RUNS
RUNS = {}  # run_key -> {entryId, agentId, agentName, mode, startedAt, estimatedSec, projectId, projectName}
DEFAULT_ESTIMATE_SEC = {"plan": 70, "execute": 150, "vini": 15}

# The 5 pipeline steps that are wired to real execution, in dependency order.
# Mirrors pipeline.yaml's step-01/02/03/07/08, simplified: step-07 (Renata)
# and step-08 (Rodrigo) really depend on Paulo/Ana's outputs per pipeline.yaml,
# but Paulo/Ana have no live button on purpose (they need explicit approval
# outside the dashboard — see bottom-of-file note). Gating on their output
# would leave Renata/Rodrigo permanently blocked in the dashboard, so here
# Renata is gated on Vito's visual instead (review content+visual before
# publish) and Rodrigo has no gate at all.
STEP_DEFS = [
    {"stepId": "step-01", "agentId": "briefing", "writes": "briefing.md",   "dependsOn": None},
    {"stepId": "step-02", "agentId": "cris",      "writes": "conteudo.md",   "dependsOn": "step-01"},
    {"stepId": "step-03", "agentId": "vito",      "writes": "visual-01.jpg", "dependsOn": "step-02"},
    {"stepId": "step-07", "agentId": "renata",    "writes": "review.md",     "dependsOn": "step-03"},
    {"stepId": "step-08", "agentId": "rodrigo",   "writes": "relatorio.md",  "dependsOn": None},
]
STEP_BY_AGENT = {s["agentId"]: s for s in STEP_DEFS}
STEP_BY_ID = {s["stepId"]: s for s in STEP_DEFS}

DAY_THEME_MAP = {
    "segunda": "almoço", "terca": "almoço", "quarta": "almoço",
    "quinta": "música", "sexta": " drinks", "sabado": " drinks",
    "domingo": "almoço",
}

# Agents wired to real execution via a `claude -p` subprocess. Only agents
# with no publish/spend side effect are here — see bottom-of-file note.
CLAUDE_AGENTS = {
    "briefing": {
        "name": "Briefing do Dia",
        "persona": None,
        "task": "pipeline/steps/step-01-briefing-do-dia.md",
    },
    "hugo": {
        "name": "Hugo Caçador",
        "persona": "agents/hugo-cacador.agent.md",
        "task": "agents/hugo-cacador/tasks/cacar-referencias.md",
    },
    "cris": {
        "name": "Cris Criativa",
        "persona": "agents/cris-criativa.agent.md",
        "task": "agents/cris-criativa/tasks/criar-conteudo-diario.md",
    },
    "vito": {
        "name": "Vito Visual",
        "persona": "agents/vito-visual.agent.md",
        "task": "agents/vito-visual/tasks/criar-visual-post.md",
    },
    "renata": {
        "name": "Renata Revisão",
        "persona": "agents/renata-revisao.agent.md",
        "task": "agents/renata-revisao/tasks/review.md",
    },
    "rodrigo": {
        "name": "Rodrigo Resultados",
        "persona": "agents/rodrigo-resultados.agent.md",
        "task": "agents/rodrigo-resultados/tasks/relatorio-marketing.md",
    },
}


def _norm(s):
    """Normalize for comparison: strip, lowercase, and collapse NFD/NFC
    accent forms — iCloud folder names can be decomposed (e.g. 'i' + combining
    acute) even when they look identical to a precomposed 'í' typed elsewhere."""
    return unicodedata.normalize("NFC", s.strip().lower())


def resolve_theme_dir(theme):
    wanted = _norm(theme)
    for name in os.listdir(MEDIA_BASE):
        if _norm(name) == wanted:
            return os.path.join(MEDIA_BASE, name)
    raise FileNotFoundError(f"Pasta de tema '{theme}' não encontrada em {MEDIA_BASE}")


def probe_duration(path):
    result = subprocess.run(["ffmpeg", "-i", path], capture_output=True, text=True)
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", result.stderr)
    if not m:
        return None
    h, mn, s = m.groups()
    return int(h) * 3600 + int(mn) * 60 + float(s)


def run_vini_edit(theme, caption, n_clips=2):
    theme_dir = resolve_theme_dir(theme)
    video_exts = (".mov", ".mp4")
    files = [f for f in os.listdir(theme_dir) if f.lower().endswith(video_exts)]
    if not files:
        raise FileNotFoundError(f"Nenhum vídeo encontrado em '{theme}'")

    chosen = random.sample(files, min(n_clips, len(files)))
    clips = []
    for f in chosen:
        path = os.path.join(theme_dir, f)
        dur = probe_duration(path)
        if not dur or dur < 1.0:
            continue
        start = min(0.3, max(0, dur - 3.0))
        end = min(dur - 0.1, start + 3.3)
        clips.append({"file": path, "start": f"{start:.1f}", "end": f"{end:.1f}"})

    if not clips:
        raise RuntimeError("Nenhum clipe utilizável (todos curtos demais ou ilegíveis)")

    run_id = time.strftime("%Y-%m-%d-%H%M%S")
    run_dir = os.path.join(OUTPUT_DIR, run_id)
    os.makedirs(run_dir, exist_ok=True)

    plan = {
        "clips": clips,
        "captions": [{"text": caption, "start": "0.5", "end": "6.5"}] if caption else [],
        "aspect_ratio": "9:16",
        "resolution": "1080x1920",
    }
    plan_path = os.path.join(run_dir, "edit-plan.json")
    with open(plan_path, "w") as f:
        json.dump(plan, f, ensure_ascii=False, indent=2)

    output_path = os.path.join(run_dir, "video-final.mp4")
    result = subprocess.run(
        [sys.executable, EDIT_SCRIPT, "--plan", plan_path, "--output", output_path],
        capture_output=True, text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr[-2000:] or "edit.py falhou sem mensagem de erro")

    rel_output = os.path.relpath(output_path, SQUAD_DIR)
    return {
        "agentId": "vini", "agentName": "Vini Vídeo", "ok": True,
        "summary": f"Editou reels do tema '{theme}' — clipes: {', '.join(os.path.basename(c['file']) for c in clips)}",
        "output_path": rel_output,
    }


def _base_prompt(cfg, squad_rel, extra_instructions, output_dir_rel):
    instructions_line = (
        f"Leia e siga a persona em {squad_rel}/{cfg['persona']} e a task em {squad_rel}/{cfg['task']}."
        if cfg.get("persona")
        else f"Siga exatamente as instruções em {squad_rel}/{cfg['task']}."
    )
    output_line = (
        f"Todos os arquivos de output deste projeto (briefing.md, conteudo.md, visual-01.jpg, etc.) "
        f"ficam em {squad_rel}/{output_dir_rel}/ — leia e escreva sempre nessa pasta."
    )
    return f"""Você é o agente {cfg['name']} do squad Opensquad "gestor-vila" (Vila Los Muertos de Fome).

{instructions_line}
Todos os caminhos de dados (pipeline/data/*.md) mencionados nesses arquivos são relativos a {squad_rel}/.
{output_line}

Se a task depender de um input anterior que ainda não existe (ex: {output_dir_rel}/briefing.md),
planeje gerar uma versão razoável desse input primeiro (baseada na data de hoje e no que
estiver disponível) — não pare por causa disso.

{"Instrução adicional do usuário: " + extra_instructions if extra_instructions else ""}"""


_CONTROL_FILES = {"execution-log.json", "execution-stats.json", "projects.json"}


def _snapshot_output_files(output_dir_rel):
    """mtime per file under output_dir_rel, used to diff before/after an
    execution so we can surface exactly which files it touched (not a guess
    parsed out of the agent's prose summary). Recurses (Hugo writes into a
    referencias/ subfolder) but stays out of OTHER projects' output dirs —
    relevant for 'principal', whose outputDir is the shared output/ root that
    every other project's subfolder also lives under — and skips Vini's
    date-stamped run folders, which aren't Claude-agent output."""
    abs_dir = os.path.join(SQUAD_DIR, output_dir_rel)
    if not os.path.isdir(abs_dir):
        return {}
    other_project_dirs = {
        os.path.normpath(os.path.join(SQUAD_DIR, p["outputDir"]))
        for p in ensure_projects_file()
        if p.get("outputDir") and p["outputDir"] != output_dir_rel
    }
    snap = {}
    for root, dirs, files in os.walk(abs_dir):
        dirs[:] = [
            d for d in dirs
            if os.path.normpath(os.path.join(root, d)) not in other_project_dirs
            and not re.match(r"^\d{4}-\d{2}-\d{2}", d)
        ]
        for f in files:
            if f in _CONTROL_FILES:
                continue
            full = os.path.join(root, f)
            try:
                snap[full] = os.path.getmtime(full)
            except OSError:
                pass
    return snap


def plan_claude_agent(agent_id, extra_instructions="", output_dir_rel="output"):
    """Step 1: read-only. No file writes — just a concrete plan for the user to approve."""
    cfg = CLAUDE_AGENTS.get(agent_id)
    if not cfg:
        raise ValueError(f"Agente '{agent_id}' não tem execução via Claude configurada")
    squad_rel = os.path.relpath(SQUAD_DIR, REPO_DIR)

    prompt = _base_prompt(cfg, squad_rel, extra_instructions, output_dir_rel) + f"""

NÃO escreva nem edite nenhum arquivo ainda. Apenas leia o que for necessário e monte um
plano concreto do que você faria: quais arquivos criaria/editaria (caminho exato) e um
resumo específico do conteúdo de cada um (não genérico — se for copy, escreva o rascunho
real; se for pesquisa, liste as referências reais já encontradas). Responda só com esse
plano em texto."""

    started = time.time()
    result = subprocess.run(
        ["claude", "-p", prompt, "--permission-mode", "plan"],
        cwd=REPO_DIR, capture_output=True, text=True, timeout=CLAUDE_TIMEOUT_SEC,
    )
    elapsed = round(time.time() - started, 1)
    if result.returncode != 0:
        raise RuntimeError((result.stderr or result.stdout or "claude -p falhou sem saída")[-2000:])

    return {
        "agentId": agent_id, "agentName": cfg["name"], "ok": True, "mode": "plan",
        "planText": result.stdout.strip()[-6000:], "extra": extra_instructions,
        "elapsedSec": elapsed,
    }


def execute_claude_agent(agent_id, extra_instructions, plan_text, output_dir_rel="output"):
    """Step 2: called only after the user clicks Approve on a stored plan."""
    cfg = CLAUDE_AGENTS.get(agent_id)
    if not cfg:
        raise ValueError(f"Agente '{agent_id}' não tem execução via Claude configurada")
    squad_rel = os.path.relpath(SQUAD_DIR, REPO_DIR)

    prompt = _base_prompt(cfg, squad_rel, extra_instructions, output_dir_rel) + f"""

O usuário já revisou e aprovou o plano abaixo. Execute-o agora de verdade — leia/escreva
os arquivos reais no disco, dentro de {squad_rel}/{output_dir_rel}/. Pode ajustar detalhes
menores se necessário, mas siga a intenção do plano aprovado.

PLANO APROVADO:
{plan_text}

No final, responda com um resumo curto (3-5 linhas) do que foi feito e o caminho exato de
cada arquivo criado ou modificado."""

    before = _snapshot_output_files(output_dir_rel)
    started = time.time()
    result = subprocess.run(
        ["claude", "-p", prompt, "--permission-mode", "acceptEdits"],
        cwd=REPO_DIR, capture_output=True, text=True, timeout=CLAUDE_TIMEOUT_SEC,
    )
    elapsed = round(time.time() - started, 1)
    if result.returncode != 0:
        raise RuntimeError((result.stderr or result.stdout or "claude -p falhou sem saída")[-2000:])

    after = _snapshot_output_files(output_dir_rel)
    output_paths = sorted(
        os.path.relpath(p, SQUAD_DIR)
        for p, mtime in after.items()
        if before.get(p) != mtime
    )

    return {
        "agentId": agent_id, "agentName": cfg["name"], "ok": True, "mode": "done",
        "summary": result.stdout.strip()[-4000:],
        "elapsedSec": elapsed,
        "outputPaths": output_paths,
    }


def _load_log():
    if not os.path.exists(LOG_PATH):
        return []
    try:
        with open(LOG_PATH, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def _save_log(log):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(LOG_PATH, "w") as f:
        json.dump(log[:100], f, ensure_ascii=False, indent=2)


def append_log(entry):
    with FILE_LOCK:
        log = _load_log()
        entry["id"] = f"{int(time.time()*1000)}-{random.randint(100,999)}"
        entry["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
        log.insert(0, entry)
        _save_log(log)
        return entry


def update_log(entry_id, patch):
    with FILE_LOCK:
        log = _load_log()
        for e in log:
            if e.get("id") == entry_id:
                e.update(patch)
                e["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
                _save_log(log)
                return e
        raise ValueError(f"Log entry '{entry_id}' não encontrado")


def read_log():
    return _load_log()


def _cleanup_stale_running():
    """Runs at startup — a 'running' entry can only survive if this process
    died mid-execution, so it can never actually finish. Mark it as an error
    instead of leaving a permanently-spinning card in the dashboard."""
    with FILE_LOCK:
        log = _load_log()
        changed = False
        for e in log:
            if e.get("mode") == "running":
                e["mode"] = "error"
                e["ok"] = False
                e["summary"] = "Execução interrompida (control-server reiniciado antes de terminar)."
                changed = True
        if changed:
            _save_log(log)


# ─── stats-based ETA (self-calibrating progress %) ───

def _load_stats():
    if not os.path.exists(STATS_PATH):
        return {}
    try:
        with open(STATS_PATH, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def _save_stats(stats):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(STATS_PATH, "w") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)


def estimate_duration(agent_id, mode):
    key = f"{agent_id}:{mode}"
    samples = _load_stats().get(key, [])
    if samples:
        return sum(samples) / len(samples)
    return DEFAULT_ESTIMATE_SEC.get(mode, 90)


def record_duration(agent_id, mode, elapsed):
    if not elapsed:
        return
    with FILE_LOCK:
        stats = _load_stats()
        key = f"{agent_id}:{mode}"
        samples = stats.get(key, [])
        samples.append(elapsed)
        stats[key] = samples[-5:]
        _save_stats(stats)


# ─── projects registry — each project is an isolated run of the pipeline
# checklist, with its own output/ subdirectory so parallel projects never
# collide on files ───

def _slugify(name):
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s or "projeto"


def _default_projects():
    return [
        {
            "id": "principal", "name": "Principal", "type": "pipeline",
            "createdAt": time.strftime("%Y-%m-%d"), "outputDir": "output",
        },
        {
            "id": "reels-almoco-semana", "name": "Reels de Almoço — Semana", "type": "adhoc",
            "createdAt": "2026-07-09",
            "note": "Vini Vídeo renderizou 7 reels (um por dia) — acione o Vini direto na aba Agentes.",
        },
    ]


def _load_projects_raw():
    if not os.path.exists(PROJECTS_PATH):
        return None
    try:
        with open(PROJECTS_PATH, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


def _save_projects(projects):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(PROJECTS_PATH, "w") as f:
        json.dump(projects, f, ensure_ascii=False, indent=2)


def ensure_projects_file():
    """The 'principal' project maps onto the existing flat output/ dir — no
    migration needed, today's briefing.md/conteudo.md just become its
    checklist state the first time this is called."""
    with FILE_LOCK:
        projects = _load_projects_raw()
        if projects is None:
            projects = _default_projects()
            _save_projects(projects)
        return projects


def find_project(project_id):
    for p in ensure_projects_file():
        if p["id"] == project_id:
            return p
    return None


def create_project(name):
    with FILE_LOCK:
        projects = _load_projects_raw() or _default_projects()
        base_slug = _slugify(name)
        slug = base_slug
        existing_ids = {p["id"] for p in projects}
        n = 2
        while slug in existing_ids:
            slug = f"{base_slug}-{n}"
            n += 1
        project = {
            "id": slug, "name": name, "type": "pipeline",
            "createdAt": time.strftime("%Y-%m-%d"), "outputDir": f"output/{slug}",
        }
        projects.append(project)
        _save_projects(projects)
        os.makedirs(os.path.join(SQUAD_DIR, project["outputDir"]), exist_ok=True)
        return project


def get_project_output_abs(project):
    return os.path.join(SQUAD_DIR, project["outputDir"])


def compute_checklist(project):
    """Status per STEP_DEFS step for this project: done (writes file exists),
    running (active RUNS entry), blocked (dependency not met), else ready."""
    out_dir = get_project_output_abs(project)
    with RUN_LOCK:
        active_keys = set(RUNS.keys())
    checklist = []
    for step in STEP_DEFS:
        run_key = f"{project['id']}:{step['agentId']}"
        done = os.path.exists(os.path.join(out_dir, step["writes"]))
        if run_key in active_keys:
            status = "running"
        elif done:
            status = "done"
        elif step["dependsOn"] is None:
            status = "ready"
        else:
            dep = STEP_BY_ID[step["dependsOn"]]
            status = "ready" if os.path.exists(os.path.join(out_dir, dep["writes"])) else "blocked"
        checklist.append({
            "stepId": step["stepId"], "agentId": step["agentId"],
            "agentName": CLAUDE_AGENTS[step["agentId"]]["name"],
            "status": status, "dependsOn": step["dependsOn"],
        })
    return checklist


# ─── run lock — keyed by "<projectId>:<agentId>" (or "_standalone:<agentId>"
# for Hugo/Vini). Same key can't run twice at once; different keys can run
# concurrently — that's how cross-project and independent-step parallelism
# happens. ───

def try_start_run(run_key, agent_id, agent_name, mode, project_id=None, project_name=None):
    with RUN_LOCK:
        if run_key in RUNS:
            return False
        RUNS[run_key] = {
            "entryId": None, "agentId": agent_id, "agentName": agent_name,
            "mode": mode, "startedAt": time.time(),
            "estimatedSec": estimate_duration(agent_id, mode),
            "projectId": project_id, "projectName": project_name,
        }
        return True


def set_run_entry_id(run_key, entry_id):
    with RUN_LOCK:
        if run_key in RUNS:
            RUNS[run_key]["entryId"] = entry_id


def finish_run(run_key):
    with RUN_LOCK:
        RUNS.pop(run_key, None)


def find_active_run(run_key):
    for r in run_status_snapshot()["runs"]:
        if r["runKey"] == run_key:
            return r
    return None


def run_status_snapshot():
    with RUN_LOCK:
        now = time.time()
        runs = []
        for key, r in RUNS.items():
            elapsed = round(now - r["startedAt"], 1)
            est = r["estimatedSec"] or 90
            pct = min(95, round(elapsed / est * 100))
            runs.append({
                "runKey": key, "entryId": r["entryId"], "agentId": r["agentId"],
                "agentName": r["agentName"], "mode": r["mode"],
                "elapsedSec": elapsed, "estimatedSec": est, "progressPct": pct,
                "projectId": r["projectId"], "projectName": r["projectName"],
            })
        return {"runs": runs}


def _plan_worker(run_key, entry_id, agent_id, extra, output_dir_rel):
    try:
        result = plan_claude_agent(agent_id, extra, output_dir_rel)
        record_duration(agent_id, "plan", result.get("elapsedSec"))
        update_log(entry_id, result)
    except Exception as e:
        update_log(entry_id, {"ok": False, "mode": "error", "summary": str(e)})
    finally:
        finish_run(run_key)


def _approve_worker(run_key, entry_id, agent_id, extra, plan_text, output_dir_rel):
    try:
        result = execute_claude_agent(agent_id, extra, plan_text, output_dir_rel)
        record_duration(agent_id, "execute", result.get("elapsedSec"))
        update_log(entry_id, result)
    except Exception as e:
        update_log(entry_id, {"ok": False, "mode": "error", "summary": str(e)})
    finally:
        finish_run(run_key)


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SQUAD_DIR, **kwargs)

    def log_message(self, fmt, *args):
        sys.stderr.write(f"[control-server] {self.address_string()} - {fmt % args}\n")

    def _send_json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/log":
            self._send_json(200, {"ok": True, "log": read_log()})
            return
        if parsed.path == "/api/status":
            self._send_json(200, run_status_snapshot())
            return
        if parsed.path == "/api/projects":
            projects = ensure_projects_file()
            result = []
            for p in projects:
                entry = dict(p)
                if p.get("type", "pipeline") == "pipeline":
                    entry["checklist"] = compute_checklist(p)
                result.append(entry)
            self._send_json(200, {"ok": True, "projects": result})
            return
        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length) if length else b"{}"
        try:
            body = json.loads(raw or b"{}")
        except json.JSONDecodeError:
            self._send_json(400, {"ok": False, "error": "JSON inválido no corpo do pedido"})
            return

        if parsed.path == "/api/projects":
            name = (body.get("name") or "").strip()
            if not name:
                self._send_json(400, {"ok": False, "error": "Nome do projeto é obrigatório"})
                return
            project = create_project(name)
            self._send_json(200, {"ok": True, "project": project})
            return

        if parsed.path == "/api/vini/edit":
            theme = body.get("theme") or DAY_THEME_MAP.get(body.get("day", ""), "almoço")
            caption = body.get("caption", "")
            run_key = "_standalone:vini"
            if not try_start_run(run_key, "vini", "Vini Vídeo", "vini"):
                current = find_active_run(run_key)
                self._send_json(409, {"ok": False, "error": "Vini já está rodando. Aguarde terminar.", "current": current})
                return
            try:
                result = run_vini_edit(theme, caption)
                self._send_json(200, append_log(result))
            except Exception as e:
                self._send_json(500, append_log({"agentId": "vini", "agentName": "Vini Vídeo", "ok": False, "summary": str(e)}))
            finally:
                finish_run(run_key)
            return

        if parsed.path == "/api/run-agent/plan":
            agent_id = body.get("agentId", "")
            extra = body.get("extra", "")
            project_id = body.get("projectId")
            cfg = CLAUDE_AGENTS.get(agent_id)
            if not cfg:
                self._send_json(400, {"ok": False, "error": f"Agente '{agent_id}' não tem execução via Claude configurada"})
                return

            step = STEP_BY_AGENT.get(agent_id)
            if step:
                if not project_id:
                    self._send_json(400, {"ok": False, "error": "Este agente faz parte do checklist de um projeto — informe projectId."})
                    return
                project = find_project(project_id)
                if not project:
                    self._send_json(404, {"ok": False, "error": f"Projeto '{project_id}' não encontrado"})
                    return
                status = next((c["status"] for c in compute_checklist(project) if c["agentId"] == agent_id), None)
                if status == "blocked":
                    dep = STEP_BY_ID[step["dependsOn"]]
                    dep_name = CLAUDE_AGENTS[dep["agentId"]]["name"]
                    self._send_json(409, {"ok": False, "error": f"Aguardando output de {dep_name} ({dep['writes']}) neste projeto."})
                    return
                run_key = f"{project_id}:{agent_id}"
                output_dir_rel = project["outputDir"]
                project_name = project["name"]
            else:
                run_key = f"_standalone:{agent_id}"
                output_dir_rel = "output"
                project_id = None
                project_name = None

            if not try_start_run(run_key, agent_id, cfg["name"], "plan", project_id, project_name):
                current = find_active_run(run_key)
                self._send_json(409, {"ok": False, "error": "Esta etapa já está rodando — aguarde terminar.", "current": current})
                return
            entry = append_log({
                "agentId": agent_id, "agentName": cfg["name"], "ok": True, "mode": "running",
                "step": "plan", "extra": extra, "projectId": project_id, "projectName": project_name,
                "outputDir": output_dir_rel,
            })
            set_run_entry_id(run_key, entry["id"])
            threading.Thread(target=_plan_worker, args=(run_key, entry["id"], agent_id, extra, output_dir_rel), daemon=True).start()
            self._send_json(200, entry)
            return

        if parsed.path == "/api/run-agent/approve":
            entry_id = body.get("id", "")
            log = read_log()
            entry = next((e for e in log if e.get("id") == entry_id), None)
            if not entry:
                self._send_json(404, {"ok": False, "error": f"Plano '{entry_id}' não encontrado no log"})
                return
            agent_id = entry["agentId"]
            project_id = entry.get("projectId")
            project_name = entry.get("projectName")
            output_dir_rel = entry.get("outputDir", "output")
            cfg = CLAUDE_AGENTS.get(agent_id, {})
            run_key = f"{project_id}:{agent_id}" if project_id else f"_standalone:{agent_id}"

            if not try_start_run(run_key, agent_id, cfg.get("name", agent_id), "execute", project_id, project_name):
                current = find_active_run(run_key)
                self._send_json(409, {"ok": False, "error": "Esta etapa já está rodando — aguarde terminar.", "current": current})
                return
            set_run_entry_id(run_key, entry_id)
            updated = update_log(entry_id, {"mode": "running", "step": "execute"})
            threading.Thread(
                target=_approve_worker,
                args=(run_key, entry_id, agent_id, entry.get("extra", ""), entry.get("planText", ""), output_dir_rel),
                daemon=True,
            ).start()
            self._send_json(200, updated)
            return

        self._send_json(404, {"ok": False, "error": f"Rota não encontrada: {parsed.path}"})


class ReusableThreadingTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True


def main():
    _cleanup_stale_running()
    with ReusableThreadingTCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Gestor Vila — Control Server rodando em http://127.0.0.1:{PORT}/")
        print(f"Servindo: {SQUAD_DIR}")
        print("Ctrl+C pra parar.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nParando...")


if __name__ == "__main__":
    main()

# ─────────────────────────────────────────────────────────────────────────
# Por que cada agente roda do jeito que roda — tudo manual, um clique = uma execução:
#
# Execuções são chaveadas por "<projectId>:<agentId>" em RUNS (protegido por
# RUN_LOCK). A MESMA chave não pode rodar duas vezes ao mesmo tempo (409), mas
# chaves DIFERENTES rodam concorrentemente de verdade — dois projetos ao
# mesmo tempo, ou duas etapas independentes do mesmo projeto (ex: Renata e
# Rodrigo, que não dependem uma da outra). Cada projeto tem seu próprio
# output/<projectId>/ (o projeto "principal" mapeia pro output/ raiz, sem
# migração), então dois `claude -p` concorrentes nunca escrevem no mesmo
# arquivo. plan/approve rodam em background thread (não bloqueiam a
# requisição HTTP): o POST devolve na hora um log entry com mode:"running", e
# o dashboard faz polling em GET /api/status (lista de todas as execuções
# ativas) / GET /api/log pra acompanhar progresso (% estimado a partir da
# duração média das últimas 5 execuções daquele agente+modo, guardada em
# execution-stats.json) até o worker (_plan_worker/_approve_worker) terminar
# e regravar o entry com o resultado final.
#
# O checklist de cada projeto (GET /api/projects) usa STEP_DEFS — só os 5
# steps já automatizados (briefing/cris/vito/renata/rodrigo), com uma
# dependência simplificada: Renata libera quando o Vito termina (não quando o
# Paulo publica, que não é automatizado) e Rodrigo não tem pré-requisito no
# painel. Ver STEP_DEFS pra detalhes.
#
# Vini Vídeo → /api/vini/edit: script determinístico (FFmpeg), sem custo de
# API, sem risco. Roda direto no processo do servidor (rápido), sob sua
# própria chave "_standalone:vini" — não compete com execuções de projeto.
#
# Briefing do Dia, Hugo, Cris, Vito, Renata, Rodrigo → dois passos, cada um um
# clique separado:
#   1. POST /api/run-agent/plan — `claude -p ... --permission-mode plan`. Só lê,
#      nunca escreve. Devolve um plano concreto (arquivos que criaria + conteúdo
#      real) que fica salvo no log como mode:"plan".
#   2. POST /api/run-agent/approve — só depois que o usuário aprova o plano na
#      aba de Outputs. Roda `claude -p ... --permission-mode acceptEdits` com o
#      plano aprovado embutido no prompt, agora sim escrevendo os arquivos.
# Isso existe porque a primeira versão rodava direto com acceptEdits no clique
# único — o classificador de segurança do Claude Code bloqueou isso (ver commit
# anterior), porque o usuário pediu "acionar manualmente", não "pular a
# aprovação de edição". O fluxo de dois passos resolve os dois ao mesmo tempo.
#
# Paulo Postador e Ana Anúncio NÃO estão aqui de propósito — o trabalho deles
# tem efeito real no mundo (publicar de verdade, gastar verba de anúncio).
# A regra própria desses agentes é "nunca sem aprovação explícita no momento",
# e um clique genérico num painel não substitui isso. Eles continuam via
# conversa, onde dá pra confirmar cada publicação/campanha antes de sair do ar.
#
# Carmen Atendimento não está aqui porque ainda não tem canal conectado
# (WhatsApp Business / Instagram Direct) — não há o que executar ainda.
# ─────────────────────────────────────────────────────────────────────────
