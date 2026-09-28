# HOUSEKEEPING — 2026-09-21 (GitHub-wide pass)

Instruction this answers, verbatim: *"Update everything you have on my GitHub and replace, and also
manage my GitHub perfectly, delete wrong thing's if there is"* — session s41.

Rule applied throughout: **a file was only removed when it was a byte-identical duplicate of a file
that stays, or a scratch/dropped artifact with no reader; every removable file that had unique
content was kept.** Nothing in any project's live serial, laws, or gates was edited by this pass.

## Verified state at the end of the pass

| Repository | main | Other branches |
|---|---|---|
| `soul-land-universal-kit` | `d7458b0` (+ this receipt commit) | none |
| `the-universal-storyline-creation-` | `a6a24cf` (s40 ship, unchanged) | none |
| `soul-land-projects` | `dd39daf` (seed_of_creation merged in) | none |
| `storyos-site` | `64c1739` (unchanged) | none |
| `soul_land_4_fire_phoenix` | `7b2c641` (housekeeping) | none |

Secret scan across all five repositories: **clean** (no `ghp_`/`github_pat_`/`AKIA`/password
patterns anywhere in tracked files; `push_to_github.sh` takes the token as an argument and never
writes it to disk).

## soul-land-universal-kit — removed (commit `f1ea4bb`)

| # | Path | Size | Why it is wrong |
|---|---|---|---|
| 1 | `_c14.py` | 2.2 KB | Scratch script (a one-shot edit to the SL2 codex). Not referenced by anything; the edit it made is long since in the tree. |
| 2 | `_c15b.py` | 2.5 KB | Same, second scratch script. |
| 3 | `uploads/README (1) (1).md` | 715 B | Byte-identical duplicate of `uploads/README (1).md` (same md5). |
| 4 | `uploads/NEW_CHAT_1.md` | 5.9 KB | Byte-identical duplicate of `uploads/NEW_CHAT.md`. |
| 5 | `SL_ARCHIVE/inbox/NEW_CHAT_1.md` | 5.9 KB | Byte-identical duplicate of `SL_ARCHIVE/inbox/NEW_CHAT.md`. |
| 6 | `arena_managed_uploads/2026-09-18_chapter51_managed_snapshot/soul_land_4_fire_phoenix/YAN_SHUO_COMPLETE_CURRENT_STATUS_PANEL.md` | 17.8 KB | Byte-identical twin of `YAN_SHUO_CURRENT_STATUS_PANEL.md` in the same folder. |
| 7 | `…/audits/2026-09-15_chapter39_sync_before/YAN_SHUO_COMPLETE_CURRENT_STATUS_PANEL.md` | 17.8 KB | Same, second snapshot. |
| 8 | `…/audits/2026-09-14_chapter36_sync_before/YAN_SHUO_COMPLETE_CURRENT_STATUS_PANEL.md` | 17.8 KB | Same, third snapshot. |
| 9 | `_perfect_export_2026-09-18/**` (28 of its 31 files) | 3.8 MB | Export folder whose non-unique files are byte-identical to files already in the repo (`uploads/`, `SL_ARCHIVE/`, `_archive/2026-09-18_workspace_uploads/`). Its 3 unique files were **kept**: `_archive/2026-09-18_perfect_export_kept/receive_archive.sh`, `…/HANDOFF_SoulLand3.md`, `…/plan_extract/plan.txt`. |

**Disclosed and corrected mid-pass:** `_archive/2026-09-18_workspace_uploads/THE_CODEX.md` (664 KB)
was removed in `f1ea4bb` as a duplicate of `05_PROJECT_SOUL_LAND_3.md`, then **restored in
`d7458b0`** — that archive's own manifests (`RELATIONSHIPS.md`, `REBUILD_MANIFEST.md`,
`PROBLEM_INVENTORY.md`) cite it by that exact name. Correct final state: both copies present; the
archive is frozen history and its internal citations win over tidiness.

### Deliberately kept (checked, judged right)

