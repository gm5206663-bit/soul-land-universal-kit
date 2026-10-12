# Chapter52 Validation — REWRITE v2 (2026-09-19)

Live edge: **after Chapter52**. Result: **PASS**

## Why this file exists

The human rejected the first Chapter52 draft as "pasted canon". Measurement agreed, for a stronger
reason than style: v1 reproduced the NovelFull Chapter177 scene in source order AND consumed beats
that this project bars until Chapter178/179 (`six days`, the communication setup). The saved verbatim
source contains no `six` and no `day`. v1 also carried three invented provenances (a lecture nine days
earlier, "the year before the exam", "the field guides") that no source supports.

## What v2 changes

- Structure: the herb reveal now lands at 69% of the chapter vs 88% in the source; Dorm333's own
  argument, scoring pressure and cost carry the scenes instead of source narration order.
- Removed: `six days`, `I want to talk to them`/`I can't, and you can`, any conclusion that the herb
  is worthless inside the simulation, any beast communication, any alliance.
- Invented provenances replaced with evidence available to the characters; Gravity Control named in
  Liu's report (documented in the consumed source), no in-world clock fabricated.
- Similarity to source prose: SequenceMatcher ratio 0.009; the only shared runs are this project's own
  established terminology (`golden-patterned Blue Silver Grass`).
- Body: 2501 words. Whole file sha256: `9d7b4c43df1b11cf9d92ee3b5a981663…`

## Validator output (captured, not transcribed)

```
STORYOS_VALIDATE: PASS  (phase=full, errors=0, warnings=0, learned-rules-active=2)
  [info] branch-supersession: CHAPTER_53_VALIDATION_2026-09-17.md still claims Chapter53 but IS marked superseded — trap neutralised. Keep it out of drafting context.
  [info] receipt-coverage: Chapter1 has no validation receipt recorded.
  [info] receipt-coverage: Chapter2 has no validation receipt recorded.
  [info] receipt-coverage: Chapter3 has no validation receipt recorded.
  [info] receipt-coverage: Chapter4 has no validation receipt recorded.
  [info] receipt-coverage: Chapter5 has no validation receipt recorded.
  [info] receipt-coverage: Chapter6 has no validation receipt recorded.
  [info] receipt-coverage: Chapter7 has no validation receipt recorded.
  [info] receipt-coverage: Chapter8 has no validation receipt recorded.
  [info] receipt-coverage: Chapter9 has no validation receipt recorded.
  [info] receipt-coverage: Chapter10 has no validation receipt recorded.
  [info] receipt-coverage: Chapter11 has no validation receipt recorded.
  [info] receipt-coverage: Chapter16 has no validation receipt recorded.
  [info] receipt-coverage: Chapter18 has no validation receipt recorded.
  NEXT CHAPTER: Chapter53  (source: Chapter178 Collaborate)
  GATE: clear — blueprint then draft
```

## Native checker (captured)

```
PERFECT_CONTINUATION_SKILL_CHECK_V2: PASS
phase=post
latest=Chapter52
next_fic=Chapter53
consumed_source=Chapter177
next_source=Chapter178
manifest_loaded=YES
active_stale_issues=0
mirrors_match=YES
future_route_body_leaks=0
```

RESULT: PASS
