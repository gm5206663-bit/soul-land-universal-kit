# GitHub Management Plan — Fire Phoenix

**Current mode:** public GitHub repository executed under `GITHUB_PUBLIC_VISIBILITY_AUTHORIZATION_2026-10-03.md`.
**Remote:** `https://github.com/gm5206663-bit/fire-phoenix-workshop.git`
**Default branch:** `main`
**StoryOS public layer:** unchanged; GitHub visibility is not StoryOS application.

## Repository posture

Public GitHub visibility was separately authorized and executed on 2026-10-03 for the tracked repository only; see `GITHUB_PUBLIC_VISIBILITY_EXECUTION_RECEIPT_2026-10-03.md`. It exposes the entire tracked workshop/history, so `GITHUB_PUBLIC_VISIBILITY_AUTHORIZATION_2026-10-03.md`, `NOTICE.md`, and `PUBLICATION_AND_DATA_CLASSIFICATION.md` control the distinction between repository visibility and StoryOS/public-story application. No new public release/license is added automatically.

Recommended future repository settings:

- default branch: `main`;
- `main` branch protection is active with the verified **Provenance and current-line checks** status check; see the public-visibility execution receipt;
- require the validation check before collaborator merges while retaining the documented owner/admin bypass;
- rely on SHA-pinned CI and installed local validation hooks in addition to public branch protection;
- GitHub accepted the secret-scanning and push-protection enablement request; retain the exact outcome in the execution receipt rather than assuming availability from visibility alone;
- keep Actions permissions read-only by default;
- do not enable automatic releases or Pages without separate authorization.

## What is ready now

- local Git repository initialization and local commit history;
- `.github/workflows/validate.yml` for recovery, V1-history, V2-current, staging, and acceptance checks;
- PR template, contribution policy, security policy, and project-control authority record;
- a dated locally accepted V2 Option A C48–C55 layer with hash-pinned provenance;
- a local-acceptance tag, `local-accepted-v2-option-a-2026-10-03`, which explicitly does not imply public release;
- `LOCAL_GIT_INITIALIZATION_RECEIPT_2026-10-03.md`, recording local commits, validation, and repository integrity;
- the quarantined rejected Dorm333-only Chapter-53 prose remains locally preserved but intentionally ignored by its nested quarantine `.gitignore`; it is not part of the staged remote-ready tree;
- an initially private remote and initial `main`/local-acceptance-tag push, recorded in `GITHUB_REMOTE_PUBLICATION_RECEIPT_2026-10-03.md`, followed by the separately executed public-visibility transition in `GITHUB_PUBLIC_VISIBILITY_EXECUTION_RECEIPT_2026-10-03.md`;
- `tools/configure_github_remote.sh`, which restores the approved non-secret `origin` URL when this sandbox resets transient Git configuration;
- SHA-pinned Actions, Dependabot monitoring for GitHub Actions, issue forms, `CODEOWNERS`, backup tooling, and an administrator settings checklist.

## What is intentionally not done

- no GitHub Release, Pages site, public Project board, public Discussions space, webhook, or public StoryOS application was created;
- no GitHub issue, PR, release, project board, deploy key, webhook, or automation token was created;
- no recovered public layer was changed or published.

No persistent GitHub credential is stored in this workspace. The destination was created privately, later converted publicly under direct authorization, and every one-time scoped credential used for these operations was removed after use.

## Authorized future remote procedure

For a future explicitly authorized push, first restore/check the approved public remote:

```bash
bash tools/configure_github_remote.sh
git remote -v
git push -u origin main
```

Before that action, re-run all checks in `CONTRIBUTING.md`, inspect `git status`, confirm the remote with `git remote -v`, and verify that the repository visibility matches the dated author authorization.

## Layer-aware review model

| Change class | Review expectation |
|---|---|
| Recovery/provenance | Must preserve byte/hash evidence and run recovery validation. |
| Frozen V1 | Must remain labelled historical; do not treat as current creative authority. |
| Protected V2 | Requires claim/continuity review and V2 validation. |
| Accepted snapshot | Must derive from validated V2/staging and carry a new dated hash manifest. |
| Public application | Requires a separate explicit author decision; local acceptance is insufficient. |
| Future chapters/source allocation | Requires a new direct authorization; C61 remains blocked. |

## License and attribution

No license is added automatically. The project is a fan-fiction/provenance workshop involving third-party intellectual property and non-public creative work; the author must make an informed licensing and visibility decision before external publication.