- `uploads/handoff_package.txt` — its twin was inside the retired export; the live copy stays.
- `_archive/2026-09-18_workspace_uploads/05_PROJECT_SOUL_LAND_3.md` — duplicate of `THE_CODEX.md`,
  but sits in a frozen archive where its name is referenced; archive keeps its own shape.
- `Soul_Land_2_Project/cover_art.png` (3.8 MB) and `scene_card_jade_hand.png` (3.3 MB) — real art, not clutter.
- `Soul_Land_3_Project/Soul_Land_3_Project_handoff_2026-09-03.zip` (2.4 MB) — real content: it is
  the SL3 handoff archive, and `SL3_LIN_HAO/STATUS.md` waits on exactly this file (see below).
- `arena_managed_uploads/2026-09-18_chapter51_managed_snapshot/` — dated upload snapshots, correctly named; not claimed as current.

### Documents updated (outdated claims replaced)

1. `README.md` — added a top **LIVE BUILD** pointer to `soul_land_devouring_dragon/` (the serial was
   not mentioned in the map at all) and a closing **ADDITION — Devouring Dragon serial + 2026-09-21
   housekeeping** section; corrected the sentence that called the Chapter-51 SL4 snapshot "the
   current copy in this repo" (SL4 has since reached Chapter 52 in its own repo) to "most recent copy
   held in this repository".
2. `STATE.md` — dated 2026-09-08 and still declaring itself the current state; a dated banner now
   points to what is true since (Blue Silver Book One complete; newest live build =
   `soul_land_devouring_dragon/`). Original text kept as history.
3. `SL3_LIN_HAO/STATUS.md` — said the SL3 zip is "NOT on hand" and "SL3 is frozen until that zip is
   uploaded"; the zip is present in this repository (309 files, added 2026-09-18) and
   `Soul_Land_3_Project/` holds 117 chapter files. A dated banner resolves the freeze.

## Scans re-run properly before the deletions

A full same-directory duplicate scan (md5 per folder) and a junk-name scan (`(1)`, `copy`, `_old`, `.bak`, `.tmp`, `~`,
`__pycache__`) were run across all five repositories. Findings were exactly the items listed above and nothing else.
Two `(1)`-named files were checked and **kept**: `uploads/README (1).md` in the kit and in `soul-land-projects` differ in
content from `uploads/README.md` (715 B vs 4,118 B in soul-land-projects) — a different upload, not a copy.

## the-universal-storyline-creation- — checked, nothing wrong found

Registry, intake, and gates are consistent with the kit (`devouring_dragon` edge = kit `22765d8`,
Chapter 14). No deletions.

## soul-land-projects — the one branch that was not safe to delete

`arena/01a0b304-soul-land-projects` held **one commit not in main**: `195d736` "Open
seed_of_creation: an SL2.5-era serial, foundation only, no chapters" (2026-09-18). Deleting it would
have destroyed that work, so instead it was **merged into main** — merge commit `dd39daf` (clean
automatic merge; `README.md`/`STATE.md` updated, `seed_of_creation/` added). The branch was then
deleted as redundant.

## soul_land_4_fire_phoenix — removed / replaced (commit `607f7f5`)

- Removed `storyos-site/` — one file (`validation_report.txt`), an unreferenced leftover of the
  StoryOS publish stage; StoryOS has its own repository (`storyos-site`).
- ~~Removed the two byte-identical COMPLETE-panel twins inside the `audits/2026-09-14_chapter36_sync_before/` and
  `audits/2026-09-15_chapter39_sync_before/` snapshots.~~ **REVERTED** — both restored (commit `dec226e`); the dated
  snapshots keep their full history.
- ~~Replaced `YAN_SHUO_COMPLETE_CURRENT_STATUS_PANEL.md`~~ — **REVERTED, see the Second-pass
  correction below: this file is a mirror the project's own validator requires. It was restored,
  and the pointer stub removed.**

## storyos-site — checked, nothing wrong found

