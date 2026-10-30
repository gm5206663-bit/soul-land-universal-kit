# Security policy

**This account publishes fiction, its method, and the tooling that checks it. There is no server,
no account system, no user data, and no database anywhere in it.** The realistic security surface
is narrow and it is listed below rather than implied.

## What is in scope

| Surface | Where |
|---|---|
| The published sites (GitHub Pages) | `*.github.io` — eight sites, all served from this account's repositories |
| The verification tooling | `SOUL_LAND_UNIVERSAL_KIT/tools/`, `tools/`, and each repository's own gates |
| Secrets and tokens | GitHub Actions secrets on this account's repositories |
| The supply chain | Actions pinned by commit SHA in `.github/workflows/` |

## What is not in scope

The fiction itself — canon accuracy, continuity, style, and prose quality — is **not** a security
matter. Every chapter-bearing tree on this account carries its own gate (`check_panels.py`,
`style_gate.py`, `run_all.py`, `mcu_verify.py`, `sentinel.py`) and those tools are the right
address for a content defect. So is the repository's `AGENTS.md`.

## Reporting

Report privately, not in a public issue:

- GitHub → **Security** tab → *Report a vulnerability* (private advisory), or
- email **gm5206663@gmail.com** with `SECURITY` in the subject line.

Include the repository, the file or URL, what an attacker could do with it, and the smallest
reproduction you have. A one-line "this looks wrong" is welcome; a proof is better.

**Response window:** acknowledged within 7 days, triaged and answered within 30. This is a
single-author account, not a company with an on-call rota — the windows are honest rather than
aspirational.

## Please do not

- Open a public issue, PR, or discussion describing an unpatched problem.
- Test against the published sites in a way that degrades them for readers (load testing,
  scraping at volume, writes).
- Access, modify, or exfiltrate content you are not the author of.

## What you can expect when something is confirmed

1. The finding is written down with a date, the affected paths, and the evidence.
2. The fix lands in the repository that owns the code, with its own gate re-run.
3. If an accepted artifact changed, the acceptance record is **re-stamped, not silently
   rewritten** — on this account an accepted hash is evidence that a reading happened, and
   restamping it to match the disk destroys that evidence.
4. The advisory is published once the fix is live.

## Scope note on this repository's own checks

`soul-land-universal-kit` verifies itself with `python3 tools/check.py` (links, spine, manifest
drift, structure, duplicate content). It does **not** claim to be a security audit of the account,
and it says so on every run.
