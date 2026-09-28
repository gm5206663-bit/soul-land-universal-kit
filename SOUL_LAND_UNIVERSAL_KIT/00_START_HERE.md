# 00 — START HERE

Read this first. It takes fifteen minutes and it tells you what to decide before you write
anything.

---

## THE ORDER

```
1. This file                    — what to decide, what to read
2. 01_CANON_SPINE.md            — the world. Read fully. You will get mechanics wrong otherwise.
3. 03_STORY_LAW.md              — the five failures. Read fully. This is the expensive lesson.
4. 02_PROJECT_SETUP.md          — set your twelve locks. Do this BEFORE drafting.
5. templates/                   — copy into your project, fill in STATUS_PANEL and CONTINUITY
6. Write chapter 1
7. Run tools/verify.py          — before you call it done, every time
```

The rest (04–10) are reference. Read them when you hit the thing they govern.

**Before you trust the gate, prove it works.** Run `python3 tools/selftest.py` once when you
set the project up. It feeds the gate chapters containing known defects and confirms every
one is caught. A gate that has only ever been seen to pass is a gate nobody has tested — and
this kit's gate was once wrong in exactly that way, failing a correct serial fifteen times.
Re-run it after any edit you make to `verify.py`.

---

## THE FIVE DECISIONS YOU CANNOT DEFER

Every one of these, left undecided, produces drift that costs a rebuild later. Decide them
now, write them into your `NO_MISTAKE_LIVE_RULES.md`, and treat them as locked.

### 1. Which era?

Soul Land spans five series and roughly ten thousand years. Pick one and stay in it.

- **SL1** — Tang San's generation. The best-documented. Highest collision risk with canon.
- **SL2** — the Unrivaled Tang Sect era, ten thousand years later.
- **SL3** — the Legend of the Dragon King era.
- **SL4** — Lan Xuanyu's generation.
- **Pre-canon** — anywhere before SL1. Most freedom, least documentation, and the trap is
  that freedom reads as licence. Blue Silver was pre-canon and still needed every lock.

### 2. Who is your protagonist, and what are they not?

Write down what your OC is **not** as carefully as what they are. The single most common
failure is an OC who quietly acquires a bloodline, a system, a past life, or a canon
character's private mechanic. Decide the ceiling now.

If your OC has a public identity and a private one, decide which is which and what the
reveal costs. If you don't, the reveal will happen by accident in chapter forty.

### 3. Where does your story touch canon?

Name the canon events your serial will actually reach. Not "the world" — specific beats.
If you cannot name five, your story is not set in Soul Land, it is set next to it.

### 4. What is the spine — who is hunting your protagonist?

This is the question that killed a 90,000-word serial. See `03_STORY_LAW.md` §2.

A serial with no opposition is not a plot, no matter how beautiful the prose is. Before you
draft, write one sentence: **"______ wants ______ from my protagonist, and will ______ to
get it."** If you cannot fill all three blanks, stop and fix that first.

### 5. What will you never do?

Every project needs a short list of absolutes. Ours have included: the protagonist never
kills; no identity reveal without approval; a canon character's fate is never rerouted;
power is never reduced to protect an outline. Yours will differ. Write them down before you
need them, because the moment you need them is the moment you'll be tempted.

---

## THE PRE-CHAPTER GATE

Before drafting **any** chapter, answer these. Out loud, in the plan, not in your head.

```
1. What canon beat does this chapter touch, and how does it stay true?
2. What is the threat in this chapter? (Not "tension" — a thing that can hurt someone.)
3. Who opposes the protagonist, and do they have a face and a name?
4. What moves? (Rank, ring, skill, relationship, resource, knowledge — pick one, name it.)
5. What is the turn at the end? (What is different that was not different at the start?)
6. Which registers will this chapter use? (Need ≥3 — see 07_PROSE_LAW.md.)
7. What are the panel endpoints for this chapter? (Set them BEFORE writing dates.)
```

Question 7 is the one everyone skips and it is the one that caused **seventeen arithmetic
errors and one hard canon violation** in a single serial. See `08_CONTINUITY_LAW.md`.

---

## WHAT "DONE" MEANS

A chapter is not done when it reads well. It is done when:

- `tools/verify.py` passes on it — zero failures, not "mostly passing."
- The status panel and continuity ledger are updated to match.
- The audit loop in `09_AUDIT_LAW.md` has been run: canon, continuity, character, power,
  tension.
- You can name the function or code path the verification actually executed.

That last line is not a formality. A check that executes nothing verifies nothing. If you
cannot say which part of the chapter the gate actually touched, you have not checked it.

---

## IF YOU INHERIT AN EXISTING PROJECT

Read `10_HANDOFF_LAW.md` first, then do this before writing anything:

1. Find the **single status source**. If there are two, one of them is wrong and you don't
   know which. Fix that before anything else.
2. Find the **live edge** — the last chapter that counts. Deleted, superseded and abandoned
   drafts will still be sitting in the tree, still readable, still wrong.
3. Run the verification script over everything. Expect failures. Fix them before adding.
4. Stamp superseded files. An unstamped stale file is a trap with a five-minute fuse.

Do not start writing chapter N+1 until those four are done. It feels slow. It is much faster
than the rebuild.
