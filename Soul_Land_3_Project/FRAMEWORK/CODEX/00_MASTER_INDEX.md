# ║ MASTER INDEX ║

**Workspace: SOUL LAND 3 ONLY.** Cleaned 2026-08-28 at the user's instruction — every other project
was archived and removed.

---

## What is here

| Path | What it is |
|---|---|
| **`Soul_Land_3_Project/`** | ★ **THE STORY.** **71 chapters, ~230.4k prose words.** Chapters, codex, status, checks. |
| **`canon_extract/`** | The canon corpus — **372 chapters (canon ch 229–600, 4.0 MB)** = the future source for fan-fic ch 63+. 🔴 Adapted chapters (23–228) **reclaimed 2026-08-29**; the 35 quote-sources are frozen in `CODEX/CANON_QUOTE_SOURCES_FROZEN.txt`; full source archived in `CODEX/98_CANON_SOURCE_PDFS_*.tar.gz`. Plus `ingest.py` and `INDEX.txt`. **Canon 600 is NOT the ending.** |
| **`CODEX/98_CANON_SOURCE_PDFS_2026-08-28.tar.gz`** | 🔒 The seven source canon PDFs (13.6 MB), archived 2026-08-28. Restore with `mkdir -p uploads && tar xzf CODEX/98_CANON_SOURCE_PDFS_2026-08-28.tar.gz -C uploads` |
| **`CODEX/`** | The thinking tools. 🔴 **Not a mirror of the project** — mirrors deleted 2026-08-29 (§THE TWO-COPIES LAW). |
| **`FANFICTION_FRAMEWORK.md`** | The reusable method — laws, progression lines, the verification suite, the consequence system. |
| **`checks_lib/verify_base.py`** | The project-agnostic check harness `Soul_Land_3_Project` builds on. |
| **`README.md`** | Workspace orientation. |

## What is in `CODEX/`

| File | Purpose |
|---|---|
| `01_UNIVERSAL_CODEX.md` | Canon-agnostic laws shared by any story |
| `consequence.py` | 🔴 **The consequence tool.** `brief` before writing · `impact` · `premise` · `check` · `decide --find` |
| `CONSEQUENCE_RULES.md` | The "if X enters the story, Y must follow" library. Every rule earned by a failure. |
| `CONSEQUENCE_REGISTRY.md` | Open premises and their unlanded consequences |
| `DECISION_JOURNAL.md` | Every AU decision with its reason and its cost. **Search it before deciding anything.** |
| `REASONING_ENGINES.md` | The ten reasoning engines, consolidated into one file (index: `01_UNIVERSAL_CODEX.md` Part 40) |
| `reference/` | The Adaptation Talent foundation — Lin Hao's martial-soul spec (3 documents) |
| `CANON_QUOTE_SOURCES_FROZEN.txt` | The 35 canon chapters our quoted lines are verified against, verbatim |
| `97_CLEANUP_LOG.md` | What was archived and removed, and when |
| `98_*.tar.gz` | **Archives.** Other projects and superseded drafts live here, recoverable. |

---

## The one command

```bash
cd /home/user/Soul_Land_3_Project && sh checks/run_all.sh      # must exit 0
```

**Thirteen layers:** regenerate → rules → semantics → cross-chapter audit → ensemble → staleness →
consequences → canon quotes → power scale → monster law → butterfly → footer facts → **the voice** →
**the clock**.
🔴 **Layer 11 is the one that matters most:** it diffs every hand-written footer against the derived
state. It found **99 contradictions on its first run** in a project that was passing the other ten.

## Before writing anything

```bash
python3 /home/user/CODEX/consequence.py brief
```

---

## 🔴 CURRENT STATE (end of Chapter 71)

> The authoritative live copy is **`Soul_Land_3_Project/LIN_HAO_STATUS.md`**, which is **GENERATED**
> by `checks/build_status.py` from `checks/state.json`, which is derived from the chapter footers.
> **This table is a convenience and must be updated every chapter — Layer 5 fails if it is not.**

| | |
|---|---|
| **Chapters** | **69** · ~226k prose words |
| **Rank** | 40 — **Soul Elder — THE GATE** · 🔴 the fourth-ring arc has BEGUN (the jiao found, absorbing — ONE MONTH) |
| **Effective combat power** | 🔴 **Soul King (51–60)**, ceiling Soul King peak — **15 ranks above his paper** |
| **Rings** | **three PURPLE**, perfectly compatible |
| **Spiritual power** | **338** / 499 (Spirit Connection) — the wall is **SPIRIT SEA at 500** |
| **Gale Hawk** | **1,490 years** · wind + lightning · both crossings done · **the fourth ring is forming (the jiao)** |
| **Ledger** | **124 lines** |
| **Smithing** | 🔨 4th rank — **Grandmaster**, the Halo (Master Craftsman is rank 5) |
| **Swordsmanship** | ⚔️ Sword Intent |
| **Position** | has said yes to Shrek · 🔴 **has told Gu Yue the whole of it** · going to find out who forged the blade |
| 🔴 **NEW at ch62** | **Wu Zhangkong is a TWO-WORD BATTLE ARMOR MASTER (Sky Ice)** — six rings, **twenty ranks above his paper**, effectively Soul Douluo. **He is the same shape as Lin Hao, forty years further along.** See `THE_CODEX.md §THE BATTLE ARMOR LAW`. |

