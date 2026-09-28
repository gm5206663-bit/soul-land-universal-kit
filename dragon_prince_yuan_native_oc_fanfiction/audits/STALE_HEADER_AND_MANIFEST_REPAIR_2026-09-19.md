# Stale Header + Missing Manifest Repair — 2026-09-19

Type: repair + machine-readable state authored
Project: Dragon Prince Yuan Native OC (Zhou Xu)
Live edge before and after: **after Chapter 1, `The Second Son in the Green Smoke`** (unchanged)
Canon consumed: novel Chapter 1 `Python and Sparrow Swallow the Dragon` (unchanged)
Files before: 28. Files after: 30 (+`foundation/CURRENT_STATE_MANIFEST.json`, +this receipt).
External gate before: **FAIL** (no machine-readable state; zero firewalls detected)
External gate after: **PASS**, edge Ch1, drift 0, firewalls 1 (`PARTIAL / TBD`)

No prose, lock, character value, firewall rule or canon decision was changed. Nothing was
deleted.

---

## 1. What was wrong

### 1a. No machine-readable current state

The project shipped no `foundation/CURRENT_STATE_MANIFEST.json`. Its live edge existed only in
prose, spread across `foundation/STATUS_PANEL.md`, `codex/CHAPTER_PROGRESS.md` and
`codex/TIMELINE.md`. Consequence: external tooling could not read the edge, could not scan the
project for drift (with no edge number there is nothing to compare claims against), and failed
the project outright.

### 1b. Two stale headers above correct content

Both root entry points carried a pre-prose status line *above* a later-appended, correct
`## Latest live edge after Chapter 1` section. A reader who stopped at the top — which is what
a "START HERE" or "HANDOFF" header is for — got the wrong state.

| File | Stale line | Contradicted by |
|---|---|---|
| `HANDOFF.md` | `Status: foundation initialized, no prose yet.` | `chapters/Chapter_01.md` exists; the same file's own live-edge section |
| `foundation/START_HERE.md` | `Do **not** write Chapter 1 yet. First lock: …` | Chapter 1 exists; the same file's own live-edge section |

This is the same defect class found in Soul Land 4 on the same day: a stale directive sitting
close enough to historical wording that readers and scanners both skip past it.

### 1c. Scanner bug (not this project's fault)

The StoryOS scanner hard-coded 11 Soul Land 4 `foundation/` filenames as the only locations
firewalls could occupy. This project declares its firewalls in
`foundation/KNOWLEDGE_FIREWALLS.md`, so it was reported as having **zero** and failed for it.
Fixed in `storyos-site` commit `686bb38` — discovery is now generic, and a firewall the project
itself marks TBD reports `PARTIAL / TBD` rather than `LOCKED`.

The FAIL was therefore partly a false accusation. Recorded here so the project's history does
not imply it was ever in a worse state than it was.

---

## 2. What was done

### `foundation/CURRENT_STATE_MANIFEST.json` (new, 25 top-level keys)

Every value was taken from this project's own files. A `provenance.derived_from` block names
the source for each field, and `provenance.authority_rule` states that the manifest is an
index, not a source of truth: on conflict the named file wins and the manifest is wrong.

| Field | Source |
|---|---|
| `latest_fic_chapter` 1, `latest_fic_title`, `latest_fic_file` | `codex/CHAPTER_PROGRESS.md` "Live edge: after Chapter 1."; `foundation/STATUS_PANEL.md` |
| `chapter_metrics` (23242 chars / 424 lines / 4140 words / 3794 body words / 0 CJK) | `audits/CHAPTER_01_VALIDATION_2026-09-13.md` Metrics table |
| `canon_consumed_through` ch.1 `Python and Sparrow Swallow the Dragon`, URL, source policy | `canon_coverage/Canon_Coverage_Chapter_01.md` |
| early novel order (1 Python and Sparrow…, 2 Genesis Runes, 3 Su Youwei) | `canon_coverage/Canon_Coverage_Chapter_01.md` line 84 |
| `next_source` ch.2 `Genesis Runes`, `blocking: true` | `foundation/CANON_SOURCE_MAP.md` line 30; `codex/TIMELINE.md` line 10; `codex/CHAPTER_PROGRESS.md` line 8 |
| `current_state`, `current_locks`, `power_boundaries`, `forbidden` | `foundation/STATUS_PANEL.md` |
| `knowledge_firewalls` | `foundation/KNOWLEDGE_FIREWALLS.md` |
| `open_items_requiring_user` | `foundation/KNOWLEDGE_FIREWALLS.md`; `HANDOFF.md` |

**Nothing was invented.** Where the project says TBD, the manifest says TBD:
`exact_cultivation_realm: "TBD — not stated yet, do not invent"`. Chapter 2's source is marked
`NOT FETCHED` and `blocking: true` rather than summarised from memory.

### `HANDOFF.md`

Status line marked **SUPERSEDED**, pointing at the live-edge section, `STATUS_PANEL.md` and the
new manifest. The user-lock list below it is untouched and still valid as the record of what
the project was built on.

### `foundation/START_HERE.md`

The "Absolute startup rule" section is headed **STATUS: COMPLETED — this gate has been
passed**, and the eight-lock checklist is preserved as historical startup discipline and as the
procedure to re-run if the project is ever reset. The source-conflict rule and butterfly rule
are untouched.

No instruction text was deleted in either file, per the standing rule *archive/mark, don't
erase*.

---

## 3. Still open — requires the author, not an agent

1. **Exact cultivation realm for Zhou Xu.** Deliberately unstated. Do not invent it.
2. **Project-specific knowledge firewall boundaries.** `foundation/KNOWLEDGE_FIREWALLS.md`
   still reads "Status: project-specific boundaries TBD" and "TBD after user locks OC
   background and relationship to canon cast." Left exactly as-is: it is an honest unresolved
   placeholder, not a stale claim, and resolving it needs the author.
3. **Wine-quirk exact handling.** `HANDOFF.md` records "exact handling TBD".
4. **Name confirmation.** `HANDOFF.md` records Zhou Xu as assistant-created and changeable.
5. **Chapter 2 is blocked** on fetching and reading novel Chapter 2 `Genesis Runes`, and
   comparing donghua/manhua if they differ. Not fetched, therefore not summarised.

---

## 4. Changed files

```
foundation/CURRENT_STATE_MANIFEST.json                       | new
HANDOFF.md                                                   | header marked superseded
foundation/START_HERE.md                                     | startup gate marked completed
audits/STALE_HEADER_AND_MANIFEST_REPAIR_2026-09-19.md        | new (this file)
```

28 files → 30 (manifest + this receipt). No deletions.
