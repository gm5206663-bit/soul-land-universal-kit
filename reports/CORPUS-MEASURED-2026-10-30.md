# The corpus, measured — 2026-10-30

**What this is.** Every registered book re-measured from disk today, every declared edge checked
against what is actually written, and every defect the measurement surfaced named. No count in this
file was typed from memory: it comes from `tools/register.py` run over this repository at
`HEAD`, and from the chapters themselves.

**Why it exists.** The register is a generated file, and generated files rot the moment nobody
regenerates them. It had not been regenerated since **2026-10-13**. One book had moved and no page
on the account said so.

---

## The corpus today

**16 registered books · 283 chapters · 1,211,566 words.** The 2026-10-13 register said
**282 · 1,209,710** — the difference is one chapter, and it is the whole finding below.

| words | ch | book | over-60 | floor hits |
|---:|---:|---|---:|---:|
| 523,356 | 116 | `adaptive_prodigy` | 0 | 0 |
| 270,659 | 52 | `soul_land_4_fire_phoenix` | 0 | 0 |
| 80,127 | 24 | `Soul_Land_2_Project` | 0 | 0 |
| 65,081 | 24 | `soul_land_devouring_dragon` | 0 | **11** |
| 63,691 | 7 | `soul_land_3_oc` | 0 | 0 |
| **34,067** | **8** | **`lan_shen`** | 0 | 0 |
| 25,956 | 9 | `qian_xunji` | 0 | 0 |
| 25,792 | 10 | `soul_land_2_the_grey_wolf` | 0 | 0 |
| 25,379 | 4 | `Miraculous_Project` | 0 | 0 |
| 22,487 | 8 | `soul_land_2_new` | 0 | 0 |
| 19,360 | 6 | `soul_land_new` | 0 | 0 |
| 18,605 | 5 | `soul_land_1_fire_dragon_lizard` | 0 | 0 |
| 15,802 | 4 | `soul_land_system_cheat` | 0 | 0 |
| 13,696 | 4 | `soul_land_holy_spirit` | 0 | 0 |
| 3,802 | 1 | `soul_land_3_new` | 0 | 0 |
| 3,706 | 1 | `dragon_prince_yuan_native_oc_fanfiction` | 0 | 0 |

**Zero sentences over sixty words, corpus-wide.** That law has held across every book since the
2026-10-13 repair, and it still holds today.

---

## What moved, and what failed to notice

### `lan_shen` — a shipped chapter that reached no ledger but the one that mattered

Chapter 8, *Clean Hands*, shipped **2026-10-16**. Its own `SERIAL_LOG.md` recorded it properly as
REVISION 12, with the gates, the word count, and two honest flags. Everything above the serial —
`REGISTER.md`, `PROJECTS.md` — still said **7 chapters / 32,211 words**, because neither is
regenerated automatically and nobody ran the command.

| | said | measured |
|---|---|---|
| chapters | 7 | **8** |
| words | 32,211 | **34,067** |
| delta | — | +1 chapter, +1,856 words |

Both files corrected today. This is the failure mode the kit's own law names — *counts are measured,
never typed* — and the fix is mechanical: the register regenerates in one command, and
`tools/check.py` now stamps `REGISTER.md`'s generating tool into the kit's manifest so a stale
register is at least visible.

### A provenance receipt that does not verify

`PROJECTS.md` carried `lan_shen/` → *repo `lan_shen`, commit `cc8c180`*. Today:

```
$ git cat-file -t cc8c180
fatal: Not a valid object name cc8c180
$ gh api repos/gm5206663-bit/lan_shen      → 404 Not Found
```

The repository is gone and the commit exists nowhere in this history. The row is **not deleted** —
provenance history is history, and erasing it would hide the fact that a copy once existed — but it
now says plainly that it cannot be checked against anything.

---

## The defect that had no gate: the zero `?`/`!` law

`lan_shen`'s REVISION 12 closed with:

