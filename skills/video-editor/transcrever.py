#!/usr/bin/env python3
"""
Transcreve um vídeo/áudio localmente (Whisper rodando no seu Mac, via
faster-whisper — sem API, sem custo) e salva um .md com timestamps por
trecho. Não sugere cortes sozinho — isso o LU2CA pede pro Claude fazer
depois, lendo a transcrição (é onde julgamento de conteúdo entra, não
uma heurística fixa no script).

Uso:
    python3 transcrever.py "/caminho/pro/video.mp4"
    python3 transcrever.py "/caminho/pro/video.mp4" -o saida.md
    python3 transcrever.py "/caminho/pro/video.mp4" --model small

Requer:
    - ffmpeg no PATH (extrai o áudio antes de transcrever)
    - pip install faster-whisper (já instalado no .venv desta pasta)

Primeira execução com cada tamanho de modelo baixa os pesos (uma vez só,
ficam em cache local). "base" é rápido e já serve bem pra PT-BR; "small"
é mais preciso e ainda roda tranquilo em CPU.
"""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path


def extrair_audio(video_path: Path, saida_path: Path) -> None:
    cmd = [
        "ffmpeg", "-y", "-i", str(video_path),
        "-vn", "-ac", "1", "-ar", "16000",
        str(saida_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("Erro ao extrair áudio com ffmpeg:", file=sys.stderr)
        print(result.stderr[-2000:], file=sys.stderr)
        sys.exit(1)


def formatar_tempo(segundos: float) -> str:
    m, s = divmod(int(segundos), 60)
    return f"{m:02d}:{s:02d}"


def transcrever(audio_path: Path, modelo: str):
    from faster_whisper import WhisperModel

    print(f"Carregando modelo '{modelo}' (primeira vez baixa os pesos)...")
    model = WhisperModel(modelo, device="cpu", compute_type="int8")
    segments, info = model.transcribe(str(audio_path), language="pt", vad_filter=False)
    return list(segments), info


def main():
    parser = argparse.ArgumentParser(description="Transcreve vídeo/áudio localmente com timestamps (Whisper local, sem API)")
    parser.add_argument("arquivo", help="Caminho do vídeo ou áudio")
    parser.add_argument("-o", "--output", help="Caminho do .md de saída (padrão: mesmo nome do arquivo + .md)")
    parser.add_argument("--model", default="small", choices=["tiny", "base", "small", "medium"], help="Tamanho do modelo (padrão: small — mais preciso, base alucina em trechos musicais)")
    args = parser.parse_args()

    video_path = Path(args.arquivo).expanduser()
    if not video_path.exists():
        print(f"Arquivo não encontrado: {video_path}", file=sys.stderr)
        sys.exit(1)

    output_path = Path(args.output).expanduser() if args.output else video_path.with_suffix(".md")

    print(f"Extraindo áudio de {video_path.name}...")
    with tempfile.TemporaryDirectory() as tmp:
        audio_path = Path(tmp) / "audio.wav"
        extrair_audio(video_path, audio_path)

        tamanho_mb = audio_path.stat().st_size / (1024 * 1024)
        print(f"Áudio extraído: {tamanho_mb:.1f} MB. Transcrevendo localmente (Whisper '{args.model}')...")

        segments, info = transcrever(audio_path, args.model)

    linhas = [
        f"# Transcrição — {video_path.name}",
        "",
        f"Duração: {formatar_tempo(info.duration)}",
        "",
    ]
    for seg in segments:
        inicio = formatar_tempo(seg.start)
        fim = formatar_tempo(seg.end)
        texto = seg.text.strip()
        linhas.append(f"**[{inicio} – {fim}]** {texto}")
        linhas.append("")

    output_path.write_text("\n".join(linhas), encoding="utf-8")
    print(f"\nPronto: {output_path}")
    print("Manda esse arquivo pro Claude pra sugerir os pontos de corte.")


if __name__ == "__main__":
    main()
