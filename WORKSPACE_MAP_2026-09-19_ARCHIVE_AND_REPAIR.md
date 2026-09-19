# WORKSPACE MAP DELTA — 2026-09-19 (archive + repair pass)

Second delta of 2026-09-19. The first, `WORKSPACE_MAP_2026-09-19_STORYOS_INDEX.md`, added the
StoryOS index and Dragon Prince Yuan. This one **acts on** what that index found.

Scope: 3 of the 4 GitHub repositories in this account. No prose was written. No character
value, lock, firewall or learned rule was changed. No file was deleted anywhere.

---

## 1. Soul Land 4 — two stale top-level copies archived

`WORKSPACE_MAP_2026-09-19_STORYOS_INDEX.md` found five copies of the same project, two of them
frozen at **Chapter 31** while the live edge is **after Chapter 51, `The Cost of Quiet`**. The
author approved archiving them.

| Moved from | Moved to | Files |
|---|---|---|
| `soul_land_4_fire_phoenix/` | `_archive/2026-09-19_stale_sl4_copies_at_ch31/soul_land_4_fire_phoenix_STALE_ch31/` | 173 |
| `sl4_fire_phoenix/` | `_archive/2026-09-19_stale_sl4_copies_at_ch31/sl4_fire_phoenix_STALE_ch31/` | 172 |

Method: `git mv`. **345 renames, every one recorded as `R100` — 100% similarity. Zero
deletions, zero content changes.** Only paths moved; `git log --follow` still reaches the
history. `_archive/` was chosen because `README.md` already defines it as
"superseded — never read it as current", and because `SL_ARCHIVE/` is itself stale (its SL4
material stops at Chapter 14).

Markers added: `README_STALE_ARCHIVED.md` inside each directory, plus a `README.md` for the
archive folder. Nothing else was added to the archived trees.

### Duplicate finding

`sl4_fire_phoenix/soul_land_4_fire_phoenix/` (168 files) was verified by git blob SHA to be a
**strict byte-identical subset** of `soul_land_4_fire_phoenix/` (173 files): 168 shared paths,
168 identical, 0 differing, 0 unique to the subset. Both were archived anyway rather than
deduplicated by deletion, because deletion would break the standing rule. Git stores one blob
per unique content regardless of path, so keeping both costs no repository space — only the
confusion of two live-looking paths, which the archive removes.

### The dangerous file

`sl4_fire_phoenix/SOUL_LAND_4_FIRE_PHOENIX_NEXT_STEPS_FOR_CONTINUATION.md` (2125 bytes) is not
merely old, it is **contradicted by an explicit ban**. It presents as current:

- `Dawnflame Kite … 1,120 years / newborn purple-tier` — `foundation/STATUS_PANEL.md` §9 bans
  `Dawnflame 960 or 1,120`
- `Dawn-Iron Phoenix Roc … 2,040 years` — §9 bans `Dawn-Iron 2,480 or 2,040`
- `Yan Shuo'er … remains Rank23/SP156` — true value at the current edge is Rank39/SP962
- `No third ring/soul spirit yet; no Level30; no Purple Flame Eidolon Bird yet; no full Fire
  Phoenix/Ultimate Fire/full wings/true flight` — all have since happened

It also names a dead sandbox path as "Active project". An agent trusting its title would have
regressed the project twenty chapters and re-committed two banned values. Left byte-identical
(blob `2d4dcc1f`) as the historical record; documented in its directory's marker.

### Rebuilt entry point

A **new** root file, `SOUL_LAND_4_FIRE_PHOENIX_NEXT_STEPS_FOR_CONTINUATION.md` (10606 bytes),
replaces the stale workspace-root next-steps document that carried the Chapter 35 edge. Every
value in it was taken from `foundation/STATUS_PANEL.md`; nothing was invented. It states its
own non-authority ("on any conflict, `STATUS_PANEL.md` wins and this file is wrong") and
defers the full forbidden-value list to §9 rather than mirroring it, per the TWO-COPIES LAW.
Superseded numbers are described in words, never restated, so the file cannot itself become a
drift finding.

Note the name collision: the archived Chapter-31 file and the earlier workspace-root
Chapter-35 file are **different documents sharing a basename**. Both are now accounted for.

---

## 2. Soul Land 4 — eight stale live-edge directives repaired (private repo)

In `gm5206663-bit/soul_land_4_fire_phoenix`, commit `6ae3553`.

Eight active-tree files claimed a current live edge other than Chapter 51 while the project's
own validator reported `active_stale_issues=0`:

