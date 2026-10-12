# GitHub Admin Settings Checklist

This is the remaining and execution-record checklist. It requires an authenticated repository administrator for setting changes; completed public-visibility controls are recorded below and in `GITHUB_PUBLIC_VISIBILITY_EXECUTION_RECEIPT_2026-10-03.md`.

## Keep / enable

- [x] Repository visibility is **Public** under `GITHUB_PUBLIC_VISIBILITY_AUTHORIZATION_2026-10-03.md`.
- [ ] Issues remain enabled for the supplied public issue forms.
- [ ] GitHub Actions is enabled with default workflow token permissions set to **read repository contents**.
- [x] GitHub accepted the public-repository secret-scanning and push-protection enablement request; see `GITHUB_PUBLIC_VISIBILITY_EXECUTION_RECEIPT_2026-10-03.md` for the exact API outcome.
- [ ] Dependabot alerts and GitHub Actions updates are enabled if available.
- [ ] Create the labels and private Project board described in `GITHUB_PROJECT_SETUP.md`.

## `main` ruleset — historical limitation and completed public configuration

**Historical limitation (resolved):** the 2026-10-03 API attempt returned `403` while the repository was private because GitHub branch protection required GitHub Pro or public visibility. After the separately authorized public-visibility transition, the retry succeeded; the exact result is recorded in `GITHUB_PUBLIC_VISIBILITY_EXECUTION_RECEIPT_2026-10-03.md`.

Public branch protection was accepted on 2026-10-03. It applies the following policy to `main`:

- [x] Block force pushes.
- [x] Block branch deletion.
- [x] Require linear history.
- [x] Require conversation resolution for pull requests.
- [x] Require the **Provenance and current-line checks** status check before merge.
- [ ] Require pull requests for collaborators. For a sole maintainer, retain an explicit owner/admin bypass rather than locking yourself out.
- [ ] Add required code-owner review only after confirming the `CODEOWNERS` mapping and collaborator workflow.

## Do not enable or expand without a separate author decision

Repository visibility is already public under the executed 2026-10-03 authorization. That decision does **not** authorize any additional distribution channel or story-facing publication action:
- [ ] GitHub Pages.
- [ ] Releases or release automation.
- [ ] Deployment environments.
- [ ] Repository transfer, deletion, or archival.
- [ ] A public GitHub Project, Discussions, or external webhook.

## Credentials

For future one-time repository administration, use a fresh, short-lived fine-grained token restricted to this repository. Minimum permissions vary by task:

| Task | Fine-grained permission |
|---|---|
| Push ordinary files | Contents: Read and write |
| Update Actions workflow | Workflows: Read and write plus Contents: Read and write |
| Labels / issues | Issues: Read and write |
| Branch rules/settings | Administration: Read and write |

Never paste a long-lived credential into project files, commit history, an issue, or a PR. Revoke a token immediately after a one-time administration task.
