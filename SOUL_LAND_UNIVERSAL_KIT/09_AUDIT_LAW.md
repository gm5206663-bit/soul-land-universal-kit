# 09 — AUDIT LAW

The audit loop and the hard gates. This is the file that turns the rest of the kit from
advice into a process.

---

## 1. THE PRINCIPLE

**A chapter is not done when it reads well. It is done when it has been checked.**

And a check that executes nothing verifies nothing. If you cannot name the specific function,
passage or code path that the check actually touched, you have not checked anything — you
have re-read your own draft and felt reassured.

A clean exit code is not a pass when the output is wrong. Read the output.

---

## 2. THE FIVE AUDITS

Run all five on every chapter, in this order. Repair at the smallest possible area,
preserve established material, then record the new state.

### Canon audit
Location, timeline, characters present, knowledge, power levels, regional behaviour.
Ask: **what changed *because of our divergence*?** Anything not deliberately changed remains
canon. An accidental change is a bug, not a liberty.

### Continuity audit
Ages, dates, injuries, promises, relationships, impossible travel, resources.
Cross-check every number against `CONTINUITY.md`. See `08_CONTINUITY_LAW.md`.

### Character audit
Does the voice, the values and the decision-making still belong to this person?
Change must be earned. A character who acts differently in chapter 14 than chapter 4 needs a
visible reason, or one of the two chapters is wrong.

### Power audit
Did strength come from an established cause? What counters remain? Does the world react to
what just became public? Has a reserved power been granted early?

### Tension audit
What can be lost? Who can fail? What stays unknown? Why isn't this easy?
If all four answers are "nothing," the chapter has no stakes and should not ship.

---

## 3. THE HARD GATES

Machine-checked by `tools/verify.py`. These are not negotiable, and "mostly passing" is a
failure.

```
1. Zero characters in an unreadable script (CJK, kana, hangul) — not a blanket non-ASCII ban
2. Zero literal backslash-n sequences
3. Zero digits in prose (panels and ledgers exempt)
4. At least three spoken dialogue lines per chapter
5. Chapter panels contiguous — no overlap, no gap
6. No template or placeholder text left in a shipped file
7. The `◆` marker never appears in prose; at most one book-end card, opening
   with `END OF`, last in the file
```

Gate 4 exists because the dialogue register silently disappears from introspective serials.
It went missing from seven of fifteen chapters in one rebuild and was only caught by
counting. Count it; do not eyeball it.

Gate 5 exists because chapter insertion and reordering desynchronise panels, and the drift
is invisible until two chapters claim the same year.

### Gate scope — which gates apply to which files

Getting this wrong produces a wall of false positives that trains everyone to ignore the
gate. This was learned three separate times while building this kit.

| Gate | Chapters | Templates | Law files | Codex / ledgers | Audit logs |
|---|---|---|---|---|---|
| 1 unreadable script | yes | yes | yes | yes | yes |
| 2 backslash-n | yes | yes | yes | yes | yes |
| 3 digits in prose | yes | — | — | no (ledgers hold figures) | no |
| 4 dialogue | yes | — | — | — | — |
| 5 contiguity | yes | — | — | — | — |
| 6 placeholders | **yes** | **NO** | **NO** | yes | **NO** |
| 7 marker discipline | yes | no | no | — | — |

**Gate 6 must never be applied to templates, law files, or audit logs.** A template with no
slot tokens is not a template, a law file that cannot show the panel format cannot teach it,
and an audit log *reports on* placeholder counts — a line reading `TODO/FIXME/TBD = 0` is
the log doing its job, not a leftover.

**Gates 1 and 2 are the only ones that apply everywhere.** They are the ones that indicate a
file is broken rather than a file being what it is.

### The self-referential false positive

Four times while building this kit, a gate fired on the text that *described* the gate:

1. A blanket non-ASCII gate flagged the em dashes in the prose law that explained the rule.
2. A case-insensitive placeholder match flagged the word "placeholder" in a sentence saying
   "no placeholder text left."
