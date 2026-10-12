# V2 Public-Promotion Proposal — Review Package

**Status:** Option A selected; a contiguous C48–C55 candidate is staged for review and **not applied**.  
**Created:** 2026-10-03.  
**This package makes no public-layer, state, gate, or frozen-draft change.**

## Why this package exists

The line-edited V2 replacement set is ready for author review, but it cannot be copied blindly into the recovered public StoryOS layer:

- the public layer currently ends at Chapter 52;
- V2 rewrites public Chapters 48–52 rather than adding after them;
- V2 deliberately consolidates old C52/C53 and C56–C60, so its internal working labels have intentional gaps;
- the public state/gate still describes the former Chapter-52-only edge and a source-text-missing drafting block.

This proposal separates the editorial decision from an irreversible technical update.

## Package contents

1. `PUBLIC_IMPACT_AND_NUMBERING_DECISION_2026-10-03.md` — current/public-to-V2 mapping, safe numbering choices, and the author decision required before any publish candidate can exist.
2. `CANDIDATE_STATE_DELTA_2026-10-03.md` — the exact narrative-state changes a later accepted public state would need to record.
3. `CANDIDATE_GATE_AND_AUTHORITY_DELTA_2026-10-03.md` — which legacy public-layer assertions would need supersession, and the validation result against existing prohibited literals/patterns.
4. `candidate_manifest.json` — hash-anchored baseline and V2 inventory, intentionally marked `AWAITING_AUTHOR_NUMBERING_DECISION`.
5. `existing_public_gate_content_screen_2026-10-03.json` — reproducible zero-match screen of V2 story bodies against the current public rules’ listed literals and regexes.
6. `staging_option_A_contiguous_public_C48_C55/` — the selected, hash-verified reader-facing C48–C55 candidate, with its own state overlay, validator, validation receipt, and review packet.

## What has been verified already

- The current public prose endpoint is `Chapter_52.md`, **Amiable Beasts**.
- Current public Chapters 48–52 exist and would be replacements, not additions.
- The V2 line has eight causal units and no C61.
- The existing public gate’s listed banned literals and regex patterns find **zero** matches in the eight V2 story bodies.
- This does **not** mean the public gate is ready to accept V2: its live edge, source-coverage record, and chapter-number model still refer to the old Chapter-52 baseline.

## Non-authorization guard

Nothing in this directory authorizes:

- copying V2 prose into `sources/storyos_current_public_layer/`;
- modifying public `state.json`, `state.txt`, `gate.json`, `gate.txt`, `rules.md`, or decisions;
- changing the existing 1,115-file recovery record;
- publishing a non-contiguous chapter sequence;
- creating C61 or allocating later source material.

The next operation must follow an author-selected numbering strategy and an explicit approval to supersede the current public C48–C52 baseline.
