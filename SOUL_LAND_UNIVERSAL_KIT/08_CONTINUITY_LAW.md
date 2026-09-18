# 08 — CONTINUITY LAW

The rule that prevents the most expensive class of error.

---

## 1. THE LAW

**Set the panel endpoints for a chapter FIRST. Then write every in-chapter date against
them.**

Never the reverse. Writing dates as prose and reconciling them afterwards is how a finished
serial shipped **seventeen arithmetic errors and one hard canon violation** — the finale
landed 49 years after a canon character had already left the story, which made the ending
impossible as written.

Not one of those errors was hard to fix. All of them were invisible from inside the draft.
That is exactly why the order matters.

---

## 2. THE PROCEDURE

Before drafting any chapter with dates in it:

```
1. Open CONTINUITY.md and read the anchor table.
2. Decide the chapter's start year and end year. Write them in the panel.
3. Check the end year against every canon constraint that bounds this story.
4. Only then write the chapter, deriving every in-chapter date from the endpoints.
5. After drafting, re-derive every date in the prose and check it against the panel.
6. Add the new anchors to the table.
```

Step 3 is the one that saves the serial. In the case above, the constraint was "a canon
character must still be present for the finale," and checking it before drafting instead of
after would have cost one line instead of a five-chapter compression.

---

## 3. THE ANCHOR TABLE

One row per dated event. This is the most valuable single artifact in the kit.

```
| Anchor                     | Year | Chapter | Note |
|----------------------------|------|---------|------|
| First hunting party        |    1 |       1 |      |
| Mantis arrives             |   61 |       3 |      |
| The killing                |   98 |       3 | founds the mercy law |
| Mantis dies                |  104 |       3 | 61 + 43 |
```

Note the last row carries its own arithmetic. Write the derivation into the table and the
error becomes visible the moment you type it.

### The panel contiguity check

Chapter panels must be contiguous — no overlap, no gap. This is machine-checked by
`tools/verify.py` and it catches whole classes of drift, including chapters that were
inserted or reordered without updating their neighbours.

---

## 4. ONE SOURCE OF TRUTH

`STATUS_PANEL.md` is the only file that states current state. Everything else derives.

The moment two files both claim to be current, one is stale and nobody knows which. This is
not hypothetical — it is the failure that produces the long tail of small contradictions
readers find and authors cannot.

**Old numbers get corrected at the source, not whispered around the project.** If the panel
says one thing and a codex file says another, fix the codex file. Do not add a note
explaining the difference. Notes explaining contradictions accumulate until the project has
more reconciliation text than story.

---

## 5. FORWARD REFERENCES

Every "X years later," "she would not learn until," and "in time he would understand" is a
promise. Track them:

```
| Promise                | Made in | Paid off in | Status |
|------------------------|---------|-------------|--------|
| "in forty-seven years" |     15  |  (external) | MATCH  |
```

Two rules:

**Compute them.** "In forty-seven years" from year 753 must land on a year that means
something. In the case above it landed exactly on a canon date — but only after correction.
The first draft said "two hundred and eleven years" and pointed past the end of the series.

**Pay them off or cut them.** An unpaid forward reference is a debt. If the serial ends
before it matures, either it points at something real outside your story, or it should not
have been written.

---

## 6. SUPERSESSION

When a draft is replaced, **stamp the old files**. Do not delete them — they are history and
the receipts still matter — but mark them unmistakably.

```
<!-- ============================================================
     SUPERSEDED — DO NOT USE AS CONTINUITY
     The authoritative continuity is: foundation/CONTINUITY.md
     Live chapters: chapters_rebuilt/
     Dates, ages and character state here are STALE.
     ============================================================ -->
```

**Classify before stamping.** A blanket stamp over files that contain still-binding canon law
destroys valid reference. Sort them:

- **State mirrors** (status panels, timelines, character dossiers) → stamp superseded
- **Mixed law + state** (world bibles, doctrine files) → qualified banner: law binds, state
  rows are stale
- **Pure law** (canon receipts, prose law, research rules) → leave alone

An unstamped stale file is a trap with a five-minute fuse. A future agent will read it,
believe it, and reintroduce every error you just fixed.

---

## 7. THE CONTINUITY AUDIT

Every chapter:

```
- Does every in-chapter date match the panel endpoints?
- Is the panel contiguous with its neighbours (no overlap, no gap)?
- Is every new anchor added to the table?
- Does any date violate a canon constraint?
- Are all forward references computed and tracked?
- Is there exactly one file claiming to state current state?
```
