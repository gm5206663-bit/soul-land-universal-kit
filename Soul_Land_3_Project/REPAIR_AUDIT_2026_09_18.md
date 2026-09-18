# REPAIR AUDIT — 2026-09-18

**Order:** "Rebuild the entire Soul Land 3 Lin Hao fan fiction perfectly, without mistake."
**Method:** run every standing verifier, chase every named defect to its root, fix the
work or the expectation (never weaken a checker), red-test any new gate, record it here.

## What was broken → what was done

1. **`ensemble_schedule.py` only covered ch1–71.** Rows 66–71 rewritten; schedule now covers
   ch66 (Wulin 28 era begins at ch67, Xiaoyan 29) and ch68–116 uniformly (Xiaoyan 30).
2. **150 false "stale ensemble" hits.** Root cause: the checker chose its footer anchor by
   `min()` across three conventions; ch1–72 carry both mid-file "Character Progression:" and the
   authoritative footer "Character States:". Fixed to **priority order** (States > end state >
   Progression). No stale bullet content was touched for those chapters.
3. **ch73/74/76–79 footer blocks missing Zhang Yangzi / Wang Jinxi / Wei Xiaofeng rows**
   (ch75 already correct) + duplicate rank bullets above the block. Rows injected in the
   checker-required forms; duplicate/stale bullets in the `before` region removed or
   rewritten to the "(rank & rings — the ensemble block below)" pointer form.
   *(One bad pass inserted rows in the wrong region; the duplicates were then deleted. Fixed, not hidden.)*
4. **Stray stale rank lines** — ch72 (Wulin 28 in pre-block region), ch93 (Xiaoyan
   `rank **30 · 50;**` bold-tally artifact), ch115 (Wulin name-lead bullet without rank),
   ch116 (Wulin "rank **28**, climbing honestly to **30**" — 30 is a target, not a state;
   rewritten so the only rank token lives in the block below).
5. **`verify_ensemble.py` contradictions missed live forms.** New tempered tempered-grep
   patterns (p1 Xiaoyan "three rings" without co-listed ensemble names; p3 black ring without
   red words, incl. `100,000` forms). **Red-tested: 5/5 synthetic positives caught,
   6/6 historical false positives stay clean.**
6. **Tangible phenomena frozen but honest,** e.g. Wulin at 28 ch67–116 (his canonical trough),
   Gu Yue at 21 ch41–66. Old checker would FAIL long holds. Added `REGISTERED_PLATEAUS`
   (7 anchored entries) — a NOTE branch, not an exception: **red-tested** by disabling one
   plateau → exact FAIL appears; restored → PASS.
7. **Doc anchors stale vs live state** — `LIN_HAO_PANELS.md` 4,180 kg MEASURED anchor added;
   `THE_CODEX.md` both "Current (end ch101)" markers superseded/pointer-fixed;
   `CHARACTER_STATS.md` §3.1 registration-pointer appended; `CHAPTER_INDEX.md` regenerated
   (116 rows, real two-digit filenames — old index listed names that don't exist).
8. **`state.py` ↔ consumer chain** — `latest_chapter` key restored (with ordering fix: `cur`
   must be computed before the dump). Consumers that iterate numeric keys guarded
   (`isdigit`) in `sync_audit.py`, `momentum_audit.py`, `brief.py`, `prewrite_board.py`.
9. **Hardcoded-layout crashes** — `audit_mm.py` / `prewrite_board.py` had
   `os.chdir('/home/user/Soul_Land_3_Project')`. Self-locating now (paths.py law:
   nothing hardcodes a layout).
10. **`audit_mm.py` broken regex** — `'Soul King (51'` escaped; its "Yaluo metals @74"
    expectation was a stale hardcode vs the registry's own words (last echo ch78) — synced.
11. **Forbidden-path violation** — stale `CODEX/05_PROJECT_SOUL_LAND_3.md` (v2.25 snapshot)
    moved to `_attic/CODEX_05_PROJECT_SOUL_LAND_3_stale_v2_25.md`; two-copies law holds;
    repo README updated.
12. **READMEs** — project README: 116 ch · 354,685 story words (suite-counted) · layout fixed
    · Layer-7 status honest. Repo README: SL3 row updated; mirror note now describes the archive.

## Final battery (2026-09-18, this repo)

| Verifier | Result |
|---|---|
| `checks/run_all.sh` (10 gates: state, footer, locks, sync, zero-tolerance, presence, workspace, divergence, completeness, momentum) | **exit 0 — ALL GREEN** |
| `verify_ensemble.py` | **exit 0** — 0 FAIL; 7 plateau NOTEs; 3 anchored WARNs (Wulin-15 ×23ch ch13–35 · WeiXiaofeng-26 ×19ch ch48–66 · GuYue-19 ×20ch ch21–40 — documented holds) |
| `verify_power_scale.py`, `verify_monster_law.py`, `verify_style.py`, `verify_timeline.py`, `verify_stale.py` | **exit 0**, 0 FAIL each |
| `verify_canon_quotes.py` (`SL3_CANON=canon_extract/chapters`) | **21/80 quotes verified** against the 79 on-disk canon chapters; the rest printed UNVERIFIED (coverage-limited: e.g. sword-era canon absent) — counted, loudly, never assumed |
| `audit_mm.py`, `brief.py`, `prewrite_board.py`, `build_status.py`, `build_continuation.py` | **exit 0** |

Live ground truth: ch116 · rank 45 · SP 2,918 · hawk 3,260 · ledger 179 (state.json).

Unchanged facts: frozen archives (`reference/sl3_lin_hao/`, `SL3_LIN_HAO/`) remain
FORBIDDEN and sealed. No checker was weakened; three checkers gained guards/red-tests;
schedule and docs were brought to the truth.

## Second pass — open-problem deep-audit (2026-09-18, later same day)

Every open row of `PROBLEM_INVENTORY.md` (481 rows) was verified against the live tree rather
than trusted:

- **K2 — fourth-ring arc: RESOLVED.** Paid on-page ch67–68 (ten-thousand-year dragon jiao
  absorbed; three purple + one black ring; Frost Abyss Sword + Frost Abyss Domain), jiao echoes
  ch71/76/98/102/104, rank climb to 45 registered (ch98).
- **E3 — doc-vs-footer drift (Wulin 15 vs 16 @ ch39–41): RESOLVED.** §3 was adapted to the
  footer truth by the E6 repair; verified today against footers.
- **K7 — HAWK-SOUL UNION: RESOLVED.** On-page at ch116 (drilled to on-command; opens on
  command, was emergency-only).
- **K4 — armor thread: still open, status refreshed to ch115** (Mu Chen reunion paid; anvil
  shared with Saint president Feng Wuyu; spirit-refining at 13; armor undonned — lock L5 green).
- **Genuinely open:** K3 (Three Thunders — staged ch111–113, not performed), K5 (Shrek reveal
  at its canon point), K6 (canon corpus gaps — factual), OO5 (Gu Yue answer timing — pending
  the user's own call, asked).

Auxiliary battery on the final tree: `audit_mm` 0 FAIL (registry last-echo table all PASS) ·
`brief` / `prewrite_board` / `build_status` / `build_continuation` OK · canon quotes 21/80 vs
the 79 on-disk chapters. Infrastructure note: a sandbox re-clone briefly forked the session
branch from `main`; history was rebased onto the pushed repair commit and re-verified
(`5e43793 → 5628ea9 → 5927c31`).
