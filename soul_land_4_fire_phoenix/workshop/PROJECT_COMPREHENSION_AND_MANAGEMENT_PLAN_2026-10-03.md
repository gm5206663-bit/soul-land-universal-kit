# Fire Phoenix Project — Comprehension and Management Plan

**Date:** 2026-10-03  
**Status:** current project-control assessment before local Git acceptance.  
**Authority:** the author’s current instruction to understand the entire project first, followed by selection of local acceptance for the Option A contiguous V2 staging candidate.

## 1. What this project is

This workspace is a **provenance-preserving fiction workshop**, not a single ordinary manuscript folder.

| Layer | Role | Current status |
|---|---|---|
| `sources/` | Recovered public evidence: StoryOS public layer, Chapter-51 managed snapshot, related public source maps, and archives. | Immutable/recovery baseline; 1,115 files verified against public Git blob SHA values. |
| `provenance/` | Recovery manifest, file index, freshness/recovery records. | Integrity evidence; do not rewrite as though it were current fiction. |
| `semantic_audit/` | Claim-level source audit, source-learning diagnosis, authorizations, source fences, craft analysis. | Evidence and policy layer. |
| `late_arc_rebuild/drafts/`, `contracts/`, `audit/` | Frozen V1 C48–C60 author-review line and its historical receipts. | Preserved historical evidence; not the current craft line. |
| `late_arc_rebuild/rebuild_v2/` | Corrected eight-unit structural rebuild, line audit, claim audit, and promotion package. | Current creative candidate. |
| `continuation_preparation/` | Earlier Chapter-53 preparation and rejected Dorm333-only work. | Historical/quarantined; never a continuation base. |
| `research/` | Source and official-adaptation access research. | Evidence only; no unviewed adaptation conclusions. |
| `tools/` | Recovery and historical validators. | Some tools validate the recovered public baseline; others validate frozen V1. They remain useful but cannot by themselves certify V2 promotion. |

## 2. Verified integrity and working facts

- Public recovery validates: **1,115 / 1,115** files and **18,725,735** bytes match the recorded public Git blobs.
- Current recovered public StoryOS prose ends at Chapter 52, _Amiable Beasts_. It remains preserved evidence.
- The prior public C48–C52 and frozen V1 late-rebuild line are **not deleted**.
- No native private repository is locally available; no private credentials or claim of private-source access exists.
- No Git repository, Git remote, GitHub CLI authentication, GitHub workflow, credential file, or tracked secret was present at the start of this management phase.
- The project footprint is approximately 25 MB; no file exceeds GitHub’s normal 100 MB limit; no live secret signature was found in authored/control directories.

## 3. Current creative decision

The author selected:

> **Local acceptance of the Option A contiguous public C48–C55 V2 candidate, without public-layer application or GitHub push.**

The underlying approved candidate is the eight-unit V2 line:

| Reader-facing accepted sequence | Protected V2 source | Function |
|---|---|---|
| C48 — _The Line We Keep_ | V2 C48 | Yin’s warning, Dorm336 debrief, Lucky Wheel doorway. |
| C49 — _What They Carry_ | V2 C49 | Correct Lucky Wheel rewards, Liu’s fusion, real Dorm336 preparation. |
| C50 — _Two Maps of the Forest_ | V2 C50 | Separate random-transfer forest routes with a material Dorm336 cost. |
| C51 — _The Cost of Quiet_ | V2 C51 | Qian’s priced-risk turn and visibility/formation consequence. |
| C52 — _What the Ground Keeps_ | V2 C52 | Consolidated ape/bear/Zoysia causal movement; held-Zoysia condition. |
| C53 — _What a Favor Costs_ | V2 C54 | Leopard action, skull-fusion instability, autonomous ape departure. |
| C54 — _What We Leave Open_ | V2 C55 | Ye’s independent exit and Dorm336’s compromised channel. |
| C55 — _The Price of Keeping_ | V2 C60 | Consolidated late consequence: plant trap, ape self-departure, public exposure cost. |

This is intentionally **not** a public C48–C60 direct copy. V2’s internal C52/C53 and C56–C60 consolidation must remain visible in the provenance map rather than being undone by filler chapters.

## 4. Active authority order after local acceptance

1. Current direct author instruction in this conversation.
2. The dated local acceptance record and accepted C48–C55 layer created from the selected Option A staging candidate.
3. `late_arc_rebuild/rebuild_v2/` claim audit, line pass, rebuild map, and protected source units.
4. `semantic_audit/C48_C60_COMPLETE_CLAIM_LEVEL_SOURCE_AUDIT_2026-10-01.md` and `C48_C60_SOURCE_LEARNING_AND_DRAFT_DIAGNOSIS_2026-10-01.md`.
5. Recovered public StoryOS C1–C52/state/gate as preserved baseline evidence, never silently overwritten.
6. Frozen V1 late-rebuild line, historical validators, continuation preparation, and archives as labelled history.

## 5. Non-negotiable story controls

- No C61, future source endgame, or implied next-chapter allocation.
- Purple Zoysia remains held under the six-day AU condition; source-timing handover is not restored.
- The Gold Silk Ape remains unstable, autonomous, untracked, uncommanded, and not a pet/scout/weapon.
- Qian has only deliberate, immediate, bounded ape contact in the stated V2 scenes; no passive tether, remote feed, tracking, or human radar.
- Liu has one bounded C52 Silver Edge finish; no mastery/repeat shortcut.
- Yan has no future ring, external bone, later Phoenix state, Domain, Nirvana, armor, or identity disclosure.
- Song/Luo have no invented skills, rings, bones, equipment, or super-senses.
- Ye stays independent; no merger, debt, confession, romance payoff, or private-identity disclosure.
- No manhua/donghua conclusion is treated as fact without directly viewed lawful panels/scenes.

## 6. Management decision

Because the workspace has no Git history or remote, the safe GitHub-ready structure is:

1. initialize a **local** Git repository only;
2. preserve all recovered sources and provenance in the first commit;
3. create a dated local accepted replacement layer rather than mutating the recovered public source layer;
4. add a V2-aware validation workflow alongside, never in place of, recovery validation;
5. create GitHub-ready documentation and CI configuration;
6. make local commits only;
7. do not add a remote or push until the author supplies/authorizes a GitHub destination and explicitly requests a push.

## 7. Required validation set

| Check | Purpose |
|---|---|
| `tools/verify_public_recovery.py` | Confirms recovered public evidence remains byte/SHA verified. |
| `tools/validate_workshop.py` | Confirms the Chapter-52 public baseline and historical recovery layout remain intact. |
| `tools/validate_replacement_line_48_60.py` | Confirms frozen V1 historical package integrity and labels it historical; does not certify V2. |
| `tools/validate_current_v2_line.py` | Confirms the eight protected V2 units, current local-control artifacts, core mechanics, and no-C61/future fences. |
| `late_arc_rebuild/rebuild_v2/promotion_proposal_2026-10-03/staging_option_A_contiguous_public_C48_C55/validate_option_a_staging.py` | Confirms selected contiguous staging, source hashes, old-public hashes, fences, and no C61. |
| `tools/validate_local_accepted_v2_release.py` | Confirms the accepted local layer matches staging, its manifest hashes, preserved public baseline, and non-public boundary. |

## 8. Explicit external-GitHub boundary

GitHub CLI is not installed/authenticated and no remote exists. No push, GitHub-repository creation, issue, PR, release, or remote configuration can occur safely without an author-supplied destination or later explicit authorization.
