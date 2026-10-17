# Fire Phoenix — illustrated media, production v1

**Unofficial, non-commercial Soul Land fan adaptation · fanfiction by Gaurav Meena.**

This is a working visual production package, not a completed animated series.
It preserves the delicate, exceptionally beautiful feminine face beneath Yan
Shuo’er’s public boy identity. The user accepted that portrait as a working
direction; new scenes, costumes and companion faces are not permanently approved.

## Open first

- **[Public gallery](https://gm5206663-bit.github.io/soul-land-universal-kit/fire-phoenix-media/)** — scene art, searchable chapter plates and videos.
- **[Trailer MP4](video/fire-phoenix-trailer.mp4)** — 1:11 English-narrated illustrated motion preview.
- **[Chapter 01–52 MP4](video/fire-phoenix-chapters-01-52.mp4)** — 9:45 narrated chapter overview.
- **[Complete ZIP download](https://github.com/gm5206663-bit/soul-land-universal-kit/releases/download/fire-phoenix-media-v1/fire-phoenix-media-v1.zip)** — extract before viewing offline.
- **[Chapter production board](CHAPTER-BOARD.md)** — 52 source-pinned entries and shot plans.
- `index.html` — self-contained gallery in the standalone delivery ZIP. In the repository this points to the single deployed gallery under `docs/fire-phoenix-media/`.

Arena’s file viewer has no network access. Gallery images are embedded and work
there; videos should be opened as separate deliverables. To use the complete
package offline, extract the ZIP and open `index.html` in a browser; keep its
folder structure intact. No CDN, external fonts or third-party scripts are needed.

## What is finished in this package

| Deliverable | Coverage |
|---|---|
| Working reference portrait | 1 accepted working direction, not an immutable model sheet |
| New scene illustrations | 8 unique scenes, separate from the reference portrait |
| Designed chapter plates | 52, one for each published chapter |
| Chapter board | 52 summaries, source hashes, progression guards and shot plans |
| English narration | 10 MP3s: trailer plus nine chapter groups |
| Motion videos | 2 MP4s, 1280 × 720, 24 fps, slow camera movement and fades |
| Accessibility | Searchable gallery, image descriptions, narration scripts, estimated WebVTT captions |
| Production tools | Source metadata builder, layout/video renderer, gallery/bundle builder, validator |

**10 chapter entries share the 8 illustrated keyframes. The other 42 chapters
have designed storyboard plates and shot plans, not dedicated scene illustrations.**
The videos have no character acting, lip sync or custom battle animation.
Chapter transitions and captions are estimated, not forced-aligned.

## Source and boundaries

Pinned source: `gm5206663-bit/soul-land-universal-kit` at
`856bc3bebe306827504c4f183ab786d225c1c3e0`,
`soul_land_4_fire_phoenix/chapters/Chapter_01.md` through `Chapter_52.md`.
Each file’s exact SHA-256 and permanent source URL are in
[`metadata/chapters.json`](metadata/chapters.json).

- This package does not write Chapter 53 or alter any existing chapter.
- Early art does not borrow earned wings, purple rings or later transformations.
- Post-awakening hair stays copper-red; the boy disguise does not masculinize the face.
- Dorm 333 remains first at 20,341; Dorm 336 remains second at 9,846.
- Chapter 52 stops with the wounded beasts alive and the herb rooted.
- No public identity reveal, fourth ring, divinity or future forest outcome is authorized.

## Folder guide

- `assets/` — working portrait and eight reviewed AI-generated keyframes.
- `cards/` — 52 chapter plates plus four video title/end plates.
- `audio/` — ten synthesized narration tracks and their exact scripts.
- `video/` — two narrated MP4s and estimated English WebVTT sidecars.
- `metadata/` — chapter sources, render timings, validation and SHA-256 manifest.
- `tools/` — builders and checks; no credentials or studio reference frames.
- `POSTER.jpg` — branded fan-project poster.
- `CREDITS.md`, `QA.md` — provenance, rights note and honest limitations.

## Rebuild from the committed assets

Python 3.10+; install `pip install -r requirements.txt`. The renderer uses
`imageio-ffmpeg`’s binary and DejaVu fonts from `/usr/share/fonts/truetype/dejavu/`.
On other systems, change the font constants in `tools/render.py`.

```sh
# Optional: prepare from an exact checkout of the pinned source revision.
# Do not point this at a moving HEAD without reviewing intervening source changes.
python tools/prepare.py --source /path/to/pinned/soul-land-universal-kit
python tools/render.py --temp /tmp/fire-phoenix-render
python tools/captions.py
python tools/validate.py --source /path/to/soul-land-universal-kit
python tools/bundle.py --zip ../fire-phoenix-media-v1.zip
# Verify the final hash manifest as a separate final step.
python tools/validate.py --source /path/to/soul-land-universal-kit --check-manifest --no-write
```

Optional browser QA: install `playwright`, run `playwright install --with-deps chromium`, start a local HTTP server, then run `python tools/browsercheck.py`. Public media integrity CI validates against the pinned source checkout, not a moving story edge.

The tools reproduce layouts and video assembly from the saved assets. They do
**not** reproduce the AI-generated art or voice bit-for-bit. The selected voice
is the previously auditioned English narrator, session ID `voice-00`.

See [credits](CREDITS.md) before reuse. No commercial rights to the underlying
franchise are asserted. This package is not a franchise-wide open-content license.
