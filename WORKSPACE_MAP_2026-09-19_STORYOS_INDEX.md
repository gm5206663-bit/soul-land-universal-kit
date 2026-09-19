# WORKSPACE MAP — 2026-09-19 StoryOS index (ADD-ONLY)

Nothing in this repository was deleted or overwritten to produce this file. Two things were
added on this date:

1. `dragon_prince_yuan_native_oc_fanfiction/` — 28 files, the complete project. It existed
   nowhere on GitHub before this commit (verified by content hash against all four repos).
2. `DRAGON_PRINCE_YUAN_FANFICTION_HANDOFF.md` — its handoff pointer.

Plus this index, and a new section appended to `README.md`.

---

## Every fanfiction project in this repository

Chapter counts are files named `chapter*NN*` under the directory. "Current" means verified
against the project's own authoritative manifest by **content hash**, not by date or name.

| Directory | Files | MB | Chapters | Status |
|---|---|---|---|---|
| `Soul_Land_3_Project/` | 399 | 10.58 | 116 | **CURRENT** — Branch 05, Lin Hao. Matches `README.md`. |
| `arena_managed_uploads/2026-09-18_chapter51_managed_snapshot/soul_land_4_fire_phoenix/` | 654 | 6.73 | 51 (+52/53 archived) | **CURRENT for SL4** — 653/653 files byte-identical to the author's own handoff ZIP |
| `soul_land_holy_spirit/` | 28 | 0.30 | 4 | **CURRENT** — edge Chapter 4 "The Use" per `WORKSPACE_MAP_2026-09-19.md` |
| `soul_land_devouring_dragon/` | 32 | 0.40 | 10 | **CURRENT** — edge Chapter 10 per `WORKSPACE_MAP_2026-09-19.md` |
| `blue_silver/` | 61 | 1.19 | 15 | **CURRENT** — `STATE.md` names this the live build |
| `Soul_Land_2_Project/` | 28 | 7.50 | 21 | **CURRENT** — Branch 06, Jiang Che |
| `Soul_Land_5_Project/` | 13 | 0.09 | 0 | **FOUNDATION STAGE** — no chapters yet, by design |
| `dragon_prince_yuan_native_oc_fanfiction/` | 28 | 0.06 | 1 | **NEW (added today)** — gate **FAIL**, see warning below |
| `Miraculous_Project/` | 40 | 0.34 | 4 | separate (non–Soul Land) project |
| `soul_land_new/` | 33 | 0.31 | 6 | superseded — see `SARA.md` §5 post-mortem; `SOUL_LAND_NEW/` is dropped |
| `SOUL_LAND_NEW/` | 25 | 0.44 | 7 | **DROPPED** per `STATE.md` |
| `soul_land_starter/` | 21 | 0.03 | 1 | starter template |
| `SL1_GU_YUAN/` | 6 | 0.03 | — | SL1 handoff material |
| `SL3_LIN_HAO/` | 2 | 0.01 | — | pointer only |
| `CODEX/` | 8 | 0.51 | — | unified codex family + mirrors |
| `SOUL_LAND_UNIVERSAL_KIT/` | 27 | 0.11 | — | kit docs |
| `SOUL_LAND_WORKSPACE/` | 19 | 0.16 | — | `SARA.md` self-file, sessions s18–s21 |
| `reference/` | 300 | 5.86 | 101 | **`reference/sl3_lin_hao/` is FORBIDDEN** per `STATE.md` — do not restore or continue |
| `SL_ARCHIVE/` | 179 | 9.54 | 15 | archive — `sl4_foundation_v1` / `v2` |
| `_archive/` | 51 | 3.10 | 18 | **DO NOT USE** per `README.md` |
| `_perfect_export_2026-09-18/` | 31 | 3.83 | — | export snapshot |
| `uploads/` | 30 | 7.40 | 1 | author upload packs |

---

## 🔴 Soul Land 4 has five copies in this account. Two are twenty chapters stale.

This is the exact failure mode SL3 retired its mirror under — the **TWO-COPIES LAW**:
*"a fact maintained in two places will be wrong in one of them, and the check reads the
other."* SL4 currently has five places.

Verified by git blob SHA (byte-level), against the author's own `workspace HANDOFF` ZIP:

