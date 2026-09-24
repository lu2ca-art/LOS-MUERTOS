#!/usr/bin/env python3
"""Renders a single branded Story image (1080x1920): background photo + logo chip +
cat mascot watermark + text block, same visual language as the Reel. Static image,
not a full pipeline — no captions timing, no concat. Reuses the logo/cat treatment
from render_branded.py.

Usage: python3 render_story.py <background.jpg> <output.png> "LINE 1" "LINE 2 (optional)"
"""
import os
import shutil
import subprocess
import sys

FFMPEG = shutil.which("ffmpeg") or os.path.expanduser("~/bin/ffmpeg")
# relative to repo root — run this script from there
DATA_DIR = "squads/gestor-vila/pipeline/data"
FONT_DIR = f"{DATA_DIR}/fonts"
CAPTION_FONT = f"{FONT_DIR}/LasLocurasDelEmperador.ttf"
INTRO_FONT = f"{FONT_DIR}/Oswald-Variable.ttf"

ASSETS_DIR = f"{DATA_DIR}/brand-assets"
LOGO_PNG = f"{ASSETS_DIR}/logo-wordmark.png"
CAT_PNG = f"{ASSETS_DIR}/mascote-gato.png"

W, H = 1080, 1920
LOGO_CROP = dict(w=716, h=272, x=172, y=532)
CAT_CROP = dict(w=312, h=452, x=388, y=440)


def escape_drawtext(text):
    return (
        text.replace("\\", "\\\\")
        .replace(":", "\\:")
        .replace("'", "\\'")
        .replace(",", "\\,")
    )


def main():
    bg_path, out_path, *lines = sys.argv[1:]

    parts = [
        f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}[vbg]"
    ]

    logo_w = 480
    logo_h = round(logo_w * LOGO_CROP["h"] / LOGO_CROP["w"])
    logo_y = 60
    parts.append(
        f"[1:v]format=rgba,colorkey=0x0f0d0e:0.15:0.06,"
        f"crop={LOGO_CROP['w']}:{LOGO_CROP['h']}:{LOGO_CROP['x']}:{LOGO_CROP['y']},"
        f"scale={logo_w}:-1[logo]"
    )
    parts.append(f"[vbg][logo]overlay=x=(W-w)/2:y={logo_y}[vlogo]")

    cat_w = 150
    cat_h = round(cat_w * CAT_CROP["h"] / CAT_CROP["w"])
    cat_x = W - cat_w - 40
    cat_y = H - cat_h - 40
    parts.append(
        f"[2:v]format=rgba,"
        f"crop={CAT_CROP['w']}:{CAT_CROP['h']}:{CAT_CROP['x']}:{CAT_CROP['y']},"
        f"scale={cat_w}:-1[cat]"
    )
    parts.append(f"[vlogo][cat]overlay=x={cat_x}:y={cat_y}[vcat]")

    # Oswald, not the brand display font: story text here includes digits (address)
    # and "à", which Las Locuras del Emperador doesn't have glyphs for (same issue
    # hit on the price line in the intro) — safer to keep both story lines in Oswald.
    video_label = "vcat"
    text_y = logo_y + logo_h + 110
    for line in lines:
        out_label = f"vtxt{lines.index(line)}"
        text = escape_drawtext(line)
        parts.append(
            f"[{video_label}]drawtext=fontfile='{INTRO_FONT}':text='{text}':"
            f"fontcolor=0xF0F000:fontsize=54:borderw=3:bordercolor=black:"
            f"x=(w-text_w)/2:y={text_y}[{out_label}]"
        )
        video_label = out_label
        text_y += 90

    filter_complex = ";".join(parts)

    cmd = [
        FFMPEG, "-y",
        "-i", bg_path,
        "-i", LOGO_PNG,
        "-i", CAT_PNG,
        "-filter_complex", filter_complex,
        "-map", f"[{video_label}]",
        "-frames:v", "1", "-update", "1",
        out_path,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("ERROR:", result.stderr[-3000:], file=sys.stderr)
        sys.exit(1)
    print(f"OK: {out_path}")


if __name__ == "__main__":
    main()