| File | Claimed |
|---|---|
| `bible/YAN_SHUOER_IDENTITY_AND_APPEARANCE.md` | after Chapter33 |
| `bible/PROTAGONIST.md` (two lines) | after Chapter34, after Chapter35 |
| `canon_coverage/Phoenix_Dragon_Canon_Dossier.md` | `CURRENT OVERRIDE after Chapter35` |
| `bible/ADAPTATION_TALENT_LOCAL.md` | after Chapter49 |
| `bible/FIRST_RING_ACQUISITION.md` | after Chapter49 |
| `foundation/DAWNFLAME_FORM_AND_SOUL_SPIRIT_FUSION_RULES.md` | after Chapter49 |
| `foundation/FIRE_LIGHT_ATTRIBUTE_LOCK.md` | after Chapter49 |
| `foundation/PRECISION_AND_GROWTH_LOCKS.md` | after Chapter49 |

The worst was `Phoenix_Dragon_Canon_Dossier.md`, whose line 1 was a `CURRENT OVERRIDE` block
carrying superseded power values while line 3 of the same file disclaimed being a status
source. Relabelled `HISTORICAL SUPERSEDED OVERRIDE (as of Chapter35) — NOT CURRENT`, values
named as superseded, pointer to `STATUS_PANEL.md`. Historical text preserved throughout;
nothing deleted.

### Why the validator missed them

Three causes, each confirmed by replaying the validator's own logic:

1. `allowed_historical()` exempts a line when the filename, the line, or ±4 lines of context
   match any of 23 historical patterns. `bible/PROTAGONIST.md:86` contains the word
   "historical" three sentences *before* its stale claim, on the same line — so the stale claim
   was exempted. All eight files were hidden this way.
2. Neither built-in live-edge regex matched these phrasings. One requires a literal colon
   (`Live edge:…Chapter(\d+)`), so `Live edge is after ChapterNN` slipped through; the other
   allows only six fixed prefixes, so `Current live edge is after ChapterNN` slipped through.
3. `canon_coverage/` was not in `active_markdown_dirs`.

### Why the fix went into the tool, not the manifest

`active_stale_regexes` are **absolute**: `check_active_files` does `if regex.search(line):
add(issues, …)` with no comparison against `state.latest_fic`. Only
`dynamic_stale_checks_for_line()` compares numbers. A manifest regex therefore cannot express
"chapter ≠ current".

This was tested rather than assumed. Adding `Live edge:\s*\**\s*after Chapter(\d+)` to
`active_stale_regexes` produced **73 issues, 48 of them false positives** — it flagged every
*correct* `Live edge: **after Chapter51**` header in `foundation/`. Reverted. Adding
`canon_coverage` to `active_markdown_dirs` was also tested and rejected: roughly 20 false
positives from per-chapter coverage receipts (`Canon_Coverage_Chapter_41.md` legitimately says
"next chapter should cover Chapter159"), because that mechanism has no per-chapter exemption.
The validator already special-cases `foundation/CANON_LEDGER.md` for exactly this class of
false positive.

So `tools/perfect_continuation_skill_check.py` gained a **directive class** checked *before*
the historical exemption: `LIVE_EDGE_DIRECTIVE_REGEXES` (four phrasings) plus
`live_edge_directive_problems()`, which compares the claimed chapter to `state.latest_fic`,
exempts a file whose own name carries that chapter number, and deduplicates double reports.
Rationale: a directive tells the reader what is true **now**; it cannot be made historical by
an adjacent clause. Historical *values* remain exempt exactly as before. Because it compares
against `state.latest_fic`, it needs **no regeneration when the edge moves** — unlike
`active_stale_regexes`, several of which hard-code Chapter52/53/176.

Regression-tested, probe file then deleted:

| Probe | Expected | Result |
|---|---|---|
| stale directive behind historical wording (the original bug) | FAIL | FAIL, 1 issue, correct line |
| `Live edge: **after Chapter35, …**` | FAIL | FAIL, 2 issues |
| `> CURRENT OVERRIDE after Chapter35:` | FAIL | FAIL, 1 issue |
| control: correct Chapter 51 directives | PASS | PASS, 0 issues |

The control matters: `active_stale_issues=0` was also the *buggy* answer, so a PASS alone
proved nothing.

Receipt: `audits/STALE_LIVE_EDGE_DIRECTIVE_REPAIR_2026-09-19.md` in that repository.

---

## 3. Dragon Prince Yuan — gate FAIL resolved to PASS

`WORKSPACE_MAP_2026-09-19_STORYOS_INDEX.md` reported this project's gate as **FAIL**. Two
distinct causes, only one of which was the project's fault.

**Scanner bug (mine).** The StoryOS scanner hard-coded a list of 11 SL4-specific
`foundation/` filenames as the only places firewalls could live. Dragon Prince Yuan declares
its firewalls in `foundation/KNOWLEDGE_FIREWALLS.md`, so it scanned as **zero firewalls** and
was failed for it. Fixed in `gm5206663-bit/storyos-site` commit `686bb38`: discovery is now
generic (`foundation/KNOWLEDGE_FIREWALLS.md` plus any `foundation/*LOCK*.md`, `*FIREWALL*.md`,
`*GUARD*.md`, `*POLICY*.md`), and status is read from the file rather than assumed — a firewall
the project itself still marks TBD now reports `PARTIAL / TBD` instead of `LOCKED`. Side
effect: SL4 went from 11 to 18 firewalls, because generic discovery found 7 real boundary
documents the hard-coded list had missed.

