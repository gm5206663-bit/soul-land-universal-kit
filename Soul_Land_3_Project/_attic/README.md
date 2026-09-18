# _attic — session scratch, retained not deleted

Moved here during the 2026-09-03 cleanup (user: "I think you should do clean up"). Nothing in this
folder is read by the live pipeline (`run_all.sh` globes only `chapters/`, named root docs,
`checks/state.json`, and `CANON_ACCESS.md`/`DIVERGENCE_LEDGER.md`/`BUTTERFLY_EFFECTS.md`). Keep
history out of the working surface; restore from here if a future session ever needs it.

## session_scratch/
- `fix_nn.py`, `fix_nn2.py`, `fix_oo.py`, `fix_oo2.py` — one-shot repair scripts for the
  BG-era relationship-row audits (duplicates / omissions). Each ran once; the fixes now live in
  `RELATIONSHIPS.md`. Do not rerun.
- `audit_mm.py` — one-shot miss-mode audit script for the same era.
- `_fix_sword_mode.py` — root-level scratch script (Stormbringer/Stormbringer-mode wording sweep).
- `REBUILD_MANIFEST.md` — the rr-session tracker for rebuilding chapters 1–79 (COMPLETE; all 102
  chapters are rebuilt and green).
- `CARRY_AUDIT_2026_09_03.md`, `DIVERGENCE_AUDIT_2026_09_03.md`, `FULL_AUDIT_2026_09_02.md` —
  point-in-time audit reports; their live findings are in `PROBLEM_INVENTORY.md` (BG/BH logs) and
  the live docs. Snapshot value only.

## archive_consolidated/ (cleanup 2026-09-03)
- `AUDIT_2026_08_30.md` + `README_archive.md` — moved from the old top-level `archive/`
  folder, which duplicated this attic and was removed. The 30-Aug full audit is a point-in-time
  snapshot; its live successors are the suite (`checks/run_all.sh`) and the prewrite board.

## session_scratch/ additions (cleanup 2026-09-03)
- `_bf_extract.json.bak` — the butterfly-fact *extraction* artifact (67 chapters of partial
  sentence fragments). NO code reads or writes it; it was a one-time preprocessing step.
  Its content is regenerated from the chapters by `checks/build_butterfly_effects.py`.
