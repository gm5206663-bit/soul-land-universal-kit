# THE CHAPTER SHAPE — the other conventions this account keeps but never checked

**Written 2026-10-30.** Found the same way as the canon line: by measuring what the corpus
already does, not by inventing a rule. Companion to [`CANON_METHOD.md`](CANON_METHOD.md) —
that file is *what source*, this one is *what shape*.

The whole corpus was surveyed (284 chapter files across 16 serials) for the structure a chapter
carries before its prose and after it. Five things turned out to be checkable, and **one of them
was wrong in the published text.** Everything else the survey found is listed in §4 as
*checked and deliberately not enforced*, because "I didn't add a gate" is also a finding.

---

## 1. The five rules

### S1 · the title must be a heading

The first non-empty line of a chapter is `# …`.

**This was broken.** `lan_shen/chapters/Chapter_01_What_the_Master_Said.md` opened with

```
--- # Chapter One: What the Master Said
```

Markdown reads that as a horizontal rule followed by plain text. The title was **not a heading**:
no anchor, no table-of-contents entry, invisible to every tool that looks for `^# `. It had been
that way since the file was written. Fixed on 2026-10-30 by splitting the rule off — the words are
untouched, and the diff is one line moving.

### S2 · the title names a chapter and a title

`# Chapter 12: The Wall` · `# Chapter 12 — The Wall` · `# Chapter 12 - The Wall` · and
`# Chapter One: What the Master Said`.

Both separators are in use across the account and both are fine. The number may be a digit **or
an English word** — `lan_shen` writes `# Chapter One:` and is right to. A bare `# Chapter 12` with
nothing after it does not pass, and neither does a heading with no number at all.

> The first version of this check required digits, and reported **eight correct `lan_shen`
> chapters** as untitled. A false finding is not a small error: it asks someone to fix what is
> already right. Word numerals are now a fixture.

### S3 · a placeholder is not a chapter

`soul_land_new/chapters/Chapter_01.md` contains:

```
# Chapter 1: {Title}

{No content yet. This file is populated only when the author opens the serial. Prose
conventions: see chapters/CHAPTER_TEMPLATE.md and foundation/RAILS.md.}
```

Twenty-four words of unfilled template, sitting beside the **real** `Chapter_01_The_Grass_That_Stayed.md`.
Every measuring tool on the account counted it as a chapter, so the corpus chapter count, the
register, and any "chapters written" claim include a file the author never wrote. That is the
silent inflation the register exists to catch, and the register caught the *words* but not the
*fact*.

It is currently **pinned** as a declared stub rather than deleted, because deleting a file in a
serial is the author's call. One click removes it; the pin is named in
`tools/chapter_shape_baseline.json` so it is visible, not forgotten.

### S4 · the `## Timeline:` line — in the serials that declared it

The sibling of the canon line. **Canon says what source; Timeline says when in-world.**

```markdown
## Timeline: Spring, age 11 — six days on the road.
## Timeline: The two days after the merge — the walk north, the oath
## Timeline: days to months after Awakening Day, age 6 → 7, Glorybound City
```

Two serials keep it on every chapter — `Soul_Land_2_Project` 24 of 24, `soul_land_2_new` 8 of 8.
It had never been written down and never been checked. Now it is declared in `DECLARED` in
`tools/chapter_shape.py`, and from that moment every new chapter in those serials must carry it.

**A convention is declared by the book that keeps it, not imposed by a tool on books that never
did.** `adaptive_prodigy` uses it in 37 of 116 chapters — a habit, not a rule — so it is counted
in `--report` and left alone. Declaring it would have invented a 72-item backlog and told the
author's own serial it was doing something wrong. Adopting it is a decision, not a check.

### S5 · the file is not truncated

The last prose line ends with terminal punctuation. A chapter that stops mid-sentence is a bad
save or a bad edit, and inside a 2,000-line file nobody sees it in review.

Advisory by design, with a pinned backlog, because a deliberately mid-air ending is a legitimate
craft choice — it must be *visible*, not forbidden. The first version of this check flagged
`Soul_Land_2_Project/chapter_01.md`, which ends on a numbered record item (`5. The meeting
happened BEFORE the forest…`). Ordered-list lines are records, not prose; the check was wrong and
was fixed rather than the prose.

---

## 2. State, 2026-10-30

| | result |
|---|---|
| chapter files surveyed | 284 |
| with a real `# ` heading | **284 / 284** (283 before the `lan_shen` fix) |
| with a chapter-and-title | **284 / 284** |
| placeholders counted as chapters | **1** — pinned, author's call |
| `## Timeline:` where declared | 32 / 32 in the two declared serials |
| truncated tails | 0 |

---

## 3. The gate

```
python3 tools/chapter_shape.py --report     # the shape of every chapter, interesting ones only
python3 tools/chapter_shape.py --check      # the gate
python3 tools/chapter_shape.py --freeze     # re-record the pins (shrink only)
python3 tools/chapter_shape.py --selftest   # 13 defect fixtures
```

Wired into `tools/run_all.sh` as **layer 9**. Read-only, like every other layer.

S1, S2 and S3 are **never pinned** — "a heading" and "a real chapter" are not backlog. Only S4 and
S5 may be pinned, and a pin that starts passing fails the build until it is removed.

---

## 4. Checked, and deliberately not enforced

The survey found five more recurring shapes. Each is real. None is a rule. This table is the
reason to believe the ones above were chosen rather than collected.

| shape | how often | why it is not a gate |
|---|---|---|
| `## End of Chapter` marker | 144 chapters, **3 serials only** (adaptive_prodigy, Soul_Land_2_Project, Miraculous) | a serial's own furniture, not the account's. Imposing it on 13 serials that never used it would be authorship |
| `## Part 1:` scene divisions | 83 chapters, mostly `adaptive_prodigy` (75) | a structural choice for long chapters. Short chapters do not need parts, and "does it need parts" is not machine-decidable |
| `◆ STATUS —` block | 8 chapters, `lan_shen` only | one serial, one shape, already self-consistent. Nothing to protect |
| `POV` label in the head | 3 chapters | a label used three times is not a convention, it is an experiment |
| a `---` rule between the header block and the prose | 119 chapters | too weak to be meaningful: it fires on any front-matter and forbids nothing |

The test applied to each: **is it universal, or is it a serial's own furniture?** An account-wide
gate over a convention one serial keeps is not a standard, it is a tax on the others.

---

## 5. What this adds up to

A chapter now has a checkable shape at both ends:

- **what it adapts** — `## Canon Reference:`, named receipt (`CANON_METHOD.md`, layer 8)
- **when it happens** — `## Timeline:`, where the serial declared it (layer 9)
- **that it is a real chapter with a real title** — S1/S2/S3 (layer 9)
- **that it finished** — S5 (layer 9)

Four of those five were already the account's practice. None of them were checked. That is the
pattern worth remembering: **the account's habits are ahead of its gates, and the gap is where
the defects live.**
