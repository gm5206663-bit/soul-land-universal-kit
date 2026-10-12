# NO_MISTAKE_LIVE_RULES — universal canon discipline

Generated 2026-09-21. Rules carry stable IDs so an agent can cite *why* it refused a beat.
Any rule below was created by a real failure the user already rejected once.

## Core operating rules
- **R01** The control centre / status panel is a *mirror* of project state, never an authority over it.
- **R02** Do not treat author knowledge as character knowledge.
- **R03** Do not invent missing canon. If a source scene is absent, name it missing.
- **R04** Preserve established decisions unless the user explicitly authorizes change.
- **R05** Never leak rejected drafts into active canon.

## Canon and butterfly
- **R06** Canon-first. Butterfly effects must grow from actual changed events.
- **R07** One canon episode = one operational unit of *consequence*, not of word count.
- **R08** Do not invent formal reward ceremonies or items just to prove a butterfly consequence.

## Information discipline
- **R09** Track every fact as KNOWN / SUSPECTED / UNKNOWN / FALSE BELIEF / KNOWN PARTLY / DISBELIEF / HIDDEN.
- **R10** Never convert suspicion, intuition, rumour, prophecy fragments, or author knowledge into factual character knowledge without on-page evidence.
- **R11** Do not give a character information earlier than the earliest valid change recorded in their firewall entry.
- **R12** Secrets between bonded characters are safety boundaries imposed by adults or circumstance — not evidence of distrust.

## Power discipline
- **R13** Do not nerf or inflate a character to force the OC plot.
- **R14** Where a baseline/floor is locked, count the full established foundation before ranking anyone below it.
- **R15** Do not use in-world excuses (admin, scanner, records) to hide a strength hierarchy the reader can see.
- **R16** Adaptation-type personal frameworks are innate, non-conscious, existence-level law — never a UI, voice, companion, reward system, or generic learning mechanic. They cannot create power from nothing or bypass setting rules.

## Craft and pacing
- **R17** Preserve competent canon characterization.
- **R18** Compress routine source beats; expand only meaningful character / system / butterfly / relationship / tactical change.
- **R19** Do not replace detailed codex files with short summaries. Add a summary file; never overwrite detail.
- **R20** After any rejection, repair the *direction*, then re-derive state — do not continue as if unnotified.

## Process gates
- **R21** Pre-draft gate is mandatory: LOAD → VERIFY → MAP, then state confirmed / missing / must-reconstruct **before** prose.
- **R22** `storyos_validate.py --phase pre` must report no errors before blueprinting.
- **R23** `storyos_validate.py --phase post --files <new chapter>` must pass before presenting.
- **R24** Record new decisions and corrections as lock cards so they cannot regress later.

## Continuation protocol
1. Re-scan state: `python3 scripts/scan_project.py <corpus> .`
2. Read `foundation/STATUS_PANEL.md`, then this file, then the relevant `codex/` files.
3. Run `--phase pre`. Resolve every `error`.
4. Write coverage file for the new chapter **before** prose.
5. Draft using R18 pacing, obeying R09–R13.
6. Run `--phase post --files chapters/Chapter_N.md`.
7. Re-scan, re-render docs, rebuild the control centre, record the receipt.