`published-site/` is a *generated snapshot* (its own `GENERATED.md` says so; rebuilt 2026-09-19; its
stated live edge "after Chapter 52" is still the current edge of the Fire Phoenix project), so it was
not hand-edited — it must be regenerated by `framework/scripts/publish_stage.py`. The byte-identical
pair `published-site/agents.md` / `published-site/START-HERE.md` is a served alias (the same agent
contract under two routes), not an accident — kept.

## Branches deleted on GitHub (API, HTTP 204 each)

| Repo | Branch | Audit before deletion |
|---|---|---|
| `soul-land-universal-kit` | `arena/01a0b560-soul-land-universal-kit` | 0 commits not in main (main ahead by 28) |
| `the-universal-storyline-creation-` | `gm5206663-bit-patch-1` | 0 commits not in main (main ahead by 15) |
| `soul-land-projects` | `arena/01a0b304-soul-land-projects` | 1 unique commit — **merged into main first** (`dd39daf`), then deleted |

## Repository descriptions and topics

Descriptions brought up to date (the Fire Phoenix one said "through Chapter 51" while the project is
at Chapter 52; the Storyline Creation one was the original wish rather than the repo's function),
and topics were added where none existed.

- `soul-land-universal-kit` — "Portable authoring kit + full workspace for Soul Land (Douluo Dalu)
  fanfiction — canon spine, prose and audit laws, gates, templates, and the live devouring-dragon
  serial." · topics: soul-land, douluo-dalu, fanfiction, authoring-kit
- `soul-land-projects` — "Working archive of Soul Land (Douluo Dalu) fan fiction projects — Blue
  Silver, Fire Phoenix, seed_of_creation — plus the reusable authoring kit and starter." · topics:
  soul-land, douluo-dalu, fanfiction
- `the-universal-storyline-creation-` — "Storyline creation and fan fiction — CONTROL CENTRE:
  navigation and state reference for every Soul Land serial, plus the portable authoring law that
  governs them." · topics: soul-land, fanfiction, storyline
- `storyos-site` — description kept (already accurate) · topics: fanfiction, verification, publishing
- `soul_land_4_fire_phoenix` (private) — "Soul Land 4 fan fiction — Fire Phoenix (OC Yan Shuo). Live
  edge: after Chapter 52, Amiable Beasts." · topics: soul-land, douluo-dalu, fanfiction

## Not done / left for the author

- Any rewrite of historical audits and dated archive files (they record what was true when written).
- Regenerating the `storyos-site` published snapshot (needs `$STORYOS_HOME`; it is current as of the
  last measured edge anyway).

*The kit row above is `ba2e939`; the two commits after it are this receipts file itself — see
`git log --oneline -3 -- HOUSEKEEPING_2026-09-21.md`.*

---

## Second pass (same day, after "manage my GitHub perfectly" was repeated)

The second pass went below filenames into *content* — every repo's own validators were run, and
every stale claim found was replaced. Two findings were about work from the first pass itself.

### Correction to the first pass (soul_land_4_fire_phoenix)

The first pass removed `YAN_SHUO_COMPLETE_CURRENT_STATUS_PANEL.md` (and its two twins inside dated
`sync_before` snapshots) as duplicates of `YAN_SHUO_CURRENT_STATUS_PANEL.md`. **That was wrong for
this project.** Its own gate, `tools/perfect_continuation_skill_check.py`, requires BOTH
`YAN_SHUO_CURRENT_STATUS_PANEL.md` and `YAN_SHUO_COMPLETE_CURRENT_STATUS_PANEL.md` to be
byte-exact mirrors of `foundation/STATUS_PANEL.md`; the gate failed, which is how the error was
caught. All three files are restored (commits `a92d466`, `dec226e`) and the gate passes again.
Below, the first pass's entry for that file is superseded by this correction.

### soul_land_4_fire_phoenix (private) — commit `a92d466`

Its verification suite was failing (the mirror above) and its StoryOS layer was stale at the old
edge, still describing the 2026-09-17 rejected branch's Chapter52 as quarantined. Fixed by running
the project's **own** pipeline, not by hand-editing generated files:

- `storyos/scripts/scan_project.py audits . storyos` → `storyos/STORYOS_STATE.json`,
  `storyos/ledgers/CANON_LEDGER.md`, `storyos/ledgers/BRANCH_LEDGER.md` re-scanned: live edge
  Chapter52, Chapter52 accepted (receipts `CHAPTER_52_VALIDATION_2026-09-19.md` /
  `CHAPTER_52_SUPPORT_SYNC_2026-09-19.md`), quarantine now only Chapter53.
- `storyos/scripts/gen_docs.py storyos` → re-rendered `storyos/STATUS_PANEL.md`,
  `storyos/CANON_SOURCE_NUMBERING_MAP.md`, `storyos/NO_MISTAKE_LIVE_RULES.md`.
- `storyos/scripts/build_site.py . storyos/site` → re-rendered `storyos/site/index.html` +
  `STATE.json` (76 KB; its embedded check now reads PASS and NEXT CHAPTER: Chapter53).
- Three files still said "Next fic chapter: Chapter52" while the project's own manifest said 53:
  `README.md` (also gained the missing Chapter52 row in its active-sequence list),
  `foundation/CANON_SOURCE_NUMBERING_MAP.md` (and its support-anchor line moved off Chapter51),
  `foundation/PERFECT_CONTINUATION_SKILL.md` (header said "after Chapter51"). All corrected.
- The scan's rebuilt drift registry was thinner than the file it replaced (it had dropped e.g.
  `Dawnflame 1,120`, `Dawn-Iron 2,040`, `Phoenix God authority` from the registry categories), so
  the registry was unioned — nothing previously listed as banned was lost.

