#!/usr/bin/env node
// Lê pipeline/data/biblioteca-respostas-atual.md e gera data/biblioteca.json
// pra uso em runtime pelo webhook (api/webhook.js). Rodar de novo sempre que
// a biblioteca for editada: `node scripts/parse-biblioteca.js`

const fs = require("fs");
const path = require("path");

const SRC = path.join(__dirname, "..", "..", "pipeline", "data", "biblioteca-respostas-atual.md");
const OUT = path.join(__dirname, "..", "data", "biblioteca.json");

const raw = fs.readFileSync(SRC, "utf8");

// Corta tudo a partir de "## Pendências" (não são categorias de resposta)
const semPendencias = raw.split(/\n##\s+Pendências/)[0];

// Cada categoria começa com "## " ou "### " ou "## X." institucional
const blocks = semPendencias.split(/\n(?=##\s)/).slice(1);

function extract(re, block) {
  const m = block.match(re);
  return m ? m[1].trim() : "";
}

function stripMd(s) {
  return s.replace(/\*\*/g, "").replace(/\*/g, "").trim();
}

const categorias = blocks.map((block, i) => {
  const titleLine = block.split("\n")[0].replace(/^##\s*/, "").trim();
  const isInstitucional = /^[B-E]\./.test(titleLine);
  const titulo = titleLine.replace(/^[B-E]\.\s*/, "");

  const perguntaRaw = extract(/\*\*(?:Pergunta típica|Situação típica):\*\*\s*(.+)/, block);
  // "vocês têm reserva?" / "como reservo?" / ... -> lista de frases
  const perguntas = perguntaRaw
    .split(/"\s*\/\s*"/)
    .map((s) => s.replace(/^"|"$/g, "").trim())
    .filter(Boolean);

  const usaDirecionamento = /\*\*Direcionamento:\*\*/.test(block);
  const respostaRaw = extract(/\*\*(?:Resposta|Direcionamento):\*\*\s*(.+?)(?=\n\*\*|\n\*[^*]|\n---|\n\n\*|\n$)/s, block);
  const respostaLimpa = stripMd(respostaRaw).replace(/\s+/g, " ").trim();

  // "Direcionamento" mistura instrução interna (ex: "Nunca fechar valor...",
  // "escalar pro Lucas") com a frase real que vai pro cliente, sempre entre
  // aspas. Extrai só a frase entre aspas pra nunca vazar instrução interna
  // — incluindo nome de pessoa — numa resposta automática de verdade.
  let resposta = respostaLimpa;
  let notaInterna = null;
  if (usaDirecionamento) {
    const quoted = respostaRaw.match(/"([^"]+)"/);
    if (quoted) {
      resposta = stripMd(quoted[1]).replace(/\s+/g, " ").trim();
      notaInterna = respostaLimpa;
    } else {
      notaInterna = respostaLimpa;
    }
  }

  const isReclamacao = /^Reclamação$/i.test(titulo);
  const isForaEscopo = /Fora do Escopo/i.test(titulo);

  // Categorias com placeholder ([...]) dependem de dado que muda (agenda da
  // semana, etc.) — não dá pra mandar o texto cru pro cliente.
  const requiresManualData = /\[/.test(resposta);
  if (requiresManualData) {
    notaInterna = notaInterna || respostaLimpa;
    resposta = "boa pergunta! deixa eu confirmar isso certinho com o time e já te falo por aqui.";
  }

  return {
    id: titulo
      .toLowerCase()
      .normalize("NFD")
      .replace(/[̀-ͯ]/g, "")
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/(^-|-$)/g, ""),
    titulo,
    perguntas,
    resposta,
    notaInterna,
    isInstitucional,
    isReclamacao,
    isForaEscopo,
    requiresManualData,
  };
}).filter((c) => c.titulo && c.resposta);

fs.mkdirSync(path.dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, JSON.stringify(categorias, null, 2), "utf8");

console.log(`OK: ${categorias.length} categorias exportadas para ${path.relative(process.cwd(), OUT)}`);
const semPergunta = categorias.filter((c) => !c.perguntas.length && !c.isInstitucional);
if (semPergunta.length) {
  console.log("Aviso — categorias sem 'pergunta típica' extraída (vão só pelo texto do título no matching):");
  semPergunta.forEach((c) => console.log("  -", c.titulo));
}
