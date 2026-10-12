# StoryOS Universal Foundation — v3

A canon-discipline system, not a story. **Project-agnostic by design:** point it at any
long-running serialised project and it derives state, enforces the rules, and hands off
cleanly to a new AI. The Story Land 4 Fire Phoenix fic is the corpus it is currently wired to.

## Why this exists
Your old control centre *displayed* state. Displayed state can silently lie — and it did:
`CHAPTER_53_VALIDATION` said “Chapter53 is valid and ready” after the user rejected that
branch, and `SP526` / `Dawnflame 960` / `Dawn-Iron 2,480` were drift values a repair had
already removed. Here those are **enforced** by tooling, and the two traps are now marked.

## Layout
| Path | Role |
|---|---|
| `AGENT_ONBOARDING.md` | **Read first.** Phase 0 gate, authority order, prohibitions |
| `foundation/STATUS_PANEL.md` | Live state (generated) |
| `foundation/NO_MISTAKE_LIVE_RULES.md` | Rules R01–R24, each traceable to a real failure |
| `foundation/PERFECT_CONTINUATION_SKILL.md` | The six gates + continuation algorithm |
| `foundation/CURRENT_STATE_MANIFEST.json` | Machine state, schema `storyos-manifest/3` |
| `foundation/canon/locks/*.card.md` | 41 lock cards, each citing its source receipt |
| `foundation/canon/characters/*.card.md` | 9 character cards, floor + ceiling |
| `foundation/BANNED_TOKENS.json` | Regression-token registry |
| `canon_coverage/CANON_LEDGER.md` | fic ↔ canon, per-chapter status |
| `canon_coverage/BRANCH_LEDGER.md` | active vs superseded branches |
| `tools/storyos_validate.py` | The gate: 9 checks, blocks drafting on error |
| `scripts/scan_project.py` | Rebuilds manifest + cards from any corpus |
| `scripts/gen_docs.py` | Renders the human docs from the manifest |
| `scripts/build_site.py` | Builds the control centre, embedding live gate status |
| `templates/` | Coverage, receipt, and new-project manifest skeletons |
| `site/index.html` | The dashboard (self-contained; `STATE.json` beside it) |

## One command
```bash
python3 scripts/scan_project.py <corpus_dir> . && python3 scripts/gen_docs.py \
 && python3 scripts/build_site.py . && python3 tools/storyos_validate.py --project . --phase full
```

## New project in 4 steps
```bash
cp -r tools scripts templates AGENT_ONBOARDING.md ../my-new-project/
cp templates/PROJECT_MANIFEST_TEMPLATE.json ../my-new-project/foundation/CURRENT_STATE_MANIFEST.json
# fill only what is true; leave blanks rather than guessing
python3 tools/storyos_validate.py --project ../my-new-project --phase pre
```
Then `python3 tools/storyos_validate.py --selftest` any time you doubt the guards.

## Invariants
1. **Nothing is hand-typed into state.** Numbers come from files, so state cannot drift from canon.
2. **A rule that cannot be checked is not enforced.** Hence gates, not prose.
3. **Missing is reported, not invented.** `UNKNOWN — needs source` beats a confident fabrication.
4. **Rejected work is quarantined, marked, and inert** — never deleted, never live.
5. **The dashboard is a mirror.** Authority order ends at `AGENT_ONBOARDING.md`.
