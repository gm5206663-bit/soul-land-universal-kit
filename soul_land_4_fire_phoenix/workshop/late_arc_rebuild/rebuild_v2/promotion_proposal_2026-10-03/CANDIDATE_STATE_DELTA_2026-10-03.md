# Candidate State Delta — V2 Promotion Proposal

**Status:** descriptive candidate delta only. It is not a replacement `state.json` or `state.txt`.  
**Date:** 2026-10-03.

## 1. Baseline versus candidate edge

| Field | Current recovered public state | V2 candidate state if promotion is approved |
|---|---|---|
| Public edge | After C52, _Amiable Beasts_ | After the final V2 causal unit; public number depends on the author’s numbering decision. Under Option A: after public C55, _The Price of Keeping_. |
| Current source framing | Chapter-177 Zoysia setup; next source listed as 178 | Direct novel spine used selectively through the ape/leopard/skull-fusion pressure, with a limited late-C182/C183 human-flight pressure. No automatic numeric `canon_consumed` value should be asserted because V2 is a partial-source, AU reconstruction rather than a transcript. |
| Purple Zoysia | Rooted under the Palm Tree Bear; no deal formed | Held by Dorm333 under an active six-day AU condition; its root ball remains viable but has been stressed and its existence is now known to hostile contestants. |
| Gold Silk Ape | Wounded/alive in the public Chapter-52 setup | Wounded, skull-fusion-unstable, self-directed, and departed by its own choice. No pet/scout/ally/tracker role. |
| Palm Tree Bear | Wounded/alive | Defeated in V2 C52’s source-supported finishing movement. No exact public score is stated. |
| C61 | No authorization | Still no authorization, title, allocation, prose, or implied continuation outcome. |

## 2. Character-state delta

### States that remain locked / unchanged

- **Lan Xuanyu:** Rank 20 / SP505 / Spirit Sea; current Blue Silver Grass state; no Platform entry/use.
- **Qian Lei:** no purple-ring jump, no declared exact ring-age result, no current Spirit Sea claim, no passive beast/human sensing utility.
- **Liu Feng:** Rank-29-adjacent/right-arm-bone state remains; only one C52 Silver Edge finish; no mastery or repeat solution.
- **Yan Shuo:** Rank 39 / SP962 / Spirit Sea / three purple rings / public Yan Shuo identity; no future Phoenix state, fourth ring, external bone, domain, Nirvana, armor, or disclosure.
- **Song Yichen / Luo Haoran:** no invented ring, skill, equipment, bone, or supernatural-sensing fact.
- **Ye Lingtong:** no confession, debt, team merger, romance progression, or Yan Shuo’er knowledge.

### Candidate operational state after final V2 unit

| Character/group | Candidate end state |
|---|---|
| Dorm333 — Lan, Qian, Liu | Still in the assessment forest; carrying the held plant; Qian has recently exhausted a Ground Fire Dragon Lizard summon; Liu has a shallow cord injury to his forearm; no exact score result is claimed. |
| Dorm336 — Yan, Song, Luo | Still separate from Dorm333; their channel/formation has been observed by hostile contestants; Song’s shield has a fresh lower-rim crack; no score, prey kill, alliance, or reunion is claimed. |
| Ye | On her chosen lower-wash route after a bounded exit, still separate from both dorms. Her prior Dorm333 teammates are not declared found, safe, lost, or merged. |
| Gold Silk Ape | Has left visually and autonomously; condition remains held by Dorm333; no tracking, future promise, recovery, or return is claimed. |
| Unnamed contestant groups | Have learned that the Purple Zoysia exists and that the group carrying it can resist a first trap; no names, ranks, score, defeat, alliance, or future appearance is claimed. |

## 3. State-file design requirements if promotion is approved

A later state migration must **not** mechanically edit the old `state.json`. It needs a new dated candidate state built from the approved public numbering. That state must:

1. retain the recovery provenance of the existing Chapter-52 public layer;
2. record a `replacement_line` / `internal_v2_map` rather than pretending V2 C54/C55/C60 are public file labels;
3. use a partial-source/AU coverage field instead of blindly setting a single source-consumption integer;
4. explicitly retain all no-currentization locks listed above;
5. record the Zoysia term, plant condition, ape autonomy, Ye’s independent route, and Dorm336’s observed formation consequence;
6. mark every prior Chapter-53 continuation candidate as superseded rather than deleted;
7. state that the next prose allocation remains **unapproved**.

## 4. Explicitly excluded state claims

Do not add any of the following in a candidate public state:

- a completed six-day term or early Zoysia handover;
- an ape alliance, command bond, scout feed, emotional tether, or recovery;
- a named contestant identity or downstream score outcome;
- an exact new Qian ring age, purple breakthrough, Platform result, or repeated Silver Edge success;
- a public Yan identity change or future power;
- any C61 next-step content.
