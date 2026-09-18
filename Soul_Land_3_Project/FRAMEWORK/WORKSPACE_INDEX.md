# WORKSPACE INDEX
### Last updated **2026-08-30**, at the end of **Chapter 71**.

> 🔴 **This file is checked.** `checks/verify_stale.py` scans it for a live-state marker that is behind
> the story and **fails** if it finds one. So do `CODEX/00_MASTER_INDEX.md` and
> `FANFICTION_FRAMEWORK.md`. **Update it every chapter** — see `FANFICTION_FRAMEWORK.md §8`.

---

## ACTIVE PROJECT

**`Soul_Land_3_Project/`** — *"Soul Land 3: The Adaptive Prodigy."* OC **Lin Hao (林浩)** beside canon MC
Tang Wulin. **71 chapters, 230,424 prose words.** Every chapter canon-backed and machine-verified.

### 🔴 CURRENT STATE — end of Chapter 71

| | |
|---|---|
| **Rank** | 🔴 **45** — **Soul Ancestor** · **THE FOURTH-RING ARC IS COMPLETE** (rank 40 → 45 in one event) |
| **Effective combat power** | 🔴 **Soul Emperor (61–70)** — **16–25 ranks above his paper** (canon's benchmark for a battle armor master is +20; he is there with nothing on) |
| **Rings** | 🔴 **FOUR — three purple rings and one BLACK** (ten-thousand-year ⇒ black, canon c260) |
| **Spiritual power** | 🔴 **517 — SPIRIT SEA** (the wall at 500 is crossed) |
| **Gale Hawk** | **1,520 years** · wind + lightning · 🔴 now shares him with something older |
| **Ledger** | **125 lines** · the gap is closed with one line |
| **Smithing / sword** | 🔨 4th rank **Grandmaster** · ⚔️ 🔴 **FROST ABYSS SWORD (TOP-LEVEL)** + 🔴 **FROST ABYSS DOMAIN** (martial-soul innate, unnamed, contested) |
| **Age** | **11** — 🔴 **and he looks sixteen.** Wulin did not recognise him in a doorway. His clothes do not fit. He is quieter. |
| **Position** | **at Shrek Academy** · 🔴 **OUT of the pool** · blacksmith council seat · 🔴 **Yue Zhengyu has spent a month calling Gu Yue an evil soul master** |

> The authoritative live copy is **`Soul_Land_3_Project/LIN_HAO_STATUS.md`**, which is **GENERATED**
> from `checks/state.json`, which is derived from the chapter footers. This table is a convenience.

### Files

| File | What it is |
|---|---|
| `THE_CODEX.md` | The bible. Story facts, **the LAWS**, canon dossiers, per-chapter records. 🔴 **Exactly one copy — the mirror was deleted 2026-08-29.** |
| `CHARACTER_STATS.md` | Every canon character's numbers, each with its canon citation. **Single source of truth for the ensemble.** |
| `POWER_MODEL.md` | Every number, its canon anchor, and its curve. **If a number isn't here with a citation, it doesn't exist.** |
| `RELATIONSHIPS.md` | Every relationship, beat by beat, with its chapter. §10 is the Lin Hao ↔ Gu Yue record. |
| `LIN_HAO_STATUS.md` | **GENERATED** — the protagonist's current figures + the canon benchmark table. |
| `LIN_HAO_PANELS.md` | The Adaptation Talent field panels, current. |
| `CONTINUATION_PROMPT.md` | **GENERATED** — what to read first, what is owed, what is locked. |
| `PROBLEM_INVENTORY.md` | Every defect with evidence and status. **Nothing is dropped until verified fixed.** |
| `CANON_ACCESS.md` · `CANON_LEARNING_DOSSIER.md` · `CANON_337_600_DOSSIER.md` | What canon is held and what it says. |
| `SL4_RESEARCH.md` | Research for the future **Soul Land 4** project (a **new** OC — Lin Hao is not dead, his fate is open). |
| `chapters/` | `chapter_01.md` … `chapter_71.md` |
| `checks/` | **The thirteen-layer verification suite. `sh checks/run_all.sh` must exit 0.** |

### Commands

```bash
cd /home/user/Soul_Land_3_Project

sh checks/run_all.sh              # THIRTEEN layers; must exit 0. Also regenerates and re-mirrors.
python3 checks/state.py --show    # state derived from the chapter footers — LOOK AT IT
python3 /home/user/CODEX/consequence.py brief   # read before writing anything
```

`run_all.sh` **stage 0** derives `state.json`, `LIN_HAO_STATUS.md`, `CONTINUATION_PROMPT.md`, rewrites the
`### Ensemble` block in all 69 footers. **Nothing derivable is typed, and nothing is duplicated.**

---

## THE THIRTEEN LAYERS

| # | Check | What it catches |
|---|---|---|
| 0 | *regenerate* | derives state, ensemble blocks, status docs, mirrors |
| 1 | `verify.py` | rules — structure, laws, progression, locks, codex records |
| 2 | `verify2.py` | semantics — continuity, threads, prose quality, descriptors |
| 3 | `audit.py` | cross-chapter facts — ages, canon values, rings, ensemble presence |
| 4 | `verify_ensemble.py` | canon characters' ranks, power, rings, roster, departures |
| 5 | `verify_stale.py` | **nothing is out of date** — generated docs, **all five mirrors**, and **every live-state marker in every working document** |
| 6 | `consequence.py` | every consequence of every registered premise has landed |
| 7 | `verify_canon_quotes.py` | **57/57** quotes attributed to canon exist in the corpus |
| 8 | `verify_power_scale.py` | **never weaker than Wulin in anything**; spiritual power above Gu Yue at every chapter |
| 9 | `verify_monster_law.py` | **0** candidates for him losing a same-level fight |
| 10 | `verify_butterfly.py` | canon's hierarchy does not survive him being in the room |
| 🔴 11 | `verify_footer_facts.py` | **the hand-written footer must not contradict the derived one.** Found **99 contradictions on its first run** in a project passing the other ten. |

---

## CANON

**`canon_extract/chapters/`** — **372 canon chapters**, canon **ch 229–600** (the future source for
fan-fic ch 63+), **4.0 MB**. 🔴 Adapted chapters (23–228) were **reclaimed 2026-08-29**; the 35 we cite
are frozen verbatim in `CODEX/CANON_QUOTE_SOURCES_FROZEN.txt`, and the full source remains archived in
`CODEX/98_CANON_SOURCE_PDFS_*.tar.gz` (re-extractable via `ingest.py`). **Title index: `canon_extract/INDEX.txt`** (372 lines).

- **Only gap in the held range: canon ch 28.**
- **Canon ch 1–22 are not held** — supplied as pasted text at the start of the project.
- **Nothing past canon ch 600**, and **600 is not the ending.**
- **Canon 337–600 is skimmed, not read line by line.** A skim is not a source.

### Ingesting more canon

```bash
pip install pypdf                 # does NOT persist between sessions — reinstall each time
python3 /home/user/canon_extract/ingest.py <pdf> --out /home/user/canon_extract/chapters
```

Reports **NEW / CHANGED / UNCHANGED / MISSING** and never overwrites silently. 🔴 **Its header regex is
dash-optional** — a strict version found 54 chapters in a PDF that contained 115.

The nine source PDFs are archived in **`CODEX/98_CANON_SOURCE_PDFS_2026-08-28.tar.gz`** (7 PDFs)
and **`CODEX/98_CANON_SOURCE_PDFS_337-600_2026-08-28.tar.gz`** (2 PDFs). Restore with:
`mkdir -p uploads && tar xzf CODEX/98_CANON_SOURCE_PDFS_2026-08-28.tar.gz -C uploads`

---

## REUSABLE METHOD

**`FANFICTION_FRAMEWORK.md`** — the project-agnostic method. The sections that save the most time:

- **§4.13 🔴 THE TWO-COPIES LAW** — *a fact maintained in two places will be wrong in one of them, and
  the check reads the other.* The root cause of nearly every recurring defect in this project.
- **§6 ⚠️ THE FIVE MIS-MEASUREMENTS** — how to calibrate a threshold before obeying it.
- **§4.7 THE CONSEQUENCE SYSTEM** — imagination was never the problem; consequence-tracking was.
- **§4.12 THE BUTTERFLY LAW** — copying canon is transcription, and it silently erases the OC.
- **§8 🔴 PER-CHAPTER WORKFLOW** — *"update everything, every time,"* as twenty enforced steps.

**`checks_lib/verify_base.py`** — the project-agnostic check harness.

### Where the story is going

**Shrek Academy**, reached around canon ch 291, at age thirteen, through an entrance exam held **once
every three years**. **Wu Zhangkong is from Shrek** (canon ch 204) — a **scheduled reveal**, not a
permanent omission. 🔴 **The FOURTH-RING ARC** is locked and waiting: rank **40 → 45**, **BLACK** ring,
ten-thousand-year ice+water dragon jiao, **Frost Abyss Domain**, a month-long absorption, he ends up
looking ~16. **"Divine Stormbringer" is CANCELLED — never name or foreshadow it.**

---

## OTHER

**`CODEX/`** — the thinking tools. 🔴 **It no longer mirrors the project.** Mirrors were deleted
2026-08-29 under §THE TWO-COPIES LAW; Layer 5 fails if any of them is recreated.

| File | Purpose |
|---|---|
| `00_MASTER_INDEX.md` | Orientation and the current state. **Checked for staleness.** |
| `01_UNIVERSAL_CODEX.md` | Canon-agnostic laws shared by any story |
| `REASONING_ENGINES.md` | The ten reasoning engines in one file (index: `01_UNIVERSAL_CODEX.md` Part 40) |
| `CANON_QUOTE_SOURCES_FROZEN.txt` | The 35 canon chapters our quoted lines verify against, verbatim |
| `reference/` | The Adaptation Talent foundation — Lin Hao's martial-soul spec (3 documents) |
| `consequence.py` | 🔴 **The consequence tool.** `brief` · `impact` · `premise` · `check` · `decide --find` |
| `CONSEQUENCE_RULES.md` | The "if X enters the story, Y must follow" library. Every rule earned by a failure. |
| `CONSEQUENCE_REGISTRY.md` | **8 open premises**, 0 unlanded consequences |
| `DECISION_JOURNAL.md` | **D001–D031.** Every AU decision with its reason and its cost. **Search it before deciding anything.** |
| `97_CLEANUP_LOG.md` | What was archived and removed, and when |
| `98_*.tar.gz` | **Archives.** Other projects, source PDFs, superseded drafts. Recoverable. |

**Archived 2026-08-28** (in `CODEX/98_OTHER_PROJECTS_ARCHIVE_2026-08-28.tar.gz`, 20 entries, verified):
`BTTH_Project/` · `02_PROJECT_BTTH.md` · `03_PROJECT_MARVEL_COSMIC.md` · `04_PROJECT_ONE_PIECE.md`.
**This workspace is Soul Land 3 only.**

---

## 🔴 THE RULES THAT COST THE MOST TO LEARN

1. **A fact in two places will be wrong in one, and the check reads the other.** One source, everything
   else derived. When two sources disagree, **the prose wins.**
2. **When a belief changes, the check enforcing it must change in the same edit** — or the mistake is
   immortal. A `LIN_BAND` table enforced a retired power curve for forty chapters.
3. **Never fabricate a source URL.** Only text you actually hold is canon. **A wiki is not canon.**
4. **Copying a canon beat without asking *"what does this look like differently because he is standing in
   it?"* is transcription, not adaptation** — and it silently erases the OC from his own story.
5. **A check that cries wolf gets ignored.** Name every false positive, exempt it in the code with a
   comment saying why, and only then obey the output.
6. **Before logging anything as missing, scan for the *concept* across all chapters — not one keyword.**
   Five things were logged as absent that were present.
7. **A parser that returns the wrong value quietly is worse than one that crashes.** Print the derived
   value back and look at it.
