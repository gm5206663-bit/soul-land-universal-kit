# HANDOFF — Soul Land 3 New Serial

**Live edge: FOUNDATION STAGE — no chapters. Next blocking action: the author answers
Rulings R1–R4 in `foundation/OPEN_RULINGS.md`.**

Created 2026-09-22 by agent session (Arena), from the author's instruction:
"new fan fiction of Soul Land 3 — everything that is useful, everything completely."

## Must read before ANY continuation (in order)

1. `README.md` (project map + single-fact table)
2. `foundation/OPEN_RULINGS.md` — R1–R6; prose is FORBIDDEN while R1–R4 are OPEN
3. `foundation/RAILS.md` — the standing law
4. `foundation/STATUS_PANEL.md` — T0 state
5. `seeds/PREMISE_CANDIDATES.md` — the six protagonist candidates for R1
6. `foundation/CANON_SPINE_SL3.md` + `foundation/POWER_LAW_SL3.md` — before any drafting

## What NOT to do

- Do **not** invent a protagonist before the author rules R1. Foundation is staged so
  every candidate leaves locks dormant, not decided.
- Do **not** pull state, figures, or characters from `Soul_Land_3_Project/` (Lin Hao),
  `_archive/`, `reference/sl3_lin_hao/`, or any Fire Phoenix panel. Their numbers are
  their own; ours live in this tree only.
- Do **not** treat `foundation/CANON_SPINE_SL3.md` rows tagged `[verify]` as settled —
  check the primary text before a chapter turns on them (kit canon-access method).
- Do **not** write a world bible beyond what is here (kit 02: "25,000 words of world
  bible before chapter one exists is procrastination with a file extension"). The codex
  grows from chapters, not before them.
- Never delete work. Archive with a README marker, never erase.

## Gates

```bash
python3 checks/verify.py --selftest   # prove the gate still catches defects
python3 checks/verify.py              # gate the real serial (chapters/ + STATUS_PANEL)
```

The gate currently checks: sequence, length budget, sentence grammar cap, dialogue
density, banned tokens (incl. the Fire Phoenix stale-edge incident tokens), zero-CJK,
chapter footer sync, STATUS_PANEL chapter tracking, canon-spine anchor presence, and
the no-prose-before-R1/R2 ruling lock.

## Next session checklist

- [ ] Author answers R1 (protagonist) — pick from `seeds/PREMISE_CANDIDATES.md` or overrule
- [ ] Author answers R2 (relation to Lin Hao branch — default: separate universe)
- [ ] Author answers R3 (canon entry point) and R4 (divergence policy)
- [ ] Fill the twelve locks in `foundation/NO_MISTAKE_LIVE_RULES.md` from the rulings
- [ ] Canon re-verification pass on all `[verify]` rows the chosen premise turns on
- [ ] Draft `chapters/Chapter_01_*.md`, then `python3 checks/verify.py`
