# Audit — Chapter Validation, 2026-10-03

Receipt for the post-write validation pass (fire-phoenix audit pattern).

## Checks run

| Check | Result |
|---|---|
| `tools/chapter_gate.py chapters/Chapter_01.md` | **PASS** — 2430 words at the then-band; band corrected same day to 3600–5000 (see RULINGS_LOG R13 correction; chapter expanded to the corrected band) |
| `tools/chapter_gate.py chapters/Chapter_02.md` | **PASS** — 2931 words at the then-band; band corrected same day to 3600–5000; chapter expanded to the corrected band |
| `tools/chapter_gate.py --selftest` | **14/14 passed** |
| `foundation_gate.py` (control-centre) | **PASS** — stage 0 unlocked, 2 chapters, 0 errors/warnings |
| Regression grep (`storyos/BANNED_TOKENS.json`) | clean on active chapters after rebuild (rejected title removed from active use) |

## Notes

- Paragraph advisory recalibrated warn-only to the author's own style
  (his Chapter 1 = 272 blocks; receipt recorded in the gate).
- Chapter 1 v1 ("The Lizard and the Grass") rejected by the author and
  superseded; v2 superseded by the birth-foundation rebuild. History
  lives in git + `SERIAL_LOG.md`; active files carry only the current
  versions.
- Both chapters: coverage files written before prose (6-part receipt
  format, `canon_coverage/`).

Signed: arena-agent, same day as the rebuild.


## Current state after the same-day expansions and full sweep

| Command | Result |
|---|---|
| `chapter_gate Chapter_01` | **PASS — 4975** (band 3600–5000), 0 warnings |
| `chapter_gate Chapter_02` | **PASS — 3713**, 0 warnings |
| `chapter_gate Chapter_03` | **PASS — 3677**, 0 warnings |
| `chapter_gate Chapter_04` | **PASS — 3713**, 0 warnings |
| `chapter_gate --selftest` | 14/14 |
| `foundation_gate` (control-centre) | PASS — 4 chapters on disk |

The 2430/2931 rows above are historical (pre-correction) and kept for
the record.
