# GitHub Project and Label Setup

This file is a public-repository operating plan. It does not authorize a public StoryOS application, public release, or public Project board beyond the repository/issue visibility decision.

## Recommended labels

| Label | Color | Meaning |
|---|---:|---|
| `type: continuity` | `B60205` | Causal, mechanics, character, or voice correction. |
| `type: source-claim` | `1D76DB` | Provenance, source-access, or evidence-classification correction. |
| `type: decision` | `5319E7` | Requires a direct author decision. |
| `layer: recovery` | `006B75` | Recovered public evidence/provenance. |
| `layer: frozen-v1` | `6E7781` | Historical V1 only. |
| `layer: v2` | `FBCA04` | Protected current V2 lineage. |
| `layer: accepted-local` | `0E8A16` | Locally accepted but not public. |
| `boundary: public-decision` | `D93F0B` | Cannot proceed without explicit public-application authority. |
| `boundary: future-locked` | `BFD4F2` | C56/C61 or later-source material blocked. |
| `security` | `D73A4A` | Credentials, sensitive source, or access issue. |
| `needs-authority` | `FFFFFF` | Evidence is insufficient to act. |

## Recommended private Project board

Create a private GitHub Project named **Fire Phoenix Control Board** with these statuses:

1. **Evidence / triage** — source/provenance question not yet classified.
2. **Authority needed** — cannot progress from inference alone.
3. **Protected V2 work** — authorized work in protected lineage.
4. **Validation / review** — awaiting the required suite and human review.
5. **Locally accepted** — dated snapshot exists; not public.
6. **Public decision required** — separate publication authorization needed.
7. **Archived / historical** — V1, superseded, rejected, or closed evidence.

Suggested custom fields: `Layer`, `Authority date`, `Publication status`, `Validator status`, and `Source-access class`.

## Safe issue policy

- Use the three supplied issue forms rather than free-form tickets.
- Never put secrets, private manuscript text, locked adaptation panels, or unverified native-source claims in an issue.
- Apply labels only after the remote-label list has been created by an admin.
- Issues are evidence/decision records, never automatic creative or public-publication authority.
