# AUDIT — the gate reads the wrong directory, and four published chapters are ungated

**Date:** 2026-10-11 · **Class:** checkers-that-lie + two-copies rot · **Severity:** critical
**Method:** clean clone (no credentials in `.git/config`) · every claim below is measured, not inferred

---

## THE FINDING IN ONE PARAGRAPH

`tools/style_gate.py` reads `chapters/Chapter_*.md`. That directory holds **six** files.
But **ten** chapters are published — `manuscript/` holds ten reader editions and `docs/`
serves ten pages on the live site. **Chapters 07, 08, 09 and 10 are live and have never been
checked by the gate.** Three of the four carry **zero dialogue lines**, which violates a hard
gate the house law calls non-negotiable.

**This is the Blue Silver bug.** The house's own ledger records it, closed, under §N2:

> *"The unified gate classified chapters by the path substring `/chapters/` — so it swept the
> **rejected first draft** and never saw the live Book One... The gate's "failure" was the
> rejected draft correctly failing while the real text went unchecked."*

**Same class. Same shape. Live again, in a different serial, unnoticed.**

---

## THE MEASUREMENTS

| Location | Count | What it is |
|---|---|---|
| `chapters/Chapter_*.md` | **6** | author editions — footers, panels, receipts |
| `manuscript/Chapter_*.md` | **10** | reader editions — footer-free |
| `docs/chapter_*.html` | **10** | **published pages — live on GitHub Pages** |
| `manuscript/FULL.md` | **6** | the combined edition |

The live site's index lists **Chapter 1 through Chapter 10**. Verified by fetching
`https://gm5206663-bit.github.io/soul-land-2-the-grey-wolf/`.

### The gate's read path

```python
# tools/style_gate.py, line 47
paths = sys.argv[1:] or sorted(glob.glob(os.path.join(
    os.path.dirname(__file__), '..', 'chapters', 'Chapter_*.md')))
```

It is hard-scoped to `chapters/`. Nothing in the script ever looks at `manuscript/` or
`docs/`.

### What the four ungated chapters measure

Run directly against `manuscript/`:

| Chapter | Words | avg | max | Dialogue lines | per 1k | Floor (≥3 lines) |
|---|---|---|---|---|---|---|
| Ch 07 The Third Village | 2,406 | 15.1 | 34 | **0** | **0.0** | 🔴 **VIOLATED** |
| Ch 08 Road To Shrek | 2,436 | 15.7 | 60 | **0** | **0.0** | 🔴 **VIOLATED** |
| Ch 09 Shrek City | 2,631 | 16.0 | 48 | 11 | 4.2 | pass |
| Ch 10 The Combat Exam | 2,512 | 18.1 | 47 | **0** | **0.0** | 🔴 **VIOLATED** |

**Three of the four unpublished-to-the-gate chapters break the dialogue floor**, and the
gate prints `ALL HARD CHECKS PASS` while looking at a directory that does not contain them.

---

## WHY IT HAPPENED — the pipeline has a fork

```
chapters/  ──[run_all.py sync_manuscript()]──►  manuscript/  ──[build_site.py]──►  docs/  ──► live site
   6 files                                          10 files                        10 pages
```

`run_all.py` regenerates `manuscript/` **from** `chapters/`. It can only ever produce six
reader editions. Yet `manuscript/` holds ten.

**Therefore chapters 07–10 have no source in `chapters/`.** They exist as reader editions and
as published pages, but the author editions the pipeline expects are absent. The generator
cannot reproduce them.

### The derived-document defect this creates

`manuscript/FULL.md` is generated from `chapters/` and currently holds **6 chapters** while
**10 are published**. That is a derived document disagreeing with its source — the house's own
Two-Copies Law, rule 2: *"nothing that can be derived may be typed"*, and the parser corollary:
*a derived document must be regenerated, not hand-edited.*

### The blast radius of the next `run_all.py`

**Checked, not assumed:**

- `sync_manuscript()` **writes** the six files it generates and **does not delete** the other
  four. So `manuscript/` keeps all ten. **No immediate data loss.**
- `manuscript/FULL.md` **would be rebuilt with six chapters again** — perpetuating the
  stale derived document, silently.
- `build_site.py` globs `manuscript/Chapter_*.md`, so **it would still publish all ten** —
  which means the four ungated chapters would keep shipping, still ungated.

**Net: the bug is stable, self-perpetuating, and invisible.** Nothing in the pipeline
surfaces it. Nothing fails. The site stays green, the gate stays green, and four chapters
stay unchecked.

---

## WHAT WAS VERIFIED, AND HOW

Every claim above was measured. The measurements, in order:

1. **Clean clone** — `git clone` without credentials in the URL. *Then* re-ran everything.
   *(An earlier pass in this session produced two false failures caused by a token sitting in
   `.git/config`. That was the agent's own contamination, not a repo defect, and it was
   disproved before being reported. The clean clone shows the affected selftest at 53/53.)*
2. **File counts** — `find` on each directory.
3. **Live site** — fetched the published index and read the chapter list back.
4. **Gate behaviour** — run against `chapters/` (exit 0) and against the four `manuscript/`
   files (exit 0, with `dlg: 0` printed for three).
