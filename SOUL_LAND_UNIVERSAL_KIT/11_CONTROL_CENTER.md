# 11 · THE CONTROL CENTRE

*One command for the state of every book on the account. Built 2026-10-11.*

The gates answer one question well: **is this chapter sound?** Nothing answered
the questions above that level — is the live directory the one that ships; does
the published site match the book; has a text quietly been given a second home;
does the README still describe the book it sits beside; does the same paragraph
appear in three chapters; and can anyone say, at the end of a run, what was
actually read.

This is that layer.

```
python3 tools/account.py report --root /tmp/all --out-prefix account_report
python3 tools/account.py diff   --root /tmp/all --baseline account_baseline.json
python3 tools/account.py index  --root /tmp/all
python3 tools/account.py freeze --root /tmp/all --out account_baseline.json
python3 tools/account.py selftest
```

Optional: `--pages --token-file PATH` also asks the **live GitHub Pages sites**
what they publish, instead of trusting the repository's copy of a site.

---

## 1 · The one defect this exists to prevent

*A check that reports success while covering less than it claims.*

Every instance this house has found wore different clothes: a gate that read
six of ten chapters and passed; a sentinel that checked one of twenty-two
things; a stage that built zero of fifty-two chapters and printed `stage built:
57 files`; a sweep that matched the directory *name* `chapters` and therefore
read the rejected draft instead of the live book. Same defect, seven times.

The cure is always the same three things, and every detector here obeys them:

| rule | how it is enforced |
|---|---|
| **declare coverage** | every detector returns *n of m*, printed in the report; a detector that examined nothing raises a finding instead of returning a silent zero |
| **carry evidence** | every finding quotes the sentence, the line, or the number that produced it — a finding you cannot check is a rumour |
| **stable identity** | every finding has an id built from what it is about (kind + location + subject), never from a size or a line number, so runs can be diffed and progress measured |

## 2 · The detectors

| detector | the question it asks | reading |
|---|---|---|
| **gate** | is each chapter sound, and is the live directory the one that ships? | the 60-word ceiling, the floor of three spoken lines, declared exemptions, orphan sources, author/reader drift |
| **dupes** | does the same prose appear twice? | a duplicate **inside one file** is hard (an accident); the same sentence across chapters is advisory (possibly a refrain) |
| **two-homes** | does one text live in two books? | identical body hash in two independent books; a book and its own published copy are one home, by design |
| **receipts** | does the book's own paperwork agree with the book? | "chapters 1–N", "live edge ChN", "N chapters live" against the text on disk |
| **publication** | does the in-tree site match the source? | chapter html in the repository against the book's chapters |
| **pages** | does the **live** site match the book? | the Pages URL itself, through the API — a repository can hold a perfect site that was never deployed |

## 3 · Severity is a judgement the house already made

**Hard — not the author's call:** a sentence over 60 words · dialogue under the
floor of three · a reader edition that is not the gated text · an orphan
published chapter · the same sentence twice in one file · a live site that does
not match the book · a scope that cannot be determined · a report over nothing.

**Advisory — the author decides:** the 2,400–3,400w band · the 8/1k dialogue
bar · a refrain across chapters · one text in two homes · a status line that has
drifted · a list that was truncated.

An exemption is never silent. Devouring Dragon's zero dialogue is LAW (RAILS
s45, CANON VOICE LAW s53); the gate prints the exemption, cites the receipt, and
**fails if that receipt cannot be found**. Law is not reported as defect, and an
exception nobody can check is not an exception.

## 4 · Why the numbers can be trusted

- **Determinism was proven, not assumed.** Three consecutive runs must be
  byte-identical in their totals. The first version sorted repeated sentences by
  size only, left ties in filesystem order, and reported 874 findings on one run
  and 860 on the next — a tool that was not comparable with itself.
- **Hard findings get their own listing budget.** A defect must never be pushed
  out of a report by a stylistic note. When this was wrong, 83 real duplicates
  inside single files were reading as 28.
- **Truncation is a finding.** 7,745 repeated sentences of 12+ words were found
  on the account; the 400 with the most occurrences are listed, and the gap is
  itself reported as a `coverage-gap`.
- **Two identical long sentences in one file get two ids.** Without an
  occurrence ordinal they shared one, and 5 findings collapsed into others when
  a baseline was frozen — a collapsed finding can never be reported as fixed,
  because it was never separately known.
- **A baseline knows which code made it.** `freeze` records a fingerprint of the
  detectors; `diff` warns when they have changed, because NEW/FIXED across
  different detectors is not a comparison.
- **Every detector was seen to fail.** `account_selftest.py` builds a small
  account, injects one defect at a time, and requires the owning detector to
  fire — and the clean tree to stay silent, so no detector can pass by flagging
  everything.

## 5 · The bugs this system found in itself

Recorded because they are the reason the account numbers can be quoted at all:

1. **571 run-ons from a reference copy.** The control centre gated
   `soul-land-projects/reference/sl3_lin_hao/` — a historical snapshot of a book
   that exists elsewhere — and reported SL3's over-long sentences twice. The
   scope rule now lives in ONE function (`is_out_of_scope`) used by both the
   gate and the centre, so they can never disagree about what exists.
2. **`## Canon Reference:` counted as prose.** The heading filter tested
   `l.startswith('# ')` and therefore never matched `##`. Outline documents
   named `chapter_NN.md` were being measured as narrative prose.
