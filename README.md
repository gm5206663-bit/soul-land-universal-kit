# ═══ WORKSPACE MAP — read this first ═══
**Every future chat/agent: the truth lives in exactly these places. Anything in `_archive/` is superseded — never read it as current.**

🔴 **LIVE BUILD:** `soul_land_devouring_dragon/` — the devouring-dragon serial (21 chapters, plain-language prose, all gates PASS; ch 21 *The Watch and the Pass* shipped 2026-09-23 under the author's standing delegation). Start at its `HANDOFF.md`; laws in its `foundation/RAILS.md`; live edge in its `foundation/STATUS_PANEL.md`. See the 2026-09-21 addition at the end of this file.

## Authoritative trees (write here, read here)

| Path | What it is | Governs |
|---|---|---|
| **`Soul_Land_3_Project/`** | Branch 05 — Soul Land 3 "The Adaptive Prodigy" (OC Lin Hao) — 🔴 **UPDATED 2026-09-18: now 116 chapters / 354,685 story words (suite-counted), full-spectrum repair pass green** | `README.md` (start here) · `THE_CODEX.md` (v3.06) · `chapters/chapter_01–71.md` · `checks/` (**`sh checks/run_all.sh` must exit 0**) · `POWER_MODEL.md` · `CHARACTER_STATS.md` · `RELATIONSHIPS.md` · `PROBLEM_INVENTORY.md` · `CANON_COMPARISON_ch66-71.md` · `FRAMEWORK/` (its own CODEX + `FANFICTION_FRAMEWORK.md`) · `ARCHIVE_THIRD_PASS_VERIFICATION.md` (history) |
| **`Soul_Land_2_Project/`** | Branch 06 — Soul Land 2 "The Unraveled Tide" (OC Jiang Che) — **PAUSED 2026-09-23 at 24 chapters (incl. 8-B *The First Rank*); revival queued** | `THE_CODEX.md` (v3.4) · `JIANG_CHE_STATUS.md` · `REVIVAL_QUEUE_2026-09-23.md` (the restart plan) · `chapters/` (24) |
| **`soul_land_2_new/`** | Branch — Soul Land 2 **"The Golden Lion"** (OC Jin Yang — village-born, Golden Lion martial soul, womb-born Adaptation Talent, walking to Shrek at eleven) — 🔴 **LIVE, agent-driven, near-daily: Chapter 7 *Three Months* (2026-09-23, P-13 law, panel v18)** | `foundation/` (STATUS_PANEL · SERIAL_LOG · AUTHORS_LAW · NATURAL_DOCTRINE · THE_LION_MODULE · THE_GOLD_REGISTER) · `chapters/` (7) · `checks/verify.py` (gate **sl2-goldenv**) · `codex/` |
| **`Soul_Land_5_Project/`** | Branch — Soul Land 5 "The Second Heartbeat" (working title, D-004) — OC = Tang San's twin brother, Falan-native, no past life — 🔴 **FOUNDATION STAGE: no chapters yet** (added 2026-09-18) | `SL5_CODEX.md` (rulings R1–R4, decisions D-001…D-005) · `SL5_RESEARCH.md` · `SL5_CANON_ACCESS.md` (primary-source method) · `SL5_BUTTERFLY_REGISTRY.md` (B1/B2, ripple rules §C) · `SL5_PROBLEM_INVENTORY.md` · `SL5_CONTINUATION_PROMPT.md` (start here) · `SL5_TWIN_STATUS.md` (ch1 status panel — source of truth) · `canon_extract/` (held SL5 canon text: ch 001/002/003/010/014 + `INDEX.txt`) |
| **`soul_land_3_new/`** | Branch — **NEW Soul Land 3 serial** (separate universe, R2 resolved) — ⚪ **FROZEN 2026-09-22 by author plan-change** (superseded by the Golden Lion SL2 serial; archived as-is at `a0a6473`): rulings R1–R4 RESOLVED, Chapter 01 *The Choosing* written (gate PASS `1e09f7a`); do not continue without the author's word | `README.md` · `HANDOFF.md` · `foundation/` (`RAILS.md`, `OPEN_RULINGS.md` R1–R6, `CANON_SPINE_SL3.md`, `POWER_LAW_SL3.md`, `KNOWLEDGE_FIREWALLS.md`, `STATUS_PANEL.md`, `CANON_LEDGER.md`, `SERIAL_LOG.md`) · `seeds/PREMISE_CANDIDATES.md` (P1–P6) · `codex/` · `checks/` (**`sh checks/run_all.sh`: gate selftest 10/10 + verify must exit 0**) |
| **`CODEX/`** | The Unified Codex family + mirrors | `00_INDEX.md` (family map & verification report) · `05_PROJECT_SOUL_LAND_3.md` (= SL3 codex mirror) · `06_PROJECT_SOUL_LAND_2.md` (= SL2 codex mirror) · `MASTER_STORYTELLING_CODEX.md` (v3.3 superset — working universal text) · `MASTER_STORYTELLING_CODEX_COMPLETE.md` (v4.0 partial — archived caution) · `GENESIS_CODEX*.md` (portfolio) |

## Standing rules (locked in each branch codex — obey, never re-derive)
- **USE EVERYTHING PROTOCOL:** read all files → research canon from **primary text** before writing → run every law/test → update **every** file after (codex, status, continuation, chapter footer, mirror, `00_INDEX.md`).
- **The Multi-Panel Law** (SL2): donghua-style panels; canon always **shown**, never skipped; the OC is **added**, never centered.
- **The Canon-First Creation Law:** check canon before inventing; butterfly-check; **personality-first**; style-match canon; self-audit every chapter (small things become big).
- **The Unfixed Law:** for AT holders nothing is fixed — traits are dated states; power is a **baseline**, never a ceiling.
- **Natural-Ripple Principle:** nothing pre-decided (romance included); canon spine; bends only when earned + logged.
- Mirror sync after every codex change: `cp Soul_Land_X_Project/THE_CODEX.md CODEX/0X_PROJECT_….md`.
  🔴 **EXCEPT Soul Land 3.** That project retired its mirror on 2026-08-29 under its own **TWO-COPIES LAW** (*"a fact maintained in two places will be wrong in one of them, and the check reads the other"*), and its Layer 5 now **fails if a second copy reappears**. **The v2.25 snapshot at `CODEX/05_PROJECT_SOUL_LAND_3.md` was archived on 2026-09-18 to `Soul_Land_3_Project/_attic/CODEX_05_PROJECT_SOUL_LAND_3_stale_v2_25.md` (the staleness layer enforces this).** The single source of truth is `Soul_Land_3_Project/THE_CODEX.md`. This rule still applies to Soul Land 2.

## `_archive/` — DO NOT USE
`_archive/2026-08-25_uploads/` holds the original uploads from earlier sessions (pre-v2.26 SL3 snapshots, the Chapter-4-era fossil codex, the stale continuation). Kept for provenance only; every file there is superseded by the trees above.
`_archive/2026-09-18_workspace_uploads/` (added 2026-09-18) holds an agent-workspace snapshot of the SL3 docset from the chapter-01 audit era — also fully superseded by `Soul_Land_3_Project/`.
`_archive/2026-09-19_stale_sl4_copies_at_ch31/` (added 2026-09-19) holds the **two stale top-level Soul Land 4 copies** (`soul_land_4_fire_phoenix/`, `sl4_fire_phoenix/`), both frozen at **Chapter 31** while the project is now at **Chapter 52**. Moved by `git mv` — 345 renames, all `R100`, zero deletions, zero content changes. `sl4_fire_phoenix/`'s nested 168-file tree was verified a **byte-identical subset** of the other copy. Each has a `README_STALE_ARCHIVED.md`. **The archived `sl4_fire_phoenix/…/SOUL_LAND_4_FIRE_PHOENIX_NEXT_STEPS_FOR_CONTINUATION.md` is actively dangerous**: it presents `Dawnflame 1,120` and `Dawn-Iron 2,040` as current, two values `STATUS_PANEL.md` §9 explicitly bans. Never read it as state.
`_archive/2026-09-21_superseded_arena_readme/` (added 2026-09-21) holds the old root file `README_ARENA_WORKSPACE.md` —
a second, unreferenced README for this repository whose content duplicated (and had gone stale against)
the soul-land-projects README and this file, including a Chapter-51 live-edge claim. Kept, not erased;
superseded by `README.md`.

---

## ADDITION — Full Workspace Upload (2026-09-18, add-only)

Everything in the live workspace was added on this date without deleting or
overwriting anything existing. Map of the addition: see
`WORKSPACE_MAP_2026-09-18.md` at the root of this repository.

---

## ADDITION — StoryOS index + Dragon Prince Yuan (2026-09-19, add-only)

Nothing existing was deleted or overwritten. See
`WORKSPACE_MAP_2026-09-19_STORYOS_INDEX.md` for:

- **an index of every fanfiction project in this repository** — files, chapters, and whether
  each is current, superseded, dropped, forbidden, or foundation-stage
- **the Soul Land 4 five-copies finding** — the live edge is after **Chapter 52**, and two
  top-level directories (`soul_land_4_fire_phoenix/`, `sl4_fire_phoenix/`) were **stale at
  Chapter 31**. 🔴 **Both archived 2026-09-19** to
  `_archive/2026-09-19_stale_sl4_copies_at_ch31/` (see the `_archive/` section above). The
  most recent copy held in this repository is
  `arena_managed_uploads/2026-09-18_chapter51_managed_snapshot/soul_land_4_fire_phoenix/`.
  This was SL3's TWO-COPIES LAW applying to SL4, which had five places; it now has three,
  and the third (`soul-land-projects` repo) was archived the same day.
  See `WORKSPACE_MAP_2026-09-19_ARCHIVE_AND_REPAIR.md` for the full delta.
- **Dragon Prince Yuan — Zhou Xu**, added today at
  `dragon_prince_yuan_native_oc_fanfiction/` (28 files). ~~Its gate is **FAIL**~~
  🔴 **RESOLVED 2026-09-19 — gate is now PASS.** The FAIL was two things: the scanner
  hard-coded 11 SL4-specific firewall filenames, so a project declaring its firewalls in
  `foundation/KNOWLEDGE_FIREWALLS.md` read as zero firewalls (scanner bug, now generic);
  and the project had no `foundation/CURRENT_STATE_MANIFEST.json`, so its live edge was not
  machine-readable (now authored from its own files, marked generated). Two stale
  pre-prose headers were also corrected: `HANDOFF.md` said "no prose yet" and
  `foundation/START_HERE.md` said "do not write Chapter 1 yet", both above their own
  appended after-Chapter-1 live-edge sections. Now 30 files.
  Still genuinely open, and needing the **user**, not an agent: exact cultivation realm for
  Zhou Xu, the project-specific knowledge-firewall boundaries (`KNOWLEDGE_FIREWALLS.md` is
  still TBD), wine-quirk handling, and name confirmation. Chapter 2 is blocked on fetching
  novel Chapter 2 `Genesis Runes`.
- **`gm5206663-bit/storyos-site`** — the verification/publishing tooling, in its own public
  repository.

---

## ADDITION — Devouring Dragon serial + 2026-09-21 housekeeping (add-only)

Nothing existing was deleted or overwritten by these additions.

- **`soul_land_devouring_dragon/`** — the Soul Land **devouring-dragon serial** (21 chapters; plain words after the s40 PLAIN LANGUAGE LAW; every chapter passes `SOUL_LAND_WORKSPACE/kit/tools/verify.py`; the s44 road chapters shipped 2026-09-23). This is the newest live build in the repository. Read order: `soul_land_devouring_dragon/HANDOFF.md` → `foundation/STATUS_PANEL.md` (live edge) → `foundation/RAILS.md` (laws of record).
- **Housekeeping, 2026-09-21 (every deletion receipted):** scratch scripts, same-directory duplicates and one redundant export were retired; the three unique files in it were kept in `_archive/2026-09-18_perfect_export_kept/`. Full receipt list: `HOUSEKEEPING_2026-09-21.md`. No project content was edited by the housekeeping pass.

---

## ADDITION — LICENSE, NOTICE & workspace housekeeping (2026-09-23, add-only)

Nothing existing was deleted or overwritten by these additions.

- `LICENSE` (MIT) added for the **code** in this repository — tools, checkers, scripts.
- `NOTICE.md` added: Soul Land (斗罗大陆) belongs to Tang Jia San Shao (唐家三少); everything here is non-commercial derivative fan work. Prose stays read-only; code is MIT.
- Profile README repository created: [`gm5206663-bit/gm5206663-bit`](https://github.com/gm5206663-bit/gm5206663-bit).
- Sister repo `soul-land-projects` — which held byte-identical copies of `SARA.md`, `SOUL_LAND_NEW/`, `blue_silver/`, `soul_land_starter/`, and `SOUL_LAND_UNIVERSAL_KIT/` — was **archived read-only** this date (nothing deleted; this repository is the single live public workspace). It remains browsable at https://github.com/gm5206663-bit/soul-land-projects
- Rename: `the-universal-storyline-creation-` → `the-universal-storyline-creation` (trailing dash removed; the old URL 301-redirects).


---

## ADDITION — Chapter 19, The North Road (2026-09-23, add-only)

Nothing existing was deleted or overwritten by these additions.

- `soul_land_devouring_dragon/chapters/Chapter_19_The_North_Road.md` — CHAPTER 19
  "The North Road", written and gated under the author's standing delegation this
  session (verbatim: "Now work on my projects, I don't know anything just do
  everything I trust you"). The first s44 PACING-LAW chapter: six quiet years told
  as time-skip summary — the packs and the map of habit, the country taking the
  men's marks back, the two long sleeps, the pale beast's silence — and the north
  road begun (the birdless hollow, the river-road, the far standing light).
  2,000 words; PANEL: NONE; all gates PASS; sweep PASS 19/19.
- `soul_land_devouring_dragon/HANDOFF.md` created as a pointer stub (the read
  order's missing first step; the handoff itself stays in the serial README —
  Two-Copies Law).
- Mirrors synced same turn: STATUS_PANEL, HIS_STATUS_PANEL (pre-existing stale
  figures also corrected), ADAPTATION_LOG, SERIAL_LOG, PLACES, TIMELINE,
  CONTINUITY, serial README.


---

## ADDITION — The Complete Mistake Ledger (2026-09-23, add-only)

- `MISTAKES_LEDGER_2026-09-23.md` — every recorded mistake across the workspace and
  its GitHub in one index: 128 distinct mistakes, 11 author strikes that became law,
  the five-copies disaster, the two mis-cuts and their reversals, the checker bugs,
  and the still-open items. A DERIVED INDEX per the Two-Copies Law — the receipts
  live where they were first recorded and win any disagreement.


---

## ADDITION — Chapter 20, The Road Itself (2026-09-23, add-only)

Nothing existing was deleted or overwritten by these additions.

- `soul_land_devouring_dragon/chapters/Chapter_20_The_Road_Itself.md` — CHAPTER 20,
  written and gated under the standing delegation (renewed: "Continue"). The road's
  first three years: the reversal, the craft reborn at the world's new size, the
  first deep meal (the near-drowning; the jaw held; the rib-tear), the hunted week
  (the veiling's failure in the open; the meat-tax lawed), and the pass country
  found — the road's first true obstacle, under watch from the high seat.
  2,126 words; PANEL: NONE; all gates PASS; sweep PASS 20/20. Mirrors synced
  same turn.


---

## ADDITION — Soul Library, Blue Silver Book One release, revival queues (2026-09-23, add-only)

Nothing existing was deleted or overwritten by these additions.

- **THE SOUL LIBRARY is live**: https://gm5206663-bit.github.io/soul-library/ — five serials
  published as one reading site (181 chapters, 766K+ words of chapter text measured from disk).
  New repo `gm5206663-bit/soul-library`; chapter text copied unchanged; the workspace remains
  the source of truth.
- **Blue Silver — Book One v1.0 released**: tag `blue-silver-book-one-v1.0` on this repo, with
  the complete Book One as an EPUB 3 (`blue_silver_book_one.epub`) + the live chapter archive.
  `blue_silver/BOOK_TWO_OPTIONS.md` queues the Book Two ruling (three premises, canon-load-bearing).
- **REVIVAL QUEUES**: `Soul_Land_2_Project/REVIVAL_QUEUE_2026-09-23.md` (paused at ch24; the
  multi-panel law's home serial) and `soul_land_holy_spirit/REVIVAL_QUEUE_2026-09-23.md`
  (paused at ch4; the cult arc barely opened). Both parked with engines warm.
- Control Centre state refreshed same date: four serials registered, the stale SL4 edge fixed
  (Ch31 -> Ch52), rebuilt via its own pipeline (selftest 102/102).


---

## ADDITION — AGENTS.md (2026-09-23, add-only)

- `AGENTS.md` created at the root: the machine-readable contract for any AI agent
  arriving in this workspace — authority order, the eight non-negotiables, measured
  style, boundaries (live serials, private repos, source-text rules), token hygiene,
  and the read order. Formalizes the HANDOFF culture in the emerging AGENTS.md
  convention. Author word still outranks it.


---

## ADDITION — Chapter 21, The Watch and the Pass (2026-09-23, add-only)

- `soul_land_devouring_dragon/chapters/Chapter_21_The_Watch_and_the_Pass.md` — CHAPTER 21,
  written and gated under the standing delegation (the advanced plan). The pass's arc
  complete: the watch (hours, edges, the quick kinds' moonset road, the storm night),
  the old grazer's taking, the crossing inside the river, THE READING (let go whole —
  beneath notice, not mercy), and the road resumed north of the pass. 2,017 words;
  PANEL: NONE; sweep PASS 21/21. Mirrors synced same turn; AGENTS.md added (see the
  same-date addition above).
