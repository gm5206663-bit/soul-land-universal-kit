# Publication and Data Classification Policy

**Current repository posture:** public GitHub workshop mirror by direct author decision.
**Public StoryOS application:** not authorized.
**Repository visibility authorization:** recorded in `GITHUB_PUBLIC_VISIBILITY_AUTHORIZATION_2026-10-03.md`; releases remain separate decisions.

## Classification matrix

| Class | Examples | Repository treatment | External-publication rule |
|---|---|---|---|
| Recovered public evidence | `sources/`, `provenance/`, public state/gate artifacts | Preserve byte/hash provenance; do not normalize or overwrite. | Public GitHub visibility is expressly authorized, but evidence must never be relabelled as new/current prose. |
| Historical internal material | Frozen V1, rejected preparation, historical audits | Keep labelled historical; do not promote by implication. | May be publicly visible as history only; never present as current/public StoryOS prose. |
| Protected V2 | `late_arc_rebuild/rebuild_v2/` | Current protected source/craft lineage. | Publicly visible in the authorized repository, but still requires a separate StoryOS/public-story application decision. |
| Locally accepted snapshot | `accepted_replacement_layers/2026-10-03_option_A_v2_contiguous_C48_C55/` | Current local creative reference; hash-pinned. | Publicly visible through GitHub; `LOCAL_ACCEPTED_NOT_PUBLIC` still means no automatic StoryOS application. |
| Quarantined local-only material | Rejected Dorm333-only Chapter 53 prose | Preserve locally; intentionally ignored from Git. | Remains untracked and unuploaded; public-repository authorization did not include it. |
| Credential/sensitive access material | Tokens, passwords, private keys, cookies, private exports | Never commit, attach to an issue, or preserve in project history. | Revoke/rotate immediately if exposed. |

## Publication controls

1. Public GitHub visibility is authorized only for the currently tracked repository/history; it does not authorize a release, Pages deployment, or StoryOS application.
2. `sources/storyos_current_public_layer/` and its state/gate/rules files remain immutable unless a direct StoryOS public-application authorization says otherwise.
3. An accepted snapshot must trace to protected V2/staging lineage and carry a dated manifest/receipt.
4. No C56, C61, future-source/endgame allocation, or adaptation conclusion may be created by repository workflow, issue discussion, or inference.
5. Do not add private/native repository content, locked adaptation material, or credentials. The intentionally ignored local quarantine remains outside the public repository.
6. Before a future authorized push, release, or StoryOS publication decision, run `python3 tools/validate_all.py` and record the authority in a dated decision file.

## External copy/share checklist

Before sharing any file outside the authorized public repository or creating a new public distribution channel, confirm all of the following:

- [ ] The author explicitly approved the destination and visibility.
- [ ] The material is correctly classified above.
- [ ] No recovered evidence is being relabelled as new/current prose.
- [ ] No private, locked, credential, or personal material is present.
- [ ] Required validators and review receipts are current.
- [ ] The share does not imply a C56/C61 or public-StoryOS authorization.
