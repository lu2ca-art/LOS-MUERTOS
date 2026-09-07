#!/usr/bin/env python3
"""
Video Editor — Opensquad Skill (FFmpeg-based, free/local)
Assembles short-form vertical/square videos from raw clips: trims, concatenates,
burns in captions, mixes background music, and exports at the target aspect ratio.

Usage:
  python3 edit.py --plan "edit-plan.json" --output "video-final.mp4"
"""

import argparse
import json
import re
import os
import shutil
import subprocess
import sys

ASPECT_DEFAULTS = {
    "9:16": "1080x1920",
    "1:1": "1080x1080",
    "16:9": "1920x1080",
}

FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
]


def check_ffmpeg():
    if not shutil.which("ffmpeg"):
        print(
            "ERROR: ffmpeg not found on PATH.\n"
            "Install it once (free, local, no account needed):\n"
            "  1. Install Homebrew: https://brew.sh\n"
            "  2. Run: brew install ffmpeg\n",
            file=sys.stderr,
        )
        sys.exit(1)


def find_font():
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            return path
    return None


def detect_rotation(path):
    """Read the display-matrix rotation iPhone/Android clips embed as metadata.

    We always render with -noautorotate (see render()) and apply this correction
    explicitly, because ffmpeg's implicit autorotate-in-filtergraph behavior is
    unreliable: empirically, it silently fails to rotate when a clip's trim starts
    at exactly 0 (works fine for start > 0), producing sideways video with no error.
    Disabling it and always rotating explicitly removes that inconsistency.
    """
    result = subprocess.run(["ffmpeg", "-i", path], capture_output=True, text=True)
    match = re.search(r"rotation of (-?\d+(?:\.\d+)?) degrees", result.stderr)
    if not match:
        return 0
    return round(float(match.group(1))) % 360


def rotation_filter(degrees):
    """Map a display-matrix rotation to the transpose filter(s) that correct it.

    Verified empirically against real footage with -noautorotate: -90 needs
    transpose=1, and by symmetry 90 needs the opposite (transpose=2), 180 needs two.
    """
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


def load_plan(plan_path):
    with open(plan_path, "r") as f:
        plan = json.load(f)
    if not plan.get("clips"):
        print("ERROR: edit plan has no clips", file=sys.stderr)
        sys.exit(1)
    for clip in plan["clips"]:
        if not os.path.exists(clip["file"]):
            print(f"ERROR: clip not found: {clip['file']}", file=sys.stderr)
            sys.exit(1)
    music = plan.get("music")
    if music and not os.path.exists(music["file"]):
        print(f"ERROR: music file not found: {music['file']}", file=sys.stderr)
        sys.exit(1)
    return plan


def to_seconds(value):
    """Convert 'HH:MM:SS(.ms)' or a plain number to seconds (float).

    Filter options like trim=start=...:end=... and eval expressions like
    between(t,start,end) both use ':' or ',' as argument separators, so a raw
    'HH:MM:SS' string breaks the filtergraph parser — it must be numeric seconds.
    """
    value = str(value)
    if ":" not in value:
        return float(value)
    parts = [float(p) for p in value.split(":")]
    seconds = 0.0
    for part in parts:
        seconds = seconds * 60 + part
    return seconds


def resolve_resolution(plan):
    if plan.get("resolution"):
        w, h = plan["resolution"].lower().split("x")
        return int(w), int(h)
    aspect = plan.get("aspect_ratio", "9:16")
    default = ASPECT_DEFAULTS.get(aspect, "1080x1920")
    w, h = default.split("x")
    return int(w), int(h)


