#!/usr/bin/env python3
"""Branded render for reel-produto-22-09, v4 — logo (keyed off its near-black backing)
+ cat mascot with genuine alpha transparency this time (client re-exported it properly,
no more colorkey hack needed for the mascot) + captions in Las Locuras del Emperador,
now in brand yellow. No white card — stays on the dark footage per vila-identity.md's
own "fundo sempre escuro" rule. Reuses the clip trim/concat/rotation logic from edit.py.
"""
import json
import os
import re
import shutil
import subprocess
import sys

# resolve ffmpeg from PATH first — falls back to the imageio-ffmpeg symlink location
# used on machines where it's not on PATH (see skills/video-editor/SKILL.md)
FFMPEG = shutil.which("ffmpeg") or os.path.expanduser("~/bin/ffmpeg")
# relative to repo root — run this script from there (e.g. `python3 squads/gestor-vila/scripts/render_branded.py`)
DATA_DIR = "squads/gestor-vila/pipeline/data"
FONT_DIR = f"{DATA_DIR}/fonts"
CAPTION_FONT = f"{FONT_DIR}/LasLocurasDelEmperador.ttf"
# the brand display font has no digits, no "$" and no "ç" glyphs — fine for short dish
# names, but would silently drop the price. Intro promo (has "R$160") uses Oswald instead.
INTRO_FONT = f"{FONT_DIR}/Oswald-Variable.ttf"

ASSETS_DIR = f"{DATA_DIR}/brand-assets"
LOGO_PNG = f"{ASSETS_DIR}/logo-wordmark.png"  # "LOS MUERTOS DE FOME" wordmark, black bg
CAT_PNG = f"{ASSETS_DIR}/mascote-gato.png"    # cat mascot ("Gato do Vila" — food/kitchen per brand kit), real alpha

PLAN_PATH = "squads/gestor-vila/output/reel-produto-22-09/edit-plan.json"
OUTPUT_PATH = "squads/gestor-vila/output/reel-produto-22-09/video-final.mp4"

W, H = 1080, 1920

# content bounding boxes inside each PNG, found via ffmpeg cropdetect (avoids
# scaling a mostly-empty canvas down to a tiny logo)
LOGO_CROP = dict(w=716, h=272, x=172, y=532)
CAT_CROP = dict(w=312, h=452, x=388, y=440)


def to_seconds(value):
    value = str(value)
    if ":" not in value:
        return float(value)
    parts = [float(p) for p in value.split(":")]
    seconds = 0.0
    for part in parts:
        seconds = seconds * 60 + part
    return seconds


def detect_rotation(path):
    result = subprocess.run([FFMPEG, "-i", path], capture_output=True, text=True)
    match = re.search(r"rotation of (-?\d+(?:\.\d+)?) degrees", result.stderr)
    if not match:
        return 0
    return round(float(match.group(1))) % 360


def rotation_filter(degrees):
    if degrees in (90, -270):
        return "transpose=2,"
    if degrees in (-90, 270):
        return "transpose=1,"
    if degrees in (180, -180):
        return "transpose=1,transpose=1,"
    return ""


def escape_drawtext(text):
    return (
        text.replace("\\", "\\\\")
        .replace(":", "\\:")
        .replace("'", "\\'")
        .replace(",", "\\,")
    )