3. **The plan-line filter never worked.** Its regex was written with double
   backslashes inside a raw string, so `(\s|$)` matched a literal backslash and
   the filter had only ever matched the `·` separator. Found by testing the
   behaviour instead of the patch: the filter was rewritten and is now covered
   by a test that runs the real function over a real file.
4. **The Pages API answers with its own URL.** Reading `url` instead of
   `html_url` made the detector fetch the API endpoint as if it were a website,
   404, and report three drift findings that were entirely its own mistake.
5. **A historical note is not a claim.** "V1 ARCHIVED (15 chapters, pre-rebuild)"
   and "all 24 chapters live" (about *another book*) were both reported as the
   live book drifting. Both are now silent, and both are selftest cases.
6. **A book and its own published copy are one home.** Counting them as two made
   54 twin groups look like duplication; one independent pair remains.
7. **The list could hide the defect.** See §4, twice.
8. **A published copy is not a second place either.** The same rule as bug 6,
   applied to the dupes detector: it was reporting every shared sentence between
   a book and its own published snapshot — 61 of 66 NEW findings in a single run
   were one book pairing with its own stage copy. A sentence whose source
   carries it is now the snapshot doing its job; a sentence **only** a copy
   carries is drift and still fires. 7,608 such occurrences were ignored in the
   live account and the note says so.

## 6 · Current state

**2026-10-11 (evening, after the repair sweep) · 24 books · 274 chapters ·
1,151,458 words · 21,726 spoken lines.**

**138 hard · 73 advisory**, every class sample-verified against the text:

| kind | count | severity | note |
|---|---|---|---|
| over 60 words | 119 sentences in 15 files, 3 repos | hard | 70 in `supergirl-adrian-vale` (a beat-style voice question, see below), 48 in the archived `SOUL_LAND_NEW` scaffold, 1 unsplittable sentence in the kit |
| repeated inside one file | 17 | hard | one sentence twice inside otherwise-different paragraphs; the author's echo style — reported, not cut |
| dialogue under the floor | 2 | hard | two 20-word stub chapters (`soul_land_starter`, `soul_land_new`), author's call |
| repeated across chapters | 69 | advisory | the house refrain style; the author decides |
| receipt drift | 2 | advisory | Grey Wolf `NEXT.md` says 6, book has 10; Soul Land 2 README says edge 21, book has 23 |
| one text, two homes | 1 | advisory | a 20-word stub in two repositories |
| dialogue exempt | 1 | advisory | Devouring Dragon, by law |

Live sites: 3 repositories publish; **1 compared to its book and it agrees**
(Grey Wolf, 10 chapter links = 10 chapters); 2 are declared *uncompared* because
those repositories hold several books — "I could not compare this" is reported,
never counted as a pass.

### What the repair sweep changed (measured, not claimed)

The sweep was measured twice against the 10:08 baseline (875 findings, code
`948038a6`).

*Under the detector as it stood at the freeze:* **415 FIXED · 66 NEW · 460 STILL
OPEN.** Read by kind, the 415 are 349 over-60 sentences split at boundaries their
own prose already had (kit 295, `stark_heir` 29, `mcu_eternal_fanfic` 8,
`supergirl` 8 removed with its padding, `lan_shen` 3,
`soul_land_4_fire_phoenix` 3, the storyos stage 3) and 66 duplicate-passage
clusters removed from `supergirl`. All 66 NEW were advisory refrains; **61 of
them were the published-copy artifact that self-bug 8 records**, and 5 were real
new echoes (three in `supergirl`, two in the kit).

*After self-bug 8 was fixed:* the same account reads **717 FIXED · 53 NEW · 158
STILL OPEN** — and the diff itself refuses to call that a comparison, because the
detector code changed under the baseline. The reshuffle is why: a cluster that
loses its published-copy place can reclassify from `repeat-across` to
`repeat-in-file`, which changes the finding's kind and therefore its stable id —
one defect, two ids, one counted FIXED and one counted NEW. That is exactly the
mismatch the fingerprint warning exists to expose, so the baseline was re-frozen
rather than the numbers massaged.

Two different things happened to the words on disk, and they should not be
blurred: **a sentence split moves no word at all** (punctuation only), while
**removing duplicate passages removes 7,702 repeated words** from
`supergirl-adrian-vale` — which is why the account total falls by exactly that
kind of amount (1,159,282 → 1,151,458) and why five of its chapters now sit
below the `Full 3000+ Words` their own headers claim. That is recorded as an open
author's question, not dressed up as a repair.

Baselines: `account_baseline_2026-10-11T1008_pre-repair.json` keeps the 875-finding
pre-repair freeze; `account_baseline.json` is the new living freeze (211 findings,
code `e88acf85de8a`) taken after the detector change, because a baseline frozen
under different detector code cannot honestly report NEW/FIXED — the diff says so
itself when it detects the mismatch.

The truncation note is gone: after the published-copy rule, 86 repeated sentences
were found and all 86 are listed.

## 7 · What it will not do

- It never edits a manuscript. Detectors report; repairs are deliberate and
  recorded.
- It never decides an author's call — band, bar, refrain, a second home.
- It never reports a number it has not verified against the text. Its first
  account run produced 1,034 hard findings; roughly half were its own bugs, and
  **none of them were reported anywhere** until they were fixed.
- It never reports success over nothing. Zero books found is a hard finding.

---

**Files:** `tools/account.py` (CLI, report, baselines) ·
`tools/account_checks.py` (the detectors) · `tools/account_selftest.py` (14 cases) ·
`tools/account_baseline.json` (today's frozen state) ·
`tools/live_book_gate.py` (the per-book gate it delegates to).