5. **Defect injection** — quotes stripped from a chapter to force zero dialogue:
   `style_gate.py` exit **0 before** and **0 after** — the gate does not catch it.
   The same injection against `lan_shen/tools/style_gate.py` gave exit **2 → 1** — that gate
   **does** catch it.
6. **Class sweep** — every repo checked for published-greater-than-gated. **Only this repo
   is affected.** The kit's System Cheat is aligned at 4/4/4; the other repos have no
   manuscript/publish split.

---

## THE TWO DEFECTS, SEPARATED

These are two distinct faults and they need separate rulings. Fixing one does not fix the other.

### Defect A — the gate reads the wrong directory (critical)

The gate checks `chapters/`. The published text lives in `manuscript/` → `docs/`.

**This one is unambiguous, and it is the more serious of the two.** It is the exact class the
house already paid for once and recorded as closed.

### Defect B — the dialogue floor is measured but never enforced (high)

```python
# tools/style_gate.py
dlg = len([l for l in lines if '"' in l])      # line 38 — measured
hard = bool(over or tw or bare)                 # line 40 — dialogue absent
print(... f"dlg:{dlg:3d} ...")                  # line 42 — printed
```

The number is computed and printed, then never consulted. The law calls the floor a hard gate:

> **Hard gate: every chapter carries at least three spoken dialogue lines.**
> — `SOUL_LAND_UNIVERSAL_KIT/07_PROSE_LAW.md` §2

And states why, in terms that describe this serial exactly:

> Gate 4 exists because the dialogue register silently disappears from introspective serials.
> It went missing from seven of fifteen chapters in one rebuild and was only caught by
> counting. **Count it; do not eyeball it.**

**The count exists. The gate ignores it.**

### The correct implementation already exists in the house

`lan_shen/tools/style_gate.py` **enforces** the floor — verified by injection. Its exit codes
are documented in its own header: `0 clean · 1 failures · 2 warnings only`.

So this is not a missing capability. **It is a copy that lost the enforcement.** Two copies of
the script exist, and one is weaker than the other — the same shape as the kit-copy divergence
recorded at §N1.

---

## WHAT WAS NOT DONE, AND WHY

- **No chapter was touched.** Chapters 07–10 are the author's live edge. Whether their
  zero-dialogue form is intended is **the author's ruling, not the agent's.**
- **No gate script was edited.** This repo has no `selftest.py`. Editing a checker that cannot
  be validated against known-bad input is worse than documenting the gap — and the house's own
  rule is *"if you add an eighth gate, add an eighth fixture."* The fixture does not exist here.
- **No directory was reorganised.** Moving files between `chapters/` and `manuscript/` is a
  structural change to a live serial. It needs a ruling, and it needs to be done with the
  source-of-truth order understood — not by an agent guessing which copy is authoritative.

---

## THE RULINGS THIS NEEDS

**Ruling 1 — which directory is authoritative?**
- **(a)** `chapters/` is authoritative and `manuscript/` has drifted → recover the author
  editions for 07–10, or re-derive them
- **(b)** `manuscript/` is authoritative for 07–10 and they were written there deliberately →
  the pipeline's premise is wrong and `run_all.py` must learn a second source
- **(c)** 07–10 are drafts that should not be published → they need pulling from `docs/`, and
  their publication is the more urgent defect

**Ruling 2 — should the gate read what is published?**
Recommended: **yes.** The gate's job is to check what a reader receives. Reading `chapters/`
checks the drafts; reading `manuscript/` checks the shipped text. Ideally both.

**Ruling 3 — the dialogue floor (Defect B).** Enforce, warn, or leave. See
`GATE_GAP_DIALOGUE_2026-10-11.md`.

**Ruling 4 — the four chapters' zero dialogue.** Intended (a hush register) or not? Note the
house's measured practice: hush-chapters run 8–15% dialogue. **Zero is outside the house's own
observed band.**

---

## THE ORDER OF WORK

1. **Rule on Ruling 1 first** — nothing else can be fixed correctly until the authority order
   is settled
2. Then decide whether 07–10 should be published at all
3. Then arm the gate to read the right directory
4. Then run it and see the true failure count, which is currently unknown — **nobody has ever
   gated the shipped text of this serial**
5. Then enforce the dialogue floor, with the chapters in whatever state the author rules

**Do not reorder these.** Fixing the gate before settling the authority order would produce
failures pointing at files whose status is not yet decided.

---

## RECEIPTS

- `tools/style_gate.py` lines 38, 40, 42, 47
- `tools/run_all.py` `sync_manuscript()` — reads `chapters/`
- `tools/build_site.py` line 108 — reads `manuscript/`
- Live site index — fetched 2026-10-11, lists Chapters 1–10
- Injection test — this session, both scripts, results recorded above
- Class sweep — all 15 cloned repos
- `SOUL_LAND_UNIVERSAL_KIT/07_PROSE_LAW.md` §2 (the dialogue floor) · `09_AUDIT_LAW.md` §3
- `MISTAKES_LEDGER_2026-09-23.md` §N2 (the Blue Silver gate-scope bug, recorded as closed)
- `lan_shen/tools/style_gate.py` (the enforcing implementation)

---

*Written 2026-10-11. Add-only: no chapter, tool, law file, or directory was altered.*
*Supersedes in part `GATE_GAP_DIALOGUE_2026-10-11.md`, which is corrected in place.*
