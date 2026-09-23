# 10 — HANDOFF LAW

How to pass a serial to another agent — or to yourself in a fresh session — without
regressing.

A handoff is the highest-risk moment in a long serial. Every error that was fixed can be
reintroduced by one agent reading one stale file.

---

## 1. THE HANDOFF FILE

One file, at the project root, named `HANDOFF.md`. It is the first thing any new agent reads
and it must answer, in order:

```
1. WHAT THIS IS          — one paragraph. Era, protagonist, premise.
2. THE LIVE EDGE         — the last chapter that counts, by number and title.
3. THE STATUS SOURCE     — which file is authoritative. Name it.
4. THE LOCKS             — the absolutes, verbatim.
5. WHAT IS FORBIDDEN NOW — powers, reveals and events reserved for later.
6. WHAT IS STALE         — superseded drafts, and where the live ones are.
7. OPEN THREADS          — what is unresolved, and what each one needs.
8. WHAT NOT TO RE-LITIGATE — decisions already made, with the reason.
9. VERIFICATION          — the command to run, and what passing looks like.
```

Keep it under 1,500 words. A handoff so long nobody reads it is worse than none.

---

## 2. THE STALE-FILE PROBLEM

This is the specific thing that breaks handoffs.

A project accumulates superseded drafts, abandoned chapters, earlier outlines and mirror
files. They stay readable. They stay plausible. A new agent finds one, believes it, and
reintroduces everything you just fixed.

**Three defences:**

**Stamp them.** See `08_CONTINUITY_LAW.md` §6. An unmistakable banner at the top of every
superseded file.

**Say where the live ones are.** Not just "the old ones are wrong" — name the directory that
is current.

**Run the check first.** Before writing anything, a new agent runs the verification script
over the whole project and reads the output. Expect failures. Fix them before adding.

---

## 3. WHAT A NEW AGENT DOES FIRST

In this order, before drafting anything:

```
1. Read HANDOFF.md
2. Find the single status source. If two files claim to be current, stop and resolve it.
3. Find the live edge. Confirm which chapters count.
4. Run tools/verify.py over everything. Read the output. Fix failures.
5. Read the most recent audits/ record. Do not re-litigate settled decisions.
6. Read the last chapter that counts.
7. Only then plan the next chapter.
```

Skipping to step 7 feels faster. It is much slower.

---

## 4. WHAT TO INCLUDE IN A HANDOFF

**Include:**
- the locks, verbatim — do not paraphrase, paraphrases drift
- the exact verification command and what a pass looks like
- the specific errors already caught, so nobody rediscovers them
- anything the user explicitly ruled on, with the date

**Do not include:**
- a plot summary — the chapters are the plot summary
- world lore — that lives in the codex
- your reasoning process — the audits carry what matters
- anything you are unsure about, unmarked. Mark it `[unverified]` or leave it out.

---

## 5. THE USER'S WORDS ARE THE TOP LAYER

When a user has ruled on something — a name, a canon classification, a thing that must never
happen — record it verbatim with the date.

```
User ruling (2026-09-08): Blue Silver Valley IS canon Soul Land 1.
Never "[design]", never "canon nowhere names it". Do not re-add revoked wording.
```

Paraphrased rulings get re-argued. Verbatim rulings with dates don't.

And when a ruling is **revoked**, record the revocation too, with its own date. Otherwise a
future agent finds the original ruling, believes it, and undoes the correction.

---

## 6. CROSS-PROJECT CONTAMINATION

If you run more than one serial in the same franchise, they will bleed into each other.

Every project needs its own:
- status source
- continuity ledger
- lock file
- numbering

**Numbers never cross.** Protagonist A's rank is not protagonist B's rank. Two serials in
the same world share canon; they share nothing else.

And identify a project from **its own contents** before applying another project's warnings
to it. A file labelled "do not open" in project A may be pointing at a completely different
file in project B. Check the magic bytes, read the header, confirm the franchise — then
decide.

---

## 7. THE HANDOFF AUDIT

Before sending:

```
- Does HANDOFF.md name exactly one status source?
- Does it name the live edge unambiguously?
- Are the locks verbatim rather than paraphrased?
- Is every superseded file stamped?
- Does the verification command actually run, and does it pass?
- Are user rulings recorded with dates?
- Is anything unverified clearly marked?
```

If the verification command does not run in the receiving environment, say so in the
handoff. A gate the next agent cannot execute is a gate that will be skipped.
