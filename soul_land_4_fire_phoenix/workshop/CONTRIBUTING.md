# Contributing to the Fire Phoenix Workshop

## Read first

1. `PROJECT_CONTROL.md` — current authority and hard boundaries.
2. `PROJECT_COMPREHENSION_AND_MANAGEMENT_PLAN_2026-10-03.md` — layer map and management rationale.
3. `PUBLICATION_AND_DATA_CLASSIFICATION.md` — what may be preserved, reviewed, or shared.
4. `accepted_replacement_layers/2026-10-03_option_A_v2_contiguous_C48_C55/ACCEPTANCE_RECORD_2026-10-03.md` — scope of the locally accepted V2 line.

This is a provenance-preserving workshop. A change that collapses recovered public evidence, frozen V1 history, protected V2 source, and local acceptance into one unlabelled copy is not acceptable.

## Change rules

- Do not modify `sources/storyos_current_public_layer/`, its state/gate/rules files, or recovery provenance unless a later explicit public-application decision authorizes it.
- Do not edit an accepted replacement snapshot by itself. Change the protected V2 lineage, validate it, then create a new dated accepted layer with hashes and an acceptance record.
- Treat V1 C48–C60 materials as historical. Treat V2 Option A C48–C55 as the current local creative line.
- Do not create C56/C61 or allocate later source material without new direct authority.
- Do not add invented mechanics, future-source outcomes, unverified adaptation claims, secrets, private repository contents, or credentials.
- Preserve rejected/archived material rather than deleting it to make the tree look simpler.
- Use the supplied issue forms for continuity, source-claim, and publication-decision records; an issue never creates creative or publication authority.

## Required local checks

Run the complete suite before committing relevant work:

```bash
python3 tools/validate_all.py
# or: make validate
# optional one-time local enforcement:
bash tools/install_local_hooks.sh
```

The suite includes GitHub-governance/security checks plus these story/preservation validators:

```bash
python3 tools/validate_github_governance.py
python3 tools/verify_public_recovery.py
python3 tools/validate_workshop.py
python3 tools/validate_replacement_line_48_60.py
python3 tools/validate_current_v2_line.py
python3 late_arc_rebuild/rebuild_v2/promotion_proposal_2026-10-03/staging_option_A_contiguous_public_C48_C55/validate_option_a_staging.py
python3 tools/validate_local_accepted_v2_release.py
```

The V1 validator is a historical-integrity check; it is not V2 promotion certification.

## Commit and review guidance

Use narrow commits with a clear scope, for example:

- `docs: establish local V2 project control`
- `acceptance: record Option A C48-C55 snapshot`
- `ci: harden provenance and GitHub validation`
- `security: update sensitive-source policy`

A pull request should state its authority, whether it touches a protected layer, and which validators were run. `CODEOWNERS` provides a default owner-review map; enable mandatory code-owner review only after confirming the collaborator workflow in `GITHUB_ADMIN_SETTINGS_CHECKLIST.md`.