**Genuine gap (the project's).** No `foundation/CURRENT_STATE_MANIFEST.json`, so the live edge
was not machine-readable and the gate failed on `if not manifest`. Now authored at 29 files,
**every value derived from the project's own files** — `codex/CHAPTER_PROGRESS.md`,
`foundation/STATUS_PANEL.md`, `foundation/CANON_SOURCE_MAP.md`, `codex/TIMELINE.md`,
`canon_coverage/Canon_Coverage_Chapter_01.md`, `audits/CHAPTER_01_VALIDATION_2026-09-13.md`. A
`provenance.derived_from` block names the source file for each field. Nothing was invented:
the cultivation realm stays `TBD — not stated yet, do not invent`, and
`open_items_requiring_user` lists the four things only the author can resolve.

**Two stale headers corrected.** Both files carried a pre-prose status line *above* a
later-appended correct live-edge section, so a reader who stopped at the top got the wrong
state:

- `HANDOFF.md` — `Status: foundation initialized, no prose yet.` → marked **SUPERSEDED**, with
  a pointer to the live edge. Chapter 1 exists.
- `foundation/START_HERE.md` — `Do not write Chapter 1 yet` → the "Absolute startup rule"
  section marked **STATUS: COMPLETED — this gate has been passed**, with the eight-lock
  checklist preserved as historical discipline and as the reset procedure.

No instruction text was deleted in either file.

**Still open, and needing the author, not an agent:** exact cultivation realm for Zhou Xu;
project-specific knowledge-firewall boundaries (`KNOWLEDGE_FIREWALLS.md` still says
"TBD after user locks OC background and relationship to canon cast"); wine-quirk handling;
name confirmation. Chapter 2 is blocked on fetching novel Chapter 2 `Genesis Runes`, which has
not been read.

Receipt: `audits/STALE_HEADER_AND_MANIFEST_REPAIR_2026-09-19.md` in that project.

---

## 4. Verification after the pass

| Check | Before | After |
|---|---|---|
| SL4 `tools/perfect_continuation_skill_check.py` | PASS, `active_stale_issues=0` (**wrong** — 8 real issues invisible) | PASS, `active_stale_issues=0` (**correct** — regression-tested to fail on injected stale directives) |
| SL4 independent drift scan | 8 findings | **0 findings / 165 active files** |
| SL4 StoryOS gate | WARN, drift 11 | **PASS, drift 0** |
| DPY StoryOS gate | FAIL, no machine-readable edge | **PASS, edge Ch1, drift 0, firewalls 1 (PARTIAL/TBD)** |
| DPY independent drift scan | not scannable (no edge) | **0 findings** |
| SL4 top-level stale copies in this repo | 2 | **0** |
| Files deleted anywhere | — | **0** |

Both projects now pass their own gates and an independent scanner, and the two scanners agree.

Still legitimately unresolved and **not** papered over: SL4 Chapter 52 remains blocked because
source Chapter 177 `1,000-year Purple Zoysia` has not been fetched. That is a missing-source
condition, correctly reported rather than invented around.

---

## 5. Standing privacy finding — unchanged, still needs the author

The `soul_land_4_fire_phoenix` repository is **private**, but
`arena_managed_uploads/2026-09-18_chapter51_managed_snapshot/soul_land_4_fire_phoenix/` inside
this **public** repository holds all 653 of its files byte-identically — all 51 chapters,
`foundation/`, the knowledge firewalls, and
`YAN_SHUOER_BEAUTY_IDENTITY_PRESSURE_LOCK.md`. The private repository's visibility setting is
therefore void in practice.

This pass did **not** touch that snapshot. Archiving it was not approved and would remove the
only public copy of the current state, so the decision is left deliberately to the author.
Options: make the private repo public (accept it), move the snapshot to the private repo and
delete it here (requires a history rewrite to actually remove it), or leave as-is knowing the
content is public.

---

## 6. Commits

| Repository | Commit | Change |
|---|---|---|
| `soul_land_4_fire_phoenix` (private) | `6ae3553` | 8 stale directives repaired + validator directive class + audit receipt. 10 files, +220/−9. |
| `storyos-site` (public) | `686bb38` | Generic firewall discovery. 1 file. |
| `soul-land-universal-kit` (public) | this commit | 345 renames (archive) + 3 markers + DPY 3 files + rebuilt root NEXT_STEPS + 3 index docs updated + this delta. |
| `soul-land-projects` (public) | separate | Third stale SL4 copy archived the same way. |

No credentials, tokens or keys were written into any repository. Each push used a token held
only in an environment variable for the duration of the command, and every remote URL was
reset to its token-free form immediately afterwards; `git grep` for the token pattern returns
nothing in any working tree or `.git/config`.