def build_filter_complex(plan, width, height, has_music):
    clips = plan["clips"]
    captions = plan.get("captions", [])
    font = find_font()
    parts = []

    for i, clip in enumerate(clips):
        start = to_seconds(clip["start"])
        end = to_seconds(clip["end"])
        rotate = rotation_filter(detect_rotation(clip["file"]))
        parts.append(
            f"[{i}:v]trim=start={start}:end={end},setpts=PTS-STARTPTS,{rotate}"
            f"scale={width}:{height}:force_original_aspect_ratio=increase,"
            f"crop={width}:{height}[v{i}]"
        )
        parts.append(
            f"[{i}:a]atrim=start={start}:end={end},asetpts=PTS-STARTPTS[a{i}]"
        )

    concat_inputs = "".join(f"[v{i}][a{i}]" for i in range(len(clips)))
    parts.append(f"{concat_inputs}concat=n={len(clips)}:v=1:a=1[vraw][araw]")

    video_label = "vraw"
    for j, cap in enumerate(captions):
        out_label = f"vcap{j}"
        text = escape_drawtext(cap["text"])
        font_opt = f"fontfile='{font}':" if font else ""
        cap_start = to_seconds(cap["start"])
        cap_end = to_seconds(cap["end"])
        parts.append(
            f"[{video_label}]drawtext={font_opt}text='{text}':fontcolor=white:fontsize=54:"
            f"borderw=3:bordercolor=black:x=(w-text_w)/2:y=h-h/3.5:"
            f"enable='between(t,{cap_start},{cap_end})'[{out_label}]"
        )
        video_label = out_label

    final_video = f"[{video_label}]"

    if has_music:
        music_volume = plan["music"].get("volume", 0.25)
        music_idx = len(clips)
        parts.append(f"[{music_idx}:a]volume={music_volume}[amusic]")
        parts.append("[araw][amusic]amix=inputs=2:duration=first:dropout_transition=0[afinal]")
        final_audio = "[afinal]"
    else:
        final_audio = "[araw]"

    return ";".join(parts), final_video, final_audio


def render(plan, output_path):
    width, height = resolve_resolution(plan)
    clips = plan["clips"]
    music = plan.get("music")

    filter_complex, video_map, audio_map = build_filter_complex(
        plan, width, height, has_music=bool(music)
    )

    # -noautorotate: disable ffmpeg's implicit autorotate-in-filtergraph behavior,
    # which is unreliable (see detect_rotation docstring) — we rotate explicitly instead.
    # -display_rotation 0: without this, ffmpeg carries the *original* rotation
    # metadata (e.g. "-90 degrees") into the output container even though the pixels
    # are already correctly rotated by our filter — a player that respects display
    # matrix metadata (Instagram, TikTok, QuickTime) would then rotate it AGAIN and
    # show the final video sideways. Forcing 0 at the input stops that propagation.
    cmd = ["ffmpeg", "-y"]
    for clip in clips:
        cmd += ["-noautorotate", "-display_rotation", "0", "-i", clip["file"]]
    if music:
        cmd += ["-i", music["file"]]

    cmd += [
        "-filter_complex", filter_complex,
        "-map", video_map,
        "-map", audio_map,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-movflags", "+faststart",
        output_path,
    ]

    os.makedirs(os.path.dirname(os.path.abspath(output_path)) or ".", exist_ok=True)
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        if os.path.exists(output_path):
            os.remove(output_path)
        print("ERROR: ffmpeg render failed:", file=sys.stderr)
        print(result.stderr[-3000:], file=sys.stderr)
        sys.exit(1)

    return output_path


def probe_duration(path):
    # Avoid depending on ffprobe (not bundled by every ffmpeg distribution) —
    # ffmpeg itself prints "Duration: HH:MM:SS.xx" to stderr when probing a file.
    result = subprocess.run(
        ["ffmpeg", "-i", path], capture_output=True, text=True
    )
    match = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", result.stderr)
    if not match:
        return "unknown"
    h, m, s = match.groups()
    return f"{int(h) * 3600 + int(m) * 60 + float(s):.1f}"


def report(output_path):
    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    duration = probe_duration(output_path)
    print(f"OK: {output_path} ({size_mb:.1f} MB, {duration}s)")


def main():
    parser = argparse.ArgumentParser(description="Assemble short-form video via FFmpeg")
    parser.add_argument("--plan", required=True, help="Path to edit plan JSON")
    parser.add_argument("--output", required=True, help="Output video file path")
    args = parser.parse_args()

    check_ffmpeg()
    plan = load_plan(args.plan)
    output_path = render(plan, args.output)
    report(output_path)


if __name__ == "__main__":
    main()
