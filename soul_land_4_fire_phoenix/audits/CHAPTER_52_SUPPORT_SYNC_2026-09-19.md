# Chapter52 Support Sync — REWRITE v2 (2026-09-19)

RESULT: PASS

Files advanced for the v2 rewrite, and nothing else:

| File | Change |
|---|---|
| `chapters/Chapter_52.md` | rewritten prose + footer documenting the withdrawal |
| `foundation/CURRENT_STATE_MANIFEST.json` | `latest_story_body_required_patterns` 11 → 10; **`six days` removed** because it was a leaked Chapter179 beat that I had laundered into a validator requirement |
| `canon_coverage/Canon_Coverage_Chapter_52.md` | new section `Withdrawn from the first draft`, incl. the governance defect (a required-pattern taken from my own draft forces the leak to stay) |

Rule learned and recorded: a required-pattern must be traceable to a beat of the **consumed** source
span, never to the draft's own prose. Patterns copied from a draft make the validator enforce that
draft's mistakes.

Support-state checks re-run after the change and still pass: live-edge patterns name
`Chapter_52\.md` and `Chapter177`; no file demands deleted history; superseded receipts remain marked
SUPERSEDED and were not touched.
