# WORKSHOP CLEANUP — 2026-09-22 (author order)

Author order: "First clean up the mess..." then: "you don't do clean up in workshop."
Rule applied (same as HOUSEKEEPING_2026-09-21 precedent): remove only what is
byte-identical elsewhere or strictly superseded; every file with unique content kept.

## CUTS
| What | Files | Why safe |
|---|---|---|
| `reference/sl3_lin_hao/Soul_Land_3_Project` | 300 | Stale mirror of live `Soul_Land_3_Project/` — 0 unique files (verified `diff -rq`) |
| `arena_managed_uploads/` | 652 | Superseded SL4 snapshot; same content in `SL_ARCHIVE/`; SL4 project lives in its own repo (`soul_land_4_fire_phoenix`) |
| `SL_ARCHIVE/sl4_foundation_v1` | ~90 | Strict subset of `sl4_foundation_v2` (0 unique) |
| `soul_land_starter.zip` | 1 | Extracted dir `soul_land_starter/` sits beside it |
| `uploads/` (whole dir) | 24 of 28 | 24 files byte-duplicated by `SL_ARCHIVE/inbox/` + `SOUL_LAND_UNIVERSAL_KIT/`; 4 kept moved to `SL_ARCHIVE/inbox/` (SARA.md, chapter_75.md, handoff_package.txt) / deleted as twin (`README (1).md` = `SL1_GU_YUAN/ARCHIVE_README.md`) |
| Root `SARA.md` | 1 | Byte-twin of `SOUL_LAND_WORKSPACE/SARA.md` |
| 4 old WORKSPACE_MAP_* (09-18, 09-19 ×2, 09-19 index) | 4 | Moved to `SL_ARCHIVE/workspace_maps_history/` (kept, root decluttered); current = 2026-09-22 |
| push_to_github.sh + split_repos.sh | 2 | Moved to `.admin/` (kept, root decluttered) |

## KEPT (everything else — all serials, libraries, codices, archives with living readers)
Soul_Land_2/3/5_Project, Miraculous_Project, soul_land_devouring_dragon, soul_land_holy_spirit,
soul_land_new, soul_land_3_new (LIVE SERIAL), blue_silver, CODEX, SL_ARCHIVE, _archive, etc.

## RESULT
Tracked files: 2,438 -> ~1,400. Root: 25 dirs -> cleaner; one current workspace map.
