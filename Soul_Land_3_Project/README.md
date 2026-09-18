# SOUL LAND 3 — THE ADAPTIVE PRODIGY

A canon-verified *Legend of the Dragon King* (Soul Land 3) fan serial with an original character,
**Lin Hao (林浩)**, running beside canon's protagonist Tang Wulin — plus the thirteen-layer
verification suite that keeps it honest.

**116 chapters · 354,685 story words (suite-counted) · 13 automated check layers · exit 0.**

---

## THE PREMISE

Lin Hao awakens a **Stormbringer Sword** and an **Adaptation Talent** that optimises whatever it is
given. By chapter 71 he is a four-ring Soul Ancestor whose effective combat power runs **sixteen to
twenty-five ranks above his paper** — in a setting where canon's benchmark for that is a man wearing
two words of battle armor. He is eleven years old and he looks sixteen.

He is not the protagonist. Tang Wulin is. The story's engine is **what canon looks like when someone
is standing in it** — see `THE_CODEX.md` §THE BUTTERFLY LAW.

---

## RUNNING THE SUITE

```bash
cd Soul_Land_3_Project

# SL3_WORKSPACE points at the directory holding CODEX/ (the repo root, one level up)
SL3_WORKSPACE=.. sh checks/run_all.sh          # must exit 0
SL3_WORKSPACE=.. python3 checks/state.py --show
```

Thirteen layers: regenerate → rules → semantics → cross-chapter audit → ensemble → staleness →
consequences → canon quotes → power scale → monster law → butterfly → footer facts → **the voice** →
**the clock**.

🔴 **Layer 7 (canon quotes) runs in PARTIAL mode in this repo** — 79 canon chapters are on disk in
`canon_extract/chapters/` (run `SL3_CANON=canon_extract/chapters python3 checks/verify_canon_quotes.py`):
**21/80 quotes verified against them; the rest are loudly UNVERIFIED, never assumed** (the corpus lacks,
among others, canon 028's neighbors and everything after canon 308). Without `SL3_CANON` it SKIPS and says
*"This is NOT a pass."* See [`CANON_SOURCE.md`](CANON_SOURCE.md). The other twelve layers run for real.

Verified in both layouts before this was committed:

| Layout | Result |
|---|---|
| Authoring workspace, corpus present | **exit 0 · 85/85 canon quotes verified against 407 chapters** |
| This repo, 79 canon chapters on disk | **exit 0 · Layer 7 partial: 21/80 verified, remainder honestly UNVERIFIED** |

---

## WHAT IS HERE

| Path | What it is |
|---|---|
| `chapters/` | `chapter_01.md` … `chapter_71.md`. Each carries a canon-reference header, the prose, and a machine-readable footer. |
| `THE_CODEX.md` | The bible. The LAWS, the canon dossiers, a per-chapter record for all 71 chapters. |
| `CHARACTER_STATS.md` | Every canon character's numbers, each with its canon citation. |
| `POWER_MODEL.md` | Every number, its canon anchor, its curve. *If a number isn't here with a citation, it doesn't exist.* |
| `RELATIONSHIPS.md` | Every relationship, beat by beat, with its chapter. |
| `PROBLEM_INVENTORY.md` | Every defect with evidence and status. Nothing is dropped until verified fixed. |
| `CANON_COMPARISON_ch66-71.md` | 🔴 **Read this one.** A full audit of my chapters against canon, including four facts I got wrong and published. |
| `WORKSPACE_INDEX.md` | The authoring-workspace index (paths assume the original layout). |
| `checks/` | The thirteen-layer suite. `checks/paths.py` resolves every path; nothing else hardcodes one. |
| `../CODEX/` | The reusable thinking tools: consequence engine, decision journal, reasoning engines. |
| `../FANFICTION_FRAMEWORK.md` | The project-agnostic method extracted from this serial. |

---

## THE LAWS THIS SERIAL IS BUILT ON

These are locked in `THE_CODEX.md` and enforced by the suite. They exist because each one was broken.

- **THE MONSTER LAW** — at equal level he defeats everyone in seconds. The one exception in the
  franchise is Tang San. Genius is common in this setting; he is not a genius, he is a monster.
- **THE BUTTERFLY LAW** — canon's hierarchy does not survive him being in the room. Every line making
  another character *"highest / strongest / best"* in a group he belongs to must be scoped.
- **THE TWO AXES** — physical (never weaker than Wulin in anything) and overall combat (effective
  realm, derived from rank and ring count, never hardcoded).
- **THE VOICE LAW** — the prose must sound like chapters 1–3. Measured, not vibes: journal tics,
  record-keeping meta-voice, first-person bold narration, and comma-chain density.
- **THE TWO-COPIES LAW** — a fact maintained in two places will be wrong in one of them, and the check
  reads the other. One source, everything else derived.
- **THE FOURTH RING LAW** — the locked specification for the rank-40→45 arc, completed at ch71.

---

## HONEST STATE

Open problems are in `PROBLEM_INVENTORY.md` and are not hidden: **K9** (Hawk-Soul Union must be
re-thought now that the hawk shares him with something older), **K10** (the Shrek working-student arc
is only half-adapted), **K11** (our timeline runs ~2 years compressed against canon, recorded as
**D032**).

`CODEX/97_CLEANUP_LOG.md` and `CODEX/DECISION_JOURNAL.md` record what was broken, what was decided,
and what it cost — including the defects I introduced myself and the checks that caught them.
