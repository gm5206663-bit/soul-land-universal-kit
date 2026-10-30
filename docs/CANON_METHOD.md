# THE CANON METHOD — follow the canon, and say at the head of every chapter which part of it

**Written 2026-10-30, from the author's own practice.** Every rule below is quoted or derived from
something this workspace already does — the seven-step method in `soul_land_3_oc/canon_coverage/INDEX.md`,
the coverage tables in the Fire Phoenix and Fire Dragon Lizard serials, and the headers in
`adaptive_prodigy` and `Miraculous_Project`. Nothing here is invented; where a rule is mine rather than
the author's, it says so.

---

## 1. The law it serves

> **Canon is ore, not transcript.** — the house line, in every chapter header that already exists.

Two things follow, and they pull in opposite directions:

1. **The canon is carried.** Its scenes run on the page, in order, unskipped. Compression is a
   retelling choice; **omission is a fidelity failure.** From `soul_land_3_oc/canon_coverage/INDEX.md`:
   *"every scene, choice, and named detail of the canon block, in order, including the small ones (a
   coin count, a scolding, a lunch bag)."*
2. **The chapter is ours.** The prose is not the canon's prose. The OC runs parallel, never instead —
   *"never crowding or rerouting canon's beats"*.

A chapter that satisfies both has to say **which canon** it is carrying. That is the whole reason for
the header. Not tidiness — checkability. A chapter that does not name its ore cannot be checked against
the canon at all. It can only be admired.

---

## 2. The rule, in one line

> **At the head of every chapter, before any prose, write which canon chapter or episode this chapter
> is built on — and where that claim comes from.**

Three shapes are already in use in this corpus. **All three pass the gate.** Pick by source type.

### 2.1 The novel form — the house default

```markdown
# Chapter 101: What the Sword Was

## Canon Reference: canon ch 286 "Dreams of Battle Armor" AS ORE (single-chapter span — the island night; the registration morning = canon 287 = ch102). Facts cited below. OURS entire: the lake lesson ("Show me"), the love-ledger beat, the hug through captain-grammar. **canon = ore; facts cited; trajectory ours.**
```

From `adaptive_prodigy/chapters/chapter_101.md` — 116 of 116 chapters in that serial carry this line.
Note what it does in one paragraph: **the canon span**, **what is canon's**, **what is ours**, and the
**next** chapter's span so the reader knows where the seam falls. That is the fullest form and the best
one to copy.

### 2.2 The short form — for a chapter that only needs the span

```markdown
## Canon Reference: SL3 ch1–ch2 (awakening · the walk home · the four bowls)
> Span taken from `canon_coverage/INDEX.md` — the receipt, not a memory. Canon is ore, not transcript; this chapter is ours.
```

This is what the backfill writes on 2026-10-30: the author's own coverage table quoted verbatim, with
the receipt named underneath. Short, checkable, no invented numbers.

### 2.3 The episode form — for an animated source

```markdown
**[canon: S1 slot 1 — Stormy Weather (production N° 101)]**
```

From `Miraculous_Project/chapters/Chapter_1*.md`. **A cartoon is numbered by episode and production
code, not by chapter** — and season + slot + title + production number together are what make an
episode uniquely identifiable across regional orderings. This form exists because a reader who looks
for "chapter 1" of Miraculous will find nothing.

The gate accepts: `ch`/`chapter` + a number · `novel prologue` · `episode`/`ep` + a number ·
`S1 E4` · `slot N` · `N° N`. It requires a **marker word** (`canon`) and a **locator** in the same
line, within the first 20 lines of the file.

---

## 3. Why it goes at the head, and not in a footer

Three reasons, and only the first is about the reader.

1. **The reader deciding whether to read on.** Someone who has read the canon wants to know whether
   this is the bit they love or a stretch they skipped. That is a first-screen question.
2. **The next agent.** Every agent that lands in a serial reads the chapter it is continuing. If the
   canon span is 200 lines down inside a record block, the agent proceeds without it — and then writes
   a chapter that re-covers ground already covered. This has happened; it is why the rule exists.
3. **The gate.** A check reads the head cheaply. A check that has to understand the whole file is a
   check nobody runs.

**On 2026-10-30, 66 chapters already contained a canon line — in the record block at the foot.** The
information was all there, in the wrong place, where it cannot do any of the three jobs above. Those
are listed in `reports/CANON-HEADERS-TODO.md` with the line to promote.

---

## 4. The seven steps — the author's method, quoted

From `soul_land_3_oc/canon_coverage/INDEX.md` §1, under the law **R12 · THE DUAL-TRACK LAW**
(*canon complete on the page; the OC runs parallel, never instead*). This is the fullest statement of
the method anywhere in the workspace, and it is the standard the other serials are measured against:

1. **Fetch live, read fully** — the chapter's canon block, from the working source. *"No canon from
   memory, ever."*
2. **List the beats** — every scene, choice and named detail of the canon block, **in order**,
   including the small ones: *a coin count, a scolding, a lunch bag*.
3. **Adapt all of them** — the beats run on the page, in order, unskipped. *"Compression is a
   retelling choice; omission is a fidelity failure. Nothing is demoted to a footnote."*
4. **Run the OC parallel** — what our character is doing in the same days; scenes out of canon's
   window; *"never crowding or rerouting canon's beats"*.
5. **Write the coverage doc the same turn** — `canon_coverage/Canon_Coverage_Chapter_0N.md`: which
   canon chapters were covered, the source lock, a beat-by-beat table (canon beat → how it is carried
   on our page), fidelity notes, and what is deliberately **not** touched.
6. **Receipt the ledger row(s)** — serial log, ledgers, audit — **one commit**.
7. **Re-measure** after the last text edit; *"receipts must equal the final numbers."*