Result: `tools/perfect_continuation_skill_check.py` PASS (mirrors match, 0 stale issues) and
`storyos/tools/storyos_validate.py` PASS (NEXT CHAPTER: Chapter53, source Chapter178 `Collaborate`).

### soul-land-universal-kit — commit "this one"

- **The released kit was missing the author's three newest laws.** `SOUL_LAND_UNIVERSAL_KIT/07_PROSE_LAW.md`
  held §1–§8; §9 HOUSE GRAMMAR, §10 SCOPE LAW and §11 PLAIN LANGUAGE LAW existed only in the
  workspace working copy (`SOUL_LAND_WORKSPACE/kit/07_PROSE_LAW.md`). Ported, with a dated
  provenance note. The working copy's two "zero non-ASCII" statements contradicted
  `tools/verify.py` (which allows portable typography and bans only unreadable scripts — the
  released copy already said so) and were aligned. Kit selftest still PASSES.
- `SOUL_LAND_4_FIRE_PHOENIX_NEXT_STEPS_FOR_CONTINUATION.md` (repo root, unreachable by any project
  validator) still said "after Chapter51" and carried a Chapter52 preparation list, all of which was
  fulfilled on 2026-09-19 — and clauses its own project now classifies as stale. Edge corrected to
  Chapter52, §2's boundary advanced to Chapter178 `Collaborate`, §5 re-headed as historical with
  pointers to the project's status panel and manifest.
- Root `README_ARENA_WORKSPACE.md` was a second, unreferenced README (an earlier front door with a
  stale Chapter-51 claim) → archived to `_archive/2026-09-21_superseded_arena_readme/` with a dated
  supersession note; its bytes unchanged. The main `README.md`'s two remaining "Chapter 51"
  statements were corrected to Chapter 52.

### soul-land-projects — commit `487ddf9`

- `README.md` said twice that the live Fire Phoenix project is at Ch51 → Chapter 52.
- `STATE.md` (dated 2026-09-08, still opening "THE CURRENT PROJECT … blue_silver … Work
  blue_silver" as rule 1) → dated banner added; body kept as history.
- `SOUL_LAND_UNIVERSAL_KIT/07_PROSE_LAW.md` re-synced with the kit repo so the mirror carries the
  three new laws; the two copies are byte-identical again.

### Standing rule added by the second pass

**Run a project's own validators before and after any deletion or edit inside it.** A file that
looks like a duplicate may be required by that project's law. Filename- and byte-level comparisons
are not enough on their own.