| Copy | Files | Identical | Differ | Missing | Verdict |
|---|---|---|---|---|---|
| `arena_managed_uploads/2026-09-18_chapter51_managed_snapshot/soul_land_4_fire_phoenix/` (this repo) | 654 | **653** | 0 | 0 | ✅ **CURRENT — read this one** |
| `soul_land_4_fire_phoenix` **private repo**, root | 654 | **653** | 0 | 0 | ✅ current duplicate |
| `soul_land_4_fire_phoenix/` (this repo, top level) | 173 | 71 | 96 | 486 | ⛔ **STALE — stops at Chapter 31** |
| `sl4_fire_phoenix/` (this repo, top level) | 172 | 0 | 0 | 653 | ⛔ **STALE — stops at Chapter 31** |
| `soul-land-projects` repo → `sl4_fire_phoenix/soul_land_4_fire_phoenix/` | 168 | 71 | 95 | 487 | ⛔ **STALE** |

The live edge is **after Chapter 51 "The Cost of Quiet"**, canon consumed through source
Chapter 176, next source Chapter 177 `1,000-year Purple Zoysia`. An agent that reads either
top-level `*fire_phoenix*` directory will draft from a state twenty chapters behind, using
superseded power values.

**Not deleted, per the standing rule "never delete user work — archive/mark, don't erase."**
Marked here instead. Recommended next step, for the author to approve: move the three stale
copies under `_archive/` or add a `README_STALE.md` inside each, the way `audits/` folders
already carry `README_OBSOLETE_BACKUP.md`.

### Privacy note the author should see

The `soul_land_4_fire_phoenix` repository is **private**, but the 653-file identical
snapshot inside this **public** repository makes that privacy void. It includes all 51
chapters, `foundation/`, the knowledge firewalls, and
`YAN_SHUOER_BEAUTY_IDENTITY_PRESSURE_LOCK.md`. Nothing was changed here; this is recorded
so the decision is made deliberately.

---

## ⚠️ Dragon Prince Yuan — added, but its gate is FAIL

`dragon_prince_yuan_native_oc_fanfiction/` is complete (28 files: 1 chapter, 4 bible,
11 foundation, 3 codex, 6 audits, 1 coverage). Its own published state says:

```
GATE: FAIL  (errors=1, warnings=1, learned-rules-active=0)
  error: firewall-integrity: No knowledge firewalls in the audited state. Define them.
  warn : next-chapter-consistency: START_HERE.md implies Chapter1 is next, but the live
         edge after Chapter1 makes Chapter2 next. Stale or superseded instruction.
  info : banned-tokens: No unambiguous regression tokens — the drift guard cannot fire.
live edge           : after Chapter1 "The Second Son in the Green Smoke"
next source chapter : None
locks / characters  : 0 / 1     firewalls: none registered
```

Note that `foundation/KNOWLEDGE_FIREWALLS.md` **does** exist in the project — so the
firewall-integrity error looks like a scanner that is not finding a file the author has
already written. Worth checking before drafting.

**Per the project's own rule 1, do not draft prose while the gate is FAIL.**

---

## StoryOS site

The verification and publishing tooling built alongside this index lives in its own
repository: **`gm5206663-bit/storyos-site`** (public).

It reads a project folder and publishes: a reader for the prose, the live gate, character
locks, knowledge firewalls, learned rules, every file with its sha256, and an independent
drift scan. It runs each project's own validator as a subprocess and reports where they
disagree — and why, derived from the validator's own declared scope.

It found 11 stale-live-edge findings across 9 active files in the SL4 project while that
project's own `tools/perfect_continuation_skill_check.py` reports `active_stale_issues=0`.
Three causes, all fixable in `foundation/CURRENT_STATE_MANIFEST.json`:

1. the workspace-root `NEXT_STEPS_FOR_CONTINUATION.md` sits outside every project dir, so no
   per-project scan can see it
2. `canon_coverage/` is not in `active_markdown_dirs`
3. seven files say `Current live edge is after ChapterNN`; the manifest's `Live edge:` regex
   requires a literal colon, and its `Current…after Chapter` regex does not allow the prefix
   `live edge is`

The site stores no secrets in git: `data/.key`, `data/audit.log` and `data/proposals.jsonl`
are gitignored, and the generated `data/` payload is built locally rather than committed —
so it cannot become a sixth stale copy.
