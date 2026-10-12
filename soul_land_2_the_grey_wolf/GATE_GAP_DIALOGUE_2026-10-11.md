# GATE GAP — the dialogue floor is measured but not enforced

> ## ⚠ CORRECTION — added later the same day (2026-10-11)
>
> **This record is superseded in part. Do not read it alone.**
>
> It says *"Ch 06 is the author's live edge"*. **That was wrong.** The author editions in
> `chapters/` end at 06, but `manuscript/` holds ten, and `docs/` publishes ten — the live
> edge is **Chapter 10**.
>
> The dialogue gap described below is real, but **it is the smaller half of the problem.**
> The larger finding is that **the gate reads the wrong directory entirely**, so four
> published chapters have never been checked at all.
>
> See **`AUDIT_2026-10-11_GATE_SCOPE_AND_LIVE_EDGE.md`** for the full finding.
>
> **Cause of this error:** the live edge was read from the profile README (which says *Ch6
> The Hem Road*) and from `chapters/`, instead of from what is actually published. This is
> the house's own *five mis-measurements* — searching where the thing is expected instead of
> where it is served. The reading was of a fact that is true about `chapters/` and false
> about the repo.


**Date:** 2026-10-11 · **Class:** checkers-that-lie · **Severity:** high (affects what the CI badge means)

---

## What was found

While wiring CI for this serial, the style gate was run and checked against the
house law it claims to enforce. It reports **`ALL HARD CHECKS PASS`**.

That statement is narrower than it reads.

### The gate's actual pass/fail condition

`tools/style_gate.py`, line 40:

```python
hard = bool(over or tw or bare)
```

The gate fails only on three things:

| Variable | What it catches |
|---|---|
| `over` | sentences over 60 words |
| `tw` | "the way" tics |
| `bare` | `「...」` panel lines left in prose |

### What the gate does NOT enforce

`09_AUDIT_LAW.md` lists **seven hard gates**. This script enforces **two of them**
(gate 1 in part — via the bare-panel check — and none of the others):

| Law's hard gate | Enforced here? |
|---|---|
| 1 · no unreadable script | no |
| 2 · no literal escape sequences | no |
| 3 · zero digits in prose | no |
| **4 · at least three spoken dialogue lines** | **measured and printed, but NOT part of `hard`** |
| 5 · panels contiguous | no — separate script (`check_panels.py`), which does pass |
| 6 · no placeholder text in shipped files | no |
| 7 · `◆` marker discipline | partially (the `bare` check) |

**The dialogue floor is the registered gap.** Line 38 computes `dlg` and line 42
prints it per chapter — the number is right there in the output — but line 40
never consults it. **The gate reports the measurement and then ignores it.**

---

## Why this matters

The house's own law states gate 4 is a hard gate:

> **Hard gate: every chapter carries at least three spoken dialogue lines.**
> — `SOUL_LAND_UNIVERSAL_KIT/07_PROSE_LAW.md` §2

and:

> Gate 4 exists because the dialogue register silently disappears from
> introspective serials. It went missing from **seven of fifteen chapters** in one
> rebuild and was only caught by counting. **Count it; do not eyeball it.**
> — `SOUL_LAND_UNIVERSAL_KIT/09_AUDIT_LAW.md` §3

**The exact failure the law was written to prevent is live in this serial.**

### The measurement

| Chapter | Words | Dialogue lines | per 1k | House bar |
|---|---|---|---|---|
| Ch 01 The Grey Wolf | 2,875 | 10 | 3.5 | ≥ 8–10 |
| Ch 02 The Quiet Climb | 2,440 | 15 | 6.1 | ≥ 8–10 |
| Ch 03 The Wall | 2,419 | 18 | 7.4 | ≥ 8–10 |
| Ch 04 The Patient Kind | 2,488 | 7 | 2.8 | ≥ 8–10 |
| Ch 05 The Road Begins | 3,370 | 9 | 2.7 | ≥ 8–10 |
| **Ch 06 The Hem Road** | **2,427** | **0** | **0.0** | **≥ 3 lines minimum** |

