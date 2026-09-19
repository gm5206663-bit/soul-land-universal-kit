# `_archive/2026-09-19_stale_sl4_copies_at_ch31/` — DO NOT USE

Two superseded top-level copies of the **Soul Land 4 Fire Phoenix** project, archived
2026-09-19. Both stopped at **Chapter 31**; the project's live edge is **after Chapter 51,
`The Cost of Quiet`**.

| Archived from | Now at | Files | Finding |
|---|---|---|---|
| `soul_land_4_fire_phoenix/` | `soul_land_4_fire_phoenix_STALE_ch31/` | 173 | Stale at Ch31. 71 identical / 96 older / 486 missing vs the current tree. |
| `sl4_fire_phoenix/` | `sl4_fire_phoenix_STALE_ch31/` | 172 | Stale at Ch31 **and** a byte-identical duplicate: its nested 168-file tree matched the copy above exactly. Only its 4 loose files were unique. |

Each directory carries its own `README_STALE_ARCHIVED.md` with the detail.

## Method

Moved with `git mv`. **345 renames, all recorded as `R100` — zero deletions, zero content
changes.** Every file is byte-identical to its former top-level version; only the path changed.
History follows the files (`git log --follow`).

## Where the truth lives

- **Authoritative project:** GitHub private repository `gm5206663-bit/soul_land_4_fire_phoenix`
  — 653 files, live edge after Chapter 51.
- **Current copy inside this repo:**
  `arena_managed_uploads/2026-09-18_chapter51_managed_snapshot/soul_land_4_fire_phoenix/`
- **Current next-steps entry point:**
  `SOUL_LAND_4_FIRE_PHOENIX_NEXT_STEPS_FOR_CONTINUATION.md` at this repo's root
- **Five-copies comparison:** `WORKSPACE_MAP_2026-09-19_STORYOS_INDEX.md` at this repo's root

## Remaining SL4 copies after this archive

Five copies became three live-plus-one-snapshot. Still standing:

1. the private repository (authoritative),
2. `arena_managed_uploads/2026-09-18_chapter51_managed_snapshot/…` in this repo (identical
   snapshot, dated),
3. `soul-land-projects` repo → `sl4_fire_phoenix/soul_land_4_fire_phoenix/` — **also stale at
   Chapter 31**, archived separately in that repository on the same date.

Note the standing privacy finding: the `arena_managed_uploads` snapshot mirrors a **private**
repository's 653 files into a **public** one. That was pre-existing and is recorded in
`WORKSPACE_MAP_2026-09-19_STORYOS_INDEX.md`. It was not changed by this archive.
