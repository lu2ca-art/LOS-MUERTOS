---
name: video-editor
description: >
  Assembles short-form vertical/square videos (Reels, Stories, TikTok) from raw clips
  using FFmpeg — cuts clips to timestamps, overlays captions, mixes background music,
  and exports in the right aspect ratio. 100% free and local, no API key, no subscription.
description_pt-BR: >
  Monta vídeos curtos verticais/quadrados (Reels, Stories, TikTok) a partir de clipes brutos
  usando FFmpeg — corta clipes por timestamp, sobrepõe legendas, mixa trilha sonora,
  e exporta na proporção certa. 100% grátis e local, sem API key, sem assinatura.
type: script
version: "1.0.0"
script:
  path: scripts/edit.py
  runtime: python3
  invoke: "python3 {skill_path}/scripts/edit.py --plan \"{plan}\" --output \"{output}\""
env: []
categories: [video, editing, automation, social-media]
---

# Video Editor (FFmpeg)

## When to use

Use this skill when an agent needs to assemble a finished short-form video (Reels, TikTok,
Stories) from raw footage the user already has — bastidor de cozinha, show ao vivo, clientes
na casa, etc. It does NOT generate footage; it edits footage that already exists as files.

**Why FFmpeg instead of CapCut:** CapCut has no public API — nothing can open or drive a CapCut
project automatically. FFmpeg is free, open-source, and fully scriptable, so an agent can
assemble the final video end-to-end without any manual step in a GUI editor.

## Requirements

- `ffmpeg` must be installed and on PATH. Check with `ffmpeg -version`.
- **Installed on this machine already** via `pip3 install --user imageio-ffmpeg` (a Python
  package that bundles a static ffmpeg binary) — no Homebrew, no sudo, no password prompt.
  The binary was symlinked into `~/bin/ffmpeg` (already on PATH). To reproduce on another
  machine:
  ```bash
  pip3 install --user imageio-ffmpeg
  ln -sf "$(python3 -c 'import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())')" ~/bin/ffmpeg
  ```
- If Homebrew is available and preferred instead: `brew install ffmpeg`.
- Either way this is a one-time, free, local install — no account, no API key, no recurring cost.
- Note: this bundled binary does not include `ffprobe` — `scripts/edit.py` gets video duration
  by parsing `ffmpeg -i`'s own stderr output instead of shelling out to `ffprobe`.

## Instructions

### 1. Build an edit plan (JSON)

```json
{
  "clips": [
    {"file": "raw/chef-alex-1.mp4", "start": "00:00:02", "end": "00:00:07"},
    {"file": "raw/chef-alex-2.mp4", "start": "00:00:00", "end": "00:00:05"}
  ],
  "captions": [
    {"text": "bastidor com o chef alex", "start": "00:00:00", "end": "00:00:03"},
    {"text": "quinta a sábado, 20h", "start": "00:00:05", "end": "00:00:09"}
  ],
  "music": {"file": "assets/trilha.mp3", "volume": 0.25},
  "aspect_ratio": "9:16",
  "resolution": "1080x1920"
}
```

- `clips`: trimmed and concatenated in order. `start`/`end` in `HH:MM:SS` (or seconds).
- `captions`: optional. Burned in as centered white text with black outline, near the bottom third.
- `music`: optional. Mixed under the original clip audio at the given volume (0.0–1.0).
- `aspect_ratio`: `9:16` (Reels/Stories/TikTok), `1:1` (feed), or `16:9` (YouTube). Clips are
  scaled and center-cropped to fit — always confirm which format the destination platform needs.
- `resolution`: output pixel size. Defaults to `1080x1920` if omitted.

### 2. Run the script

```bash
python3 skills/video-editor/scripts/edit.py \
  --plan "squads/{squad}/output/{run_id}/edit-plan.json" \
  --output "squads/{squad}/output/{run_id}/video-final.mp4"
```

### 3. Report the result

The script prints the final duration and file size. Confirm the output file exists before
telling the user it's ready — never claim success without verifying the output file.

## Phone footage rotation (handled automatically, but know why)

Real iPhone/Android clips embed a display-matrix rotation (e.g. "-90 degrees") instead of
storing pixels pre-rotated. Two ffmpeg quirks around this are already handled in
`scripts/edit.py` — worth knowing if you extend the script:

1. **ffmpeg's implicit autorotate is unreliable inside `-filter_complex`.** Empirically, it
   correctly auto-rotates when a clip's `trim` starts after 0, but silently fails to rotate
   when `trim` starts at exactly `0` — same file, same metadata, no error, just sideways
   output. The script disables autorotate entirely (`-noautorotate`) and applies the correct
   `transpose` filter explicitly based on the detected rotation, so behavior no longer depends
   on the trim start value.
2. **The original rotation metadata leaks into the output container even after the pixels are
   correctly rotated by a filter.** ffmpeg's own side-data propagation copies the *input's*
   display matrix (e.g. "-90 degrees") onto the *output* stream regardless of what the filter
   graph did — so a player that respects that metadata (Instagram, TikTok, QuickTime) would
   rotate the already-correct video again and show it sideways. The script forces
   `-display_rotation 0` on every input to stop that propagation, verified by checking the
   rendered output has no `displaymatrix` side data (`ffmpeg -i output.mp4` should show no
   `rotation of ... degrees` line).

Both were caught and fixed by testing against real Vila footage, not just synthetic clips —
synthetic `testsrc`/`smptebars` clips carry no rotation metadata, so this class of bug is
invisible until real phone footage is used.

## Anti-patterns

- Never invent footage — this skill only assembles clips that already exist on disk. If the
  footage doesn't exist yet, say so; don't fabricate a plan around files that aren't there.
- Never skip the aspect ratio check — a 16:9 video posted as a Reel gets cropped wrong.
- Keep captions short (≤ 6 words per line) — burned-in text on 9:16 mobile screens gets
  unreadable fast if it's long.

## Error handling

- If `ffmpeg` is not found on PATH, the script exits with instructions to install it.
- If a clip file listed in the plan doesn't exist, the script exits before rendering anything
  and reports which file is missing.
- If rendering fails partway, the script deletes the partial output file so it's never mistaken
  for a finished video.