> *CH7 DEFECT FLAG: ch7 contains 11 question marks; the zero ?/! rule is not enforced by any gate.*

The second half was true and important. The first half was **aimed at the wrong chapter.**

Measured today, narration only (quoted spans stripped, which is what the law governs — every
PREWRITE board says *"zero ? and ! in prose"*, and a character may ask a question in dialogue):

| chapter | narration `?` | narration `!` | all `?` | all `!` |
|---|---:|---:|---:|---:|
| Ch01 | 0 | 0 | 1 | 0 |
| Ch02 | 0 | 0 | 1 | 0 |
| Ch03 | 0 | 0 | 0 | 0 |
| **Ch04** | **1** | 0 | 6 | 1 |
| **Ch05** | **5** | 0 | 29 | 5 |
| Ch06 | 0 | 0 | 11 | 1 |
| Ch07 — the flagged one | **0** | **0** | 13 | 12 |
| Ch08 | 0 | 0 | 0 | 0 |

**ch7's prose is clean; every one of its 13 `?` and 12 `!` sits inside quotation marks.** The real
violations are six, in ch4 (1) and ch5 (5).

**What was built.** `style_gate.py` check **5b** counts `?`/`!` in narration only, and the selftest
grew three cases so the detector cannot go blind: a narrating question, a narrating exclamation, and
a **quoted** question that must *not* misfire. Suite: **20/20** (was 17).

**Why it warns rather than fails.** Clearing the six means rewriting shipped prose. That is the
author's word, not a repair, so `QE_ENFORCE = "warn"` — one constant, flipped to `"fail"` the day
those six are cleared. Advisory is not blind: the selftest proves the detector speaks.

---

## The largest open quality defect on the account

`soul_land_devouring_dragon`: **11 of 24 chapters sit below the dialogue floor.** It is the only
book in the corpus carrying a floor-hit count at all. Its canon-voice rollout is measured at
**12 of 24** chapters rewritten (next: Ch 13), so the two figures describe the same work from
opposite ends — the rewrite is also the repair.

Nothing else in the corpus has a structural defect. Zero over-sixty sentences anywhere, zero
registered books unaccounted for, **33 of 33 chapter-bearing trees** classified (28 under a book,
5 archived or inbox).

---

## What only the author can decide, restated and current

| Where | The open call | State |
|---|---|---|
| `lan_shen` Ch8 | **3,192 words against a 3,800–5,000 band** — flagged, deliberately not padded | the light-unit case is written in REVISION 12; the author may accept it as-is |
| `lan_shen` | **mother's name: "Lang Yue" (shipped text, codex) vs "Lan Yue" (CONTINUITY row 6, canon-011 receipt)** | ch8 follows the shipped text; the conflict is unresolved |
| `lan_shen` ch4 + ch5 | **six narration `?`** under the zero law | mechanical to fix, but it is rewriting prose |
| `lan_shen` | **arc map re-cadence** (desk item A) — filed as issue #8 with the full measurement | awaiting |
| `soul_land_4_fire_phoenix` | **V2 public-promotion numbering** — staged C48–C55, `apply_authorization: NOT_GRANTED` (issue #9) | awaiting |
| `supergirl-adrian-vale` | **seven stale acceptances** — fix written and proved green (53/53) in `reports/supergirl-reaccept-2026-10-30/` | needs one session on that repo |

---

## How to keep this from rotting again

1. **Regenerate, don't retype.** `python3 SOUL_LAND_UNIVERSAL_KIT/tools/register.py --root . --out REGISTER.md` after any chapter ships.
2. **The kit's gate now stamps what it governs.** `tools/check.py --strict` covers the manifest; run it before saying the corpus is in order.
3. **A shipped chapter updates three things in the same commit:** its `SERIAL_LOG.md` row, `PROJECTS.md`'s count, and `REGISTER.md`'s regeneration. ch8 did the first and skipped the other two — which is exactly how a corpus of 1.2 million words ends up one chapter short of its own record.