def main():
    with open(PLAN_PATH) as f:
        plan = json.load(f)
    clips = plan["clips"]
    captions = plan["captions"]

    parts = []
    for i, clip in enumerate(clips):
        start = to_seconds(clip["start"])
        end = to_seconds(clip["end"])
        rotate = rotation_filter(detect_rotation(clip["file"]))
        parts.append(
            f"[{i}:v]trim=start={start}:end={end},setpts=PTS-STARTPTS,{rotate}"
            f"scale={W}:{H}:force_original_aspect_ratio=increase,"
            f"crop={W}:{H}[v{i}]"
        )
        parts.append(f"[{i}:a]atrim=start={start}:end={end},asetpts=PTS-STARTPTS[a{i}]")

    concat_inputs = "".join(f"[v{i}][a{i}]" for i in range(len(clips)))
    parts.append(f"{concat_inputs}concat=n={len(clips)}:v=1:a=1[vraw][araw]")

    logo_idx = len(clips)
    cat_idx = len(clips) + 1

    # logo: key out its near-black backing (0x0f0d0e sampled from a corner), crop to
    # the actual wordmark content, scale, place top-center
    logo_w = 480
    logo_h = round(logo_w * LOGO_CROP["h"] / LOGO_CROP["w"])
    logo_y = 60
    parts.append(
        f"[{logo_idx}:v]format=rgba,colorkey=0x0f0d0e:0.15:0.06,"
        f"crop={LOGO_CROP['w']}:{LOGO_CROP['h']}:{LOGO_CROP['x']}:{LOGO_CROP['y']},"
        f"scale={logo_w}:-1[logo]"
    )
    parts.append(f"[vraw][logo]overlay=x=(W-w)/2:y={logo_y}[vlogo]")

    # cat mascot ("Gato do Vila" = comida/bastidores de cozinha, per vila-identity.md) —
    # small persistent watermark, bottom-right corner. Real alpha this time, no keying.
    cat_w = 150
    cat_h = round(cat_w * CAT_CROP["h"] / CAT_CROP["w"])
    cat_x = W - cat_w - 40
    cat_y = H - cat_h - 40
    parts.append(
        f"[{cat_idx}:v]format=rgba,"
        f"crop={CAT_CROP['w']}:{CAT_CROP['h']}:{CAT_CROP['x']}:{CAT_CROP['y']},"
        f"scale={cat_w}:-1[cat]"
    )
    parts.append(f"[vlogo][cat]overlay=x={cat_x}:y={cat_y}[vcatbadge]")

    video_label = "vcatbadge"
    text_y = logo_y + logo_h + 110
    for j, cap in enumerate(captions):
        out_label = f"vcap{j}"
        text = escape_drawtext(cap["text"])
        cap_start = to_seconds(cap["start"])
        cap_end = to_seconds(cap["end"])
        parts.append(
            f"[{video_label}]drawtext=fontfile='{CAPTION_FONT}':text='{text}':"
            f"fontcolor=0xF0F000:fontsize=58:borderw=3:bordercolor=black:"
            f"x=(w-text_w)/2:y={text_y}:"
            f"enable='between(t,{cap_start},{cap_end})'[{out_label}]"
        )
        video_label = out_label

    intro = plan.get("intro")
    if intro:
        intro_start = to_seconds(intro["start"])
        intro_end = to_seconds(intro["end"])
        line1 = escape_drawtext(intro["line1"])
        line2 = escape_drawtext(intro["line2"])
        parts.append(
            f"[{video_label}]drawtext=fontfile='{INTRO_FONT}':text='{line1}':"
            f"fontcolor=white:fontsize=64:borderw=4:bordercolor=black:"
            f"x=(w-text_w)/2:y=780:"
            f"enable='between(t,{intro_start},{intro_end})'[vintro1]"
        )
        parts.append(
            f"[vintro1]drawtext=fontfile='{INTRO_FONT}':text='{line2}':"
            f"fontcolor=0xDC2828:fontsize=100:borderw=5:bordercolor=black:"
            f"x=(w-text_w)/2:y=900:"
            f"enable='between(t,{intro_start},{intro_end})'[vintro2]"
        )
        video_label = "vintro2"

    filter_complex = ";".join(parts)

    cmd = [FFMPEG, "-y"]
    for clip in clips:
        cmd += ["-noautorotate", "-display_rotation", "0", "-i", clip["file"]]
    cmd += ["-i", LOGO_PNG, "-i", CAT_PNG]

    cmd += [
        "-filter_complex", filter_complex,
        "-map", f"[{video_label}]",
        "-map", "[araw]",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-movflags", "+faststart",
        OUTPUT_PATH,
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        if os.path.exists(OUTPUT_PATH):
            os.remove(OUTPUT_PATH)
        print("ERROR:", result.stderr[-3000:], file=sys.stderr)
        sys.exit(1)

    size_mb = os.path.getsize(OUTPUT_PATH) / (1024 * 1024)
    print(f"OK: {OUTPUT_PATH} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