Step 5 is what makes step 1 above the chapter possible: the coverage doc is written before the prose,
so the header is a **summary of a receipt that already exists** — never a memory typed at the top.

### The standing fidelity notes, also quoted

- **The clock wins.** *"When our pages and canon's days collide, canon's calendar is law — reconcile
  our clause, never canon's scene."*
- **The record shows.** Where canon measures, the OC's reading is *"exact, absent-with-reason, or a
  locked private note."*
- **No sidelining.** *"Canon is not a checklist and Su Yan is not a spectator"* — the parallel must
  **do work** while canon breathes.
- **Parallel, not overlapping.** Same town, same week, never each other's scenes: no knowledge, no
  saves, no crossings.
- **Do not re-stage.** New chapters get *new* receipts, not retro-edits.

---

## 5. What does not count

- **"Canon-inspired"** — a mood, not a reference. No locator, no line.
- **Naming the fic's own chapter number.** During the 2026-10-30 backfill I built an extractor that
  read `Target canon span for Chapter 8: **SL4 Chapters 41-45**` and returned **8** — the fic's own
  number, presented as the canon span. Ten Fire Phoenix chapters would have been given headers
  naming themselves. That is why every number this tool writes is **quoted from a receipt and the
  receipt is named in the header** — and why nothing is written when the receipt is ambiguous.
- **A canon line in the footer.** The head is the contract; the footer is the lab notebook.
- **A guess.** If the receipt does not state a span, the chapter stays in the pinned backlog. A wrong
  header is worse than none: it is a false receipt that others will trust.

---

## 6. The gate

```
python3 tools/canon_header.py --report      # coverage per serial, with what is still silent
python3 tools/canon_header.py --check       # the gate: fails on growth, fails on stale pins
python3 tools/canon_header.py --backfill    # fill from the author's coverage receipts
python3 tools/canon_header.py --freeze      # re-record the backlog (may shrink only)
python3 tools/canon_header.py --selftest    # prove the gate can fail
```

Wired into `tools/run_all.sh` as **layer 8**. It is read-only — the battery never edits a chapter.

**The pinned backlog.** 137 chapters predate the rule. Turning that red on day one would red the whole
workspace and teach everyone to ignore red, which the method warns about by name. Instead
`tools/canon_header_baseline.json` records exactly which chapters are unpinned, and:

- a chapter **not** in the baseline must carry a canon line — new chapters cannot slip in;
- a baseline entry that has since **gained** a line must be removed, or the gate fails;
- a baseline entry whose file is **gone** must be removed, or the gate fails.

**A pinned set that can grow is not a gate. It is a historian.**

---

## 7. State, 2026-10-30 — measured, not estimated

| serial | canon line | total | where the spans came from |
|---|---:|---:|---|
| adaptive_prodigy (SL3 Lin Hao) | 116 | 116 | written by the author, chapter by chapter |
| soul_land_2_new | 8 | 8 | written |
| soul_land_3_oc | 7 | 7 | backfilled from `canon_coverage/INDEX.md` |
| Miraculous_Project | 4 | 4 | written, **episode form** |
| dragon_prince_yuan_native_oc_fanfiction | 1 | 1 | promoted from its own record block |
| Soul_Land_2_Project | 23 | 24 | written; one variant file (`chapter_08a.md`) is silent |
| soul_land_4_fire_phoenix | 40 | 52 | 37 promoted from the chapters' own record blocks; 3 from the coverage index |
| soul_land_1_fire_dragon_lizard | 3 | 5 | coverage index + own record block |
| soul_land_devouring_dragon | 0 | 24 | **no per-chapter span anywhere yet** |
| soul_land_2_the_grey_wolf | 0 | 10 | **same** |
| qian_xunji | 0 | 9 | **same** |
| lan_shen | 0 | 8 | **same** |
| soul_land_new | 0 | 7 | **same** |
| soul_land_holy_spirit · soul_land_system_cheat | 0 | 8 | **same** |
| soul_land_3_new | 0 | 1 | **same** |

**202 of 284 chapter files (71%) name their canon source. 82 sit in the pinned backlog.**

How the 202 arrived matters, because the difference is the whole method:

- **147 already had a line** — the author's own practice, in three shapes.
- **4 more became visible** when the detector learned two shapes it had been blind to: the house
  shorthand `canon 247` (no `ch`), and headers hard-wrapped across several `##` lines. All four
  were in `adaptive_prodigy`, the serial with the strictest habit on the account. **A false gap
  is not a neutral error** — it invites someone to "fix" a chapter that was already correct.
- **14 were backfilled** from a coverage index (`soul_land_3_oc` ×7, `soul_land_1_fire_dragon_lizard`
  ×2, `soul_land_4_fire_phoenix` ×5).
- **37 were promoted** from the same chapter's own record block. The span was already written;
  it was 900 lines down. `--promote` copies the author's sentence to the head and leaves the
  original in place as the receipt, naming the line number it came from.
- **0 were guessed.** Where a serial's records do not say which chapter carries which span, the
  chapter stays in the backlog and `reports/CANON-HEADERS-TODO.md` lists it. Those serials keep
  canon in a harvest document, a canon ground or a fidelity ledger — global documents that never
  say *which chapter carries which span*. No tool can fill that. It fills as each chapter is
  written, because step 5 of the method produces the receipt the header quotes.

## 8. The one-line version, for an agent starting a chapter

> Write the canon coverage doc first. Put its span at the top of the chapter in parentheses after
> `## Canon Reference:`. Name the receipt underneath. Then write the chapter to the beats you listed —
> all of them, in order, with the OC running parallel and never taking a canon scene.

That is the method. Everything else in this file is the reasoning for it.