**Chapter 06 contains zero dialogue.** Verified independently: zero straight
double-quotes, zero curly quotes U+201C/U+201D, and no speech-like construction —
the chapter is written entirely in indirect report and summary
(*"father had said hem, and north"*, *"Village knows when not to ask"*).

Every other chapter is also below the house dialogue bar of 8–10 lines per
1,000 words. Ch 06 is the only one that breaks the absolute floor of three lines.

**This is not a checker bug.** The gate counts correctly; the chapter genuinely
has none. The gate simply does not act on the count.

---

## What was and was not done

**Done.** The gate script was **not modified**. Editing the author's checker
requires the author's ruling, and this serial has no `selftest.py` to validate a
checker edit against — so a change could not have been verified to house
standard. Per the Honesty Rule (*"if the real check is blocked, unblocking it is
part of the task"*), this record exists instead of a silent edit.

**Done.** The CI badge is scoped honestly. The workflow added at
`.github/workflows/style-gate.yml` carries a header stating plainly which checks
it does and does not enforce, so a green tick is not read as "all seven gates
satisfied."

**Not done.** Chapters were not touched. Ch 06 is the author's live edge and its
form — 0 panel lines, daily-life register — is a deliberate author choice
recorded in F22. Whether it should also carry zero dialogue is **the author's
ruling, not the agent's.**

---

## The two rulings this needs

### Ruling 1 — the gate

Should `tools/style_gate.py` enforce the dialogue floor?

- **(a) Enforce it.** Add `dlg < 3` to the `hard` condition. Honest, and the CI
  badge would then mean what the law says. **Cost:** the gate goes red on Ch 06
  immediately — and on nothing else.
- **(b) Enforce as a warning.** Print a loud `DIALOGUE FLOOR` line per offending
  chapter without changing the exit code. The CI stays green; the gap becomes
  visible in the log on every run.
- **(c) Leave the gate as-is.** Accept that this gate polices three things and
  the other four are audited by hand.

**Recommendation:** (a), **after** Ch 06 is ruled on — so the badge turns red for
one night and green again when the chapter is settled, rather than being red for
months and ignored. *(A gate that cries wolf is worse than no check.)*

### Ruling 2 — Chapter 06

Is the zero-dialogue hem-road chapter intended?

- **If intended:** the law needs an explicit exception recorded — for example a
  *"hush chapter"* class, which the house already recognises
  (the measured corpus shows hush-chapters running 8–15% dialogue versus 44–66%
  for lesson chapters — so the house's own practice allows a low-dialogue
  register, but never zero).
- **If not intended:** Ch 06 gains its three lines and the gate can be armed
  strictly with no exception.

**Note on the second reading:** the surrounding chapters sit at 2.7–7.4 lines per
1,000 against a bar of 8–10. If the author's intent is a deliberately quiet,
hem-road register for this arc, then **the bar and the arc disagree** — and that
is worth one ruling rather than six chapter rewrites.

---

## Blast radius

**Checked, not assumed:**

- `check_panels.py` — **passes.** The 0-panel Ch 06 is lawful under F22 and the
  ledger reports 80 rows in sync
- `run_all.py` — **passes** end-to-end
- The kit's equivalent gate, `soul_land_system_cheat/tools/style_gate.py` —
  **same gap, but no chapter below the floor.** Its four chapters run 15, 16, 26
  and 15 dialogue lines. Arming the kit's CI will not surface this
- No other serial's chapters were measured in this pass

**Sweep status:** the gap exists in **both** copies of `style_gate.py`
(Grey Wolf and the kit). If the author rules (a) or (b), **both must be changed
and both re-run** — fixing one instance and not the class is the documented
mistake this house keeps paying for.

---

## Receipts

- `tools/style_gate.py` lines 38, 40, 42
- `SOUL_LAND_UNIVERSAL_KIT/07_PROSE_LAW.md` §2 (the dialogue floor)
- `SOUL_LAND_UNIVERSAL_KIT/09_AUDIT_LAW.md` §3 (gate 4 and its stated purpose)
- `.github/workflows/style-gate.yml` (armed 2026-10-11, header documents the gap)
- Chapter measurements: this record, run 2026-10-11

---

*Written 2026-10-11. Add-only: no chapter, tool, or law file was altered.*