3. Gate 6 applied to `templates/` flagged every slot token in every template.
4. Gate 6 applied to an audit log flagged `TODO/FIXME/TBD = 0` — the log reporting that it
   had found none.

The general rule: **a check must not match its own description.** If a gate fires on the
documentation of the gate, the gate is scoped wrong — not the documentation. Fix the scope,
because "just reword the docs" leaves the trap armed for the next file.

---

## 3b. TESTING THE GATE ITSELF

```
python3 tools/selftest.py
```

**Run this after every edit to `verify.py`.** It builds throwaway chapters, each carrying
exactly one known defect, and confirms every one is caught — then builds a clean chapter and
confirms it passes.

Why this is not optional: `verify.py` was once run against a proven 33,000-word serial and
reported 15 failures. All 15 were false positives from an over-broad rule. The serial was
correct and the gate was wrong, and nothing revealed that except a hand-built negative test.
A gate that has only ever been seen to pass is a gate nobody has tested.

The self-test covers all seven gates plus panel overlap and panel gap. It was itself
mutation-tested: each gate was deliberately disabled in a copy of the kit, and the self-test
failed every time. A self-test that cannot fail is decoration.

**If you add an eighth gate, add an eighth fixture.** A gate with no fixture is a gate you
are hoping works.

---

## 4. THE VERIFICATION PATTERN

The one that works, and the one that doesn't:

```python
# WRONG (1) — the panel is not at file start; the title precedes it.
prose = re.sub(r'^```.*?```', '', s, flags=re.S)

# WRONG (2) — this one looks right and is not. Joining everything after the first
# fence reclassifies any LATER fenced block (a book-end card) as prose, so the
# marker gate and the digits gate both fire on apparatus they should ignore.
parts = s.split('```')
prose = ''.join(parts[2:])

# RIGHT — every fenced block is apparatus. Prose is only what sits outside all of
# them: the even indices past the first fence.
parts = s.split('```')
panel = parts[1] if len(parts) >= 3 else ''
prose = ''.join(parts[i] for i in range(2, len(parts), 2))
extra = [parts[i] for i in range(3, len(parts), 2)]   # book-end cards etc.
```

The second wrong version is the dangerous one. It passes every test you think to write
until the day a chapter grows a second fenced block, and then it produces failures that
look like real defects in the prose. Both bugs were found in this kit's own gate, on
prose that was correct.

That single distinction is the difference between a gate that catches digits in prose and a
gate that quietly passes everything. A verification script with a bug in it is worse than no
script, because it produces false confidence.

Also: express the backslash-n check as `chr(92) + 'n'`. Writing the literal sequence in a
rule about the literal sequence is how the artifact keeps reappearing.

---

## 5. THE HONESTY RULE

If the real check is blocked, unblocking it is part of the task.

Install the missing dependency. Look past a bare `command -v` — the tool is often present
but not on PATH. Prefer the project's own runner over a script you write yourself.

If it genuinely cannot be run, **say so plainly in the same breath as the change**: what you
did, what you could not check, and why. That is an acceptable outcome and it costs nothing.

Presenting an unverified change as done is the failure to avoid. A guess written in the same
voice as a verified fact is how you end up being wrong twice.

---

## 6. WHEN THE AUDIT FINDS SOMETHING

Fix it, then run the audit again. Not "note it and move on."

And check the blast radius. One wrong date usually means the arithmetic around it is wrong
too — the case that produced seventeen errors had a mantis living 43 years in one line and
being alive 37 years later in another, and fixing the first line without the second just
moved the contradiction.

When a class of error appears, sweep for the whole class. Do not fix the instance you
happened to notice.

---

## 7. RECORD THE AUDIT

Every non-trivial audit gets a dated record in `audits/`:

```
audits/2026-09-18_TIMELINE_COMPRESSION.md
```

What it contains: what was found, what was wrong, what was changed, what was verified
afterward, and what remains open.

This is how a project survives a handoff. An agent who can read what was already caught does
not re-litigate it. See `10_HANDOFF_LAW.md`.
