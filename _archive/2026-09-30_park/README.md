# PARK — 2026-09-30 · the workshop park

> **Why this exists:** the author closed the "Qing Ling" serial on 2026-09-30 and ordered the workshop cleaned before a new serial opened. This folder is where everything that was sitting at the top level went, so that only live, working serials remain in the open.
> **How it was made:** pure `git mv` — rename entries only, zero content changes, nothing deleted. Every folder keeps its own README/HANDOFF.
> **The `_archive/` law still applies:** nothing in here is current state — with **one intentional exception**, flagged below.

## Contents

| Path | What it is | Status |
|---|---|---|
| `soul_land_3_fanfiction/` | **"Qing Ling"** — the Soul Land 3 serial (Tang Wulin's canon line, ch 34–37 consumed; 7 chapters shipped / ~31.4k words across ch 1–7, every gate green). | **PARKED — RESUMABLE.** This is the exception to the archive law: see its `foundation/PARKED_2026-09-30.md` (shipped-state table, held threads, resume kit, and the push snag — ch 7's commit `2ea1ef6` is local-only until the remote is restored). Its `foundation/NEXT_STEPS.md` carries the drafted ch 8 plan with three author markers. |
| `Soul_Land_3_Project/` | **"The Adaptive Prodigy"** (OC Lin Hao) — the older SL3 branch (116 chapters / 354,685 words). | **DELETED from this repository 2026-10-03** at the author's word — tree and history purged. Not resumable from here; the serial reads on the Soul Library shelf. |
| `blue_silver/` | **Blue Silver** — pre-canon Blue Silver Grass serial; Book One complete (15 rebuilt chapters / 34,711 words, gates green). | PARKED at the Book Two threshold — awaits author rulings (`BOOK_TWO_OPTIONS.md`). |
| `_root_docs/` | Five root documents that had gone stale: `CLEANUP_2026-09-22_WORKSHOP.md`, `HOUSEKEEPING_2026-09-21.md`, `WORKSPACE_MAP_2026-09-22.md`, plus two outside-project pointers — `DRAGON_PRINCE_YUAN_FANFICTION_HANDOFF.md` (→ `/home/user/dragon_prince_yuan_native_oc_fanfiction/`) and `SOUL_LAND_4_FIRE_PHOENIX_NEXT_STEPS_FOR_CONTINUATION.md` (entry point to the private Fire Phoenix repo; its own §0 applies — STATUS_PANEL beats it on any conflict). | HISTORY / POINTERS. |

## Reachability

Everything here is in git forever — with one deliberate exception: `Soul_Land_3_Project/` was deleted (tree and history) on 2026-10-03 at the author's word. If a future sparse view un-materializes this folder, any remaining file is still one command away:

```
git show HEAD:_archive/2026-09-30_park/<path>
```
