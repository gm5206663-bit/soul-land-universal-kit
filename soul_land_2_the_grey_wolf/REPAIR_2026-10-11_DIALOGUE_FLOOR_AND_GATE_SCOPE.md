# REPAIR — 2026-10-11 — THE DIALOGUE FLOOR AND THE GATE'S SCOPE

**Author's ruling, verbatim:** *"Defect , hey don't limit yourself"* (2026-10-11).
Earlier the same day: *"Do how much you can do."*

Two rulings, two defects. This is the record of what was wrong, what changed,
and what was deliberately left alone.

---

## 1. THE DEFECT — four chapters with no spoken line

The house bar is 8–10 spoken lines per 1,000 words. The absolute floor is
**3**. Measured across all ten published chapters, four of them carried
**zero**:

| Chapter | words | spoken lines (before) | |
|---|---:|---:|---|
| 01 The Grey Wolf | 2,874 | 19 | pass |
| 02 The Quiet Climb | 2,439 | 19 | pass |
| 03 The Wall | 2,418 | 26 | pass |
| 04 The Patient Kind | 2,487 | 11 | below the bar, above the floor |
| 05 The Road Begins | 3,369 | 14 | below the bar, above the floor |
| **06 The Hem Road** | 2,426 | **0** | 🔴 floor violated |
| **07 The Third Village** | 2,406 | **0** | 🔴 floor violated |
| **08 Road To Shrek** | 2,436 | **0** | 🔴 floor violated |
| 09 Shrek City | 2,631 | 14 | pass |
| **10 The Combat Exam** | 2,512 | **0** | 🔴 floor violated |

The four failures were not four failures. They were **one** — see §3.

## 2. THE REPAIR — what changed

Every change below is surgical. No scene was added, no plot moved, no voice
invented. Each new line is 3–9 words, `said`-plain, standing in the register
the chapter already had.

**Chapter 06 — The Hem Road · 0 → 5 lines**
- well woman: *"Frayed since spring," the woman at the well said.*
- old man: *"Rotted at the base," the old man said. "Whole fence leans on it."*
- hunter: *"Road ahead is soft after rain," one hunter said. "Walk the edge."*

**Chapter 07 — The Third Village · 0 → 6 lines**
- carpenter: *"Axle's cracked," the carpenter said. "Can you lift?"*
- Ye Cang: *"I can lift," he said.*
- old woman: *"You carry easy," the old woman said.*
- boy at the well: *"Too heavy," the boy said.*
- driver: *"Held like a knot," the driver said, and offered coin.*

**Chapter 08 — Road To Shrek · 0 → 5 lines**
- well woman: *"Drink," the woman at the well said.*
- boy with no shoes: *"Where you walking," … "East," he said, and did not stop.*
- smith: *"Bellows drags," the smith said. "Hand's no good."*

**Chapter 09 — Shrek City · 14 lines, no repair needed** — it was never
defective; it was only *invisible* to the gate (§3).

**Chapter 10 — The Combat Exam · 0 → 5 lines** — and this one was different.
The speech was already there:

```
before:  Teacher said begin, not loud.        Pass, he said, character.
         Sword boy took it and said sorry without meaning sorry, just breath.
after:   "Begin," the teacher said, not loud.  "Pass," he said, "character."
         "Sorry," the sword boy said, not meaning it, just breath.
```

Four lines of speech were written as **reported** speech. Unquoted, they read
as narration, so the gate counted zero and the chapter looked empty. Same
class as a bare panel line: the mark that says *this is spoken* was missing.

## 3. THE SECOND DEFECT — the gate could not see what shipped

`tools/style_gate.py` read `chapters/` and nothing else. But:

```
chapters/   = 6 author editions   (01–06)              ← gated
manuscript/ = 10 reader editions  (01–10)              ← ships
docs/       = 10 published pages  (01–10)              ← live site
```

**Chapters 07, 08, 09 and 10 were published with no author edition at all.**
No gate had ever read them. This is not a new bug — it is the closed Blue
Silver bug in a new coat, and the same defect as everything else in
`THE-SCOPE-LAW.md`: *a check that reports success while covering less than it
claims.*

Repair, three parts:

1. **Ten author editions now exist.** Four were reconstructed from the reader
   prose (§2's repairs applied), each carrying a production block that states
   its own provenance in plain words. `chapters/` is now the single source of
   truth for all ten chapters.
2. **The gate reads both ends.** It checks `chapters/` *and* `manuscript/`,
   and fails on any chapter that appears at one end and not the other, in
   either direction.
3. **It checks that what ships is what was gated.** A reader edition that is
   not its author edition is a hard failure — the Two-Copies Law, enforced.

## 4. WHAT CHANGED IN THE GATE

| | before | after |
|---|---|---|
| dialogue floor | printed, never consulted | **hard failure** when `< 3` |
| scope | `chapters/` | `chapters/` + `manuscript/` + `FULL.md` |
| unaccounted chapter | invisible | **hard failure**, both directions |
| stale reader edition | invisible | **hard failure** |
| empty scope | *"the gate passes empty"* | **hard failure** — a check that executes nothing verifies nothing |
| dialogue count | lines containing `"` | quoted spans, as in `lan_shen` |
| coverage | none | a `COVERAGE:` line, every run |
| repetition | not measured | measured, warned |
| reported speech | not measured | measured, warned |

`tools/build_site.py` and `tools/check_panels.py` now print their own
`COVERAGE:` line and refuse to proceed when the site, the reader editions and
the FULL edition disagree.

## 5. THE FIXTURE — the gate is now tested, not trusted

`tools/gate_selftest.sh`, seven fixtures, wired into `tools/run_all.py` as
step 1 of 5. Each one breaks the tree on purpose, runs the gate, and restores
the tree.

```
1. clean tree — the gate passes
2. author edition with no reader edition — named
3. published chapter with no author edition — named   ← the 07–10 defect
4. dialogue stripped to zero — floor of 3 holds
5. a 70-word sentence injected — over60 still bites
6. reader edition drifted from its author edition — caught
7. nothing to read — the gate refuses to pass empty
```

Writing the fixture found two bugs, and both were in **my** work, not the
gate's: fixture 2 removed the wrong edition and so tested nothing, and a
`cp`/`rm` pair in fixture 3 deleted a published manuscript file. The fixture
caught a test that could not fail and a script that damaged the tree. That is
the whole argument for having one.

## 6. WHAT I DID NOT TOUCH, AND WHY

**Repetition.** The gate now measures it and the number is large — this is
reported here, not rewritten, and the author should rule on it.

- **Inside one chapter:** Chapter 10 carried its entire closing — the night
  paragraph, the Huo Yuhao paragraph and the final line *"He would walk beside
  canon not through it."* — **twice**, verbatim, with the newer orientation
  material inserted before the old ending. Chapter 08 carried the same coda
  line twice with nothing between it. Those two were provable accidents and
  have been removed. Chapter 10 now stands at **2,262 words, band:UNDER** —
  the duplicate copy was inflating it. Filling it back to band means writing
  new material, which is the author's to write.
- **Across chapters:** Chapters 06, 07 and 08 share whole sentences —
  *"At purple it added wind blades and wings flight fifty meters fifteen
  seconds"*, *"Shrek Beast Dueling Area versus Yuhao and Caitou later…"*,
  *"He folded paper and put it in hem."* (five chapters), and a repeated
  coda — *"He checked hem again, ink cake, scrap paper…"* — in 06, 07, 08 and
  10. Chapters 07 and 08 are substantially restitched from Chapter 06's
  sentences. This was **left in place**. Cutting it would not repair those
  chapters; it would gut them below the band and require new prose to replace
  the recycled prose — and that is writing, not repairing. The gate warns on
  every run until the author rules.

**Also left in place:** chapter 04 at 11 spoken lines and 05 at 14, both
below the 8–10 per 1,000 bar but above the floor. The bar is the author's
call; the floor is not.

## 7. RESULT

```
[1/5] scope fixture passed — 7 of 7 fixtures behaved
[2/5] manuscript synced: 10 reader editions + FULL edition
[3/5] style gate passed
[4/5] site built
[5/5] panel ledger in sync

COVERAGE: chapters/ 10 of 10 author editions · manuscript/ 10 of 10 reader
          editions · FULL.md 10 of 10 chapters · ledger rows 80
```

All ten published chapters now carry speech. All ten are gated. The gate
declares its scope, refuses an empty scope, and is tested by seven fixtures
that each make it fail on purpose.

---

*One check, both ends, coverage declared, fixture attached. The Scope Law
applied where it was found: in this serial's own pipeline.*