## 🔴 OWED — the full list lives in `Soul_Land_3_Project/PROBLEM_INVENTORY.md`

> 🔴 **CORRECTION, 2026-08-29.** This list said **"F1 — the purple-ring skill evolution is unwritten,
> this blocks any honest combat chapter."** **That was false and I propagated it into four documents
> without reading ch40.** F1 **CLOSED IN ch40**: *"Gale Talon is now a thousand-year soul skill — he lays
> the same strike he has laid four hundred times, changes nothing, and a thirty-metre deadfall comes
> apart instead of opening."* Gu Yue: *"Your skill didn't improve. It got **older**… A soul ring isn't a
> container. It's a **permission**."* `verify_ensemble.py` already detects the evidence in prose.
> The stale line came from `CONTINUATION_PROMPT.md`, which **hard-coded it** — that generator now parses
> the inventory instead. **The problem IDs below are renumbered K1–K8 because F1–F8 were already taken
> by a closed series in `PROBLEM_INVENTORY.md`.**

- **K1 — ✅ retracted, see above.** What *is* genuinely unwritten is **Hawk-Soul Union's** upgrade —
  because its first use is still reserved (D006). See K7.
- **K2 — THE FOURTH-RING ARC IS NOT WRITTEN.** Rank 40 → 45, **BLACK** ring, ten-thousand-year ice+water
  dragon jiao, **Frost Abyss Domain**, a month-long absorption, he ends up looking ~16. **He has 4 ranks
  of headroom left.** 🔴 **"Divine Stormbringer" is CANCELLED — never name or foreshadow it.**
- **K3 — 「三雷合鸣」 Three Thunders in One Voice** — the synchronisation of all three skills — has never
  been done on-page. Largest multiplier in his kit.
- **K4 — 🔴 NEW: the battle-armor-smithing thread is OPENED.** Xie Xie decided out loud: *"you're going
  to make the metal."* Mu Chen's canon line — *"the foundation of a battle armor master stems from being
  a first-rank blacksmith"* — was never connected to Lin Hao until ch62. **Must not be dropped.**
- **K5 — 🔴 NEW: Shen Yi is Wu Zhangkong's TEACHER**, now on the page. Their history is unexplored and
  **Shrek is still not named as his origin** (canon ch204 reveal).
- **K7 — 🔴 HAWK-SOUL UNION HAS NEVER BEEN USED ON-PAGE — 62 chapters in.** Deliberate (D006), but it
  upgraded to thousand-year tier at ch40 and that half has never been shown. **The debt is not the
  upgrade; it is that the trump card has no shape in the reader's mind after 62 chapters.**

## Open canon gaps (verified 2026-08-29 against `canon_extract/INDEX.txt`)

- **372 chapters on disk, canon ch 229–600, 4.0 MB** (future source). Adapted 23–228 reclaimed 2026-08-29; 35 quote-sources frozen in `CODEX/CANON_QUOTE_SOURCES_FROZEN.txt`; full source in the archived PDFs.
- **Canon ch 28** is absent from every source PDF. It is the only gap in the held range.
- **Canon ch 1–22 are not held** — they were supplied as pasted text at the start of the project.
- **Nothing past canon ch 600**, and **600 is not the ending** (at 600 Wulin and Gu Yue are travelling
  in a foreign land at a blacksmith's stall).
- **Canon 337–600 is skimmed, not read line by line.** `CANON_337_600_DOSSIER.md` is the skim, and a
  skim is not a source.

## Removed 2026-08-28 (archived, not lost)

- `BTTH_Project/` — *Battle Through the Heavens: The Adaptive Cousin*, 11 chapters
- `CODEX/02_PROJECT_BTTH.md`
- `CODEX/03_PROJECT_MARVEL_COSMIC.md` — *The First Triune*, 2 chapters
- `CODEX/04_PROJECT_ONE_PIECE.md` — *One Piece: Kai*, 7 chapters

All in **`CODEX/98_OTHER_PROJECTS_ARCHIVE_2026-08-28.tar.gz`** (20 entries, verified recoverable).
To restore: `tar xzf CODEX/98_OTHER_PROJECTS_ARCHIVE_2026-08-28.tar.gz -C /home/user`
