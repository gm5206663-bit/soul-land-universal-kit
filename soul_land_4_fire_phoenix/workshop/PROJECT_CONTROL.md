# Fire Phoenix Project Control

**Current status:** `LOCAL_ACCEPTED_NOT_PUBLIC` — this remains the creative/publication status; the GitHub repository itself is separately public.
**Effective date:** 2026-10-03  
**Git status:** public GitHub repository verified; public-visibility execution and the current `main` state are recorded in `GITHUB_PUBLIC_VISIBILITY_EXECUTION_RECEIPT_2026-10-03.md`. Future pushes remain authority-gated.
**Public recovery status:** unchanged and hash-verified.  
**C61:** not authorized.

## 1. Active local creative line

The current locally accepted replacement is:

`accepted_replacement_layers/2026-10-03_option_A_v2_contiguous_C48_C55/`

It contains the selected contiguous reader-facing line C48–C55, with this durable mapping:

| Accepted local chapter | Protected V2 source |
|---|---|
| C48 — _The Line We Keep_ | V2 C48 |
| C49 — _What They Carry_ | V2 C49 |
| C50 — _Two Maps of the Forest_ | V2 C50 |
| C51 — _The Cost of Quiet_ | V2 C51 |
| C52 — _What the Ground Keeps_ | V2 C52 |
| C53 — _What a Favor Costs_ | V2 C54 |
| C54 — _What We Leave Open_ | V2 C55 |
| C55 — _The Price of Keeping_ | V2 C60 |

The protected source, claim audit, craft diagnosis, and line pass remain in `late_arc_rebuild/rebuild_v2/`. The accepted copy must never be edited in isolation; revise V2 first, validate, then create a new dated accepted layer.

## 2. What this does and does not change

### Local acceptance does

- establish the above C48–C55 line as the current local creative reference;
- preserve the selected causal-unit consolidation instead of restoring filler C53/C56–C60 boundaries;
- make a hash-pinned, reader-facing snapshot available for local Git tracking and review.

### Local acceptance does not

- overwrite `sources/storyos_current_public_layer/`;
- alter recovered public `state.json`, `state.txt`, gate/rules/decisions, source files, or recovery provenance;
- delete frozen V1 late-rebuild files, historical contracts, audit receipts, rejected drafts, or archives;
- authorize a public StoryOS application, a release, Pages, an additional public distribution channel, or any future GitHub push without direct author approval; GitHub repository visibility was separately authorized and executed;
- authorize C56, C61, future-source allocation, or adaptation claims.

## 3. Authority order

1. Direct author instruction in the current conversation.
2. This project-control document and the dated local acceptance record.
3. V2 claim audit, source-learning diagnosis, rebuild map, line pass, and promotion package.
4. Current semantic/source audits and hard continuity locks.
5. Recovered public StoryOS layer as immutable public baseline evidence.
6. Frozen V1 replacement materials, historical validators, continuation preparation, and archives as labelled historical evidence.

Older root navigation files may describe the former V1 C48–C60 author-review line. They remain historical context, but they do not supersede this local V2 acceptance.

## 4. Hard story controls

- The Purple Zoysia remains held under the active six-day AU condition; no source-timing handover.
- The Gold Silk Ape remains unstable, autonomous, and unavailable as a pet, scout, weapon, tracker, or command asset.
- Qian uses only deliberate, immediate, bounded contact in the stated V2 scenes; no passive tether, emotion/image feed, tracking, or human radar.
- Liu has one bounded Silver Edge finish; no mastery/repeat shortcut.
- Yan has no future ring, external bone, later Phoenix state, Domain, Nirvana, armor, or identity disclosure.
- Song/Luo gain no invented skills, rings, bones, gear, or super-senses.
- Ye retains her independent route; no merger, debt, confession, romance payoff, or identity disclosure.
- No C61 or later-source/endgame movement is authorized.

## 5. Required checks before any local change

Run the complete suite with `python3 tools/validate_all.py` (or `make validate`). The suite executes:

```bash
python3 tools/validate_github_governance.py
python3 tools/verify_public_recovery.py
python3 tools/validate_workshop.py
python3 tools/validate_replacement_line_48_60.py
python3 tools/validate_current_v2_line.py
python3 late_arc_rebuild/rebuild_v2/promotion_proposal_2026-10-03/staging_option_A_contiguous_public_C48_C55/validate_option_a_staging.py
python3 tools/validate_local_accepted_v2_release.py
```

`tools/validate_replacement_line_48_60.py` validates frozen V1 historical integrity. It should remain runnable, but it is not a validator for the accepted V2 line.

## 6. GitHub remote boundary

The GitHub repository at `https://github.com/gm5206663-bit/fire-phoenix-workshop` is public under the executed `GITHUB_PUBLIC_VISIBILITY_AUTHORIZATION_2026-10-03.md`; the exact transition and controls are recorded in `GITHUB_PUBLIC_VISIBILITY_EXECUTION_RECEIPT_2026-10-03.md`. Public repository visibility makes tracked workshop material and reachable history public, but does **not** modify the recovered public StoryOS layer or apply the V2 line to StoryOS.

No persistent GitHub credential is stored in the workspace. This sandbox may reset `.git/config`; run `bash tools/configure_github_remote.sh` before a later explicitly authorized push, then verify with `git remote -v`. Public releases, Pages, public StoryOS application, C56/C61 work, or future pushes still require their own explicit author instruction.
