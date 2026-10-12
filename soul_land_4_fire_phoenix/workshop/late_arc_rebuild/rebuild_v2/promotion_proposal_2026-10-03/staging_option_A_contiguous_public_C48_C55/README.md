# Option A — Contiguous Public C48–C55 Staging Candidate

**Status:** staged for review only; **not applied**.  
**Selection:** author chose Option A on 2026-10-03.  
**Public source layer:** untouched.

This directory contains a reader-facing, contiguous candidate sequence built from the eight protected V2 causal units. It is intentionally separate from `sources/storyos_current_public_layer/`.

## Mapping

| Candidate public file | Protected V2 source | Action if separately approved |
|---|---|---|
| C48 | V2 C48 | Replace current public C48 |
| C49 | V2 C49 | Replace current public C49 |
| C50 | V2 C50 | Replace current public C50 |
| C51 | V2 C51 | Replace current public C51 |
| C52 | V2 C52 | Replace current public C52 |
| C53 | V2 C54 | New public candidate; header renumbered only |
| C54 | V2 C55 | New public candidate; header renumbered only |
| C55 | V2 C60 | New public candidate; header renumbered only |

The candidate files contain prose only: V2 author-review continuity notes have been stripped from the staged public bodies and remain in the protected V2 originals.

## Hard boundary

- No recovered public file has been changed.
- No state/gate has been changed.
- No C56 or later public chapter is created.
- No C61 is created or implied.
- `staging_manifest.json` is the hash-anchored inventory; verify it before any future apply proposal.
- `candidate_state_overlay_option_A.json` describes the proposed state change without touching the live public state.
- `OPTION_A_STAGING_VALIDATION_2026-10-03.md` records the passing non-applying staging validation; rerun `validate_option_a_staging.py` after any staging edit.
- `OPTION_A_PUBLIC_STAGING_REVIEW_PACKET.md` presents the eight proposed public chapters in reader-facing C48–C55 order.
