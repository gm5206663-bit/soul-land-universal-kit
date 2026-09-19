# ⛔ SUPERSEDED — DO NOT READ AS CURRENT

**Archived 2026-09-19.** Moved here by `git mv` from the repository top level
(`sl4_fire_phoenix/`). Nothing was deleted and no file content was changed — all 172 files
are byte-identical to what they were at the top level.

## Why this is archived

Two independent reasons.

**1. Stale.** The nested project tree stops at **Chapter 31**. The project's real live edge is
**after Chapter 51, `The Cost of Quiet`**.

**2. Duplicate.** The nested tree `soul_land_4_fire_phoenix/` (168 files) was verified by git
blob SHA on 2026-09-19 to be a **strict byte-identical subset** of the sibling archived copy at
`../soul_land_4_fire_phoenix_STALE_ch31/` (173 files). Every one of the 168 matched exactly;
zero differed; the sibling simply has 5 more files. This directory therefore held no unique
project content at all — only the 4 loose files listed below were unique to it.

This is SL3's **TWO-COPIES LAW** applying to SL4: *a fact maintained in two places will be
wrong in one of them, and the check reads the other.*

## The 4 loose files (the only unique content in this directory)

| File | Bytes | Status |
|---|---|---|
| `SOUL_LAND_4_FIRE_PHOENIX_NEXT_STEPS_FOR_CONTINUATION.md` | 2125 | **⚠️ Actively dangerous, not merely old.** See below. Left byte-identical (blob `2d4dcc1f`) as the historical record. |
| `actual_output_hits.txt` | 7591 | Scan output from an earlier session. Tool artefact, not project content. |
| `marker_hits.txt` | 16582 | Scan output from an earlier session. Tool artefact, not project content. |
| `marker_hits2.txt` | 2784 | Scan output from an earlier session. Tool artefact, not project content. |

### Why that `NEXT_STEPS` file is dangerous

Its title is *Next Steps for Soul Land 4 Fire Phoenix Continuation* and it opens
`Live edge: after Chapter31 (`chapters/Chapter_31.md` — `The Ticket Owed to Fire`)`. Twenty
chapters behind the real edge.

Worse, it presents as **current** two values that `foundation/STATUS_PANEL.md` section 9
("Not current / forbidden") explicitly bans from ever being restated as achieved:

- `Dawnflame Kite … **1,120 years / newborn purple-tier**` — section 9 bans `Dawnflame 960 or 1,120`.
- `Dawn-Iron Phoenix Roc rose from 1,680 to **2,040 years**` — section 9 bans `Dawn-Iron 2,480 or 2,040`.

It also asserts `Yan Shuo'er … remains Rank23/SP156` (true value at the current edge:
Rank39/SP962), `No third ring/soul spirit yet`, `no Level30`, `no Purple Flame Eidolon Bird
yet`, and `no full Fire Phoenix/Ultimate Fire/full wings/true flight` — every one of which has
since happened. It points at a dead sandbox path, `/home/user/soul_land_4_fire_phoenix/`, as
the "Active project".

An agent that found this file at the repository top level and trusted its title would have
regressed the project by twenty chapters and re-committed two explicitly banned values. That
is the concrete harm the TWO-COPIES LAW predicts, and the reason for this archive.

Note there is a **second, unrelated** file with the same basename: the workspace-root copy
that carried the Chapter35 edge. That one was rebuilt to Chapter 51 and now lives at this
repository's root. The two are different documents that happen to share a filename.

## Where the truth lives

| What | Where |
|---|---|
| **Authoritative project** | GitHub private repository `gm5206663-bit/soul_land_4_fire_phoenix` (653 files, live edge after Chapter 51) |
| Current copy inside *this* repo | `arena_managed_uploads/2026-09-18_chapter51_managed_snapshot/soul_land_4_fire_phoenix/` |
| **Current next-steps file** | `SOUL_LAND_4_FIRE_PHOENIX_NEXT_STEPS_FOR_CONTINUATION.md` at this repo's root |
| Current state panel | that tree's `foundation/STATUS_PANEL.md` |
| Five-copies comparison | `WORKSPACE_MAP_2026-09-19_STORYOS_INDEX.md` at this repo's root |

## Do not

- Do not read any file here as current state.
- Do not use the `NEXT_STEPS` file in this directory. Use the root one.
- Do not copy values, ranks, spirit-power figures, soul-spirit ages, or the live edge from here.
- Do not delete this directory. It is kept for provenance only.
