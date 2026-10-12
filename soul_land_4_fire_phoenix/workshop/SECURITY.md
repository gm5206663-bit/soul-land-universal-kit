# Security and Sensitive-Source Policy

## Do not commit, paste, or attach

- GitHub tokens, passwords, private keys, cookies, or `.env` credentials;
- private/native manuscript content or repository exports without the author’s explicit permission;
- personal information, paid/locked adaptation panels, or unlawfully obtained source material;
- credentials copied from browser profiles, Git configuration, or external services.

A credential posted in a chat, issue, pull request, or document must be treated as compromised even if it is later deleted from local files. Revoke and rotate it immediately.

## Report a concern

Use a direct maintainer channel for a suspected secret or sensitive-source exposure. Do **not** open a public issue containing the secret, private material, or the full reproduction path. Public repository visibility does not make sensitive disclosure appropriate.

## Remediation sequence

If a secret or sensitive material is committed, uploaded, or shared:

1. stop further pushes and public sharing;
2. revoke/rotate the credential with its provider;
3. remove it from the working tree and Git history before any further external publication;
4. rerun `python3 tools/validate_github_governance.py` and `python3 tools/validate_all.py`;
5. document only the remediation status, never the secret itself;
6. assess whether repository visibility, external logs, or collaborator access require additional cleanup.

## Publication boundary

This public GitHub repository contains recovered public evidence and locally accepted creative material under the explicit visibility authorization. Repository visibility does not authorize StoryOS application, public releases, C56/C61 work, or additional external sharing beyond the tracked repository. Follow `PROJECT_CONTROL.md`, `GITHUB_PUBLIC_VISIBILITY_AUTHORIZATION_2026-10-03.md`, and `PUBLICATION_AND_DATA_CLASSIFICATION.md` for the authority ladder and controls.
