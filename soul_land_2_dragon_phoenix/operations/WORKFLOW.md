# Working and publication procedure

## One owner, readable views

[FILE_REQUIREMENTS.json](FILE_REQUIREMENTS.json) assigns practical story functions
to subject documents and drives the reading guide. State, source receipts and
exact author rulings are separate owners. README is the front door; the generated
opening dossier is a readable view of current values, not another stat panel.
Historical audits belong in records and never override current state.

The latest author words outrank all files. A supported delegated design can
establish off-page fiction history; it cannot become a fabricated author quote,
a primary canon claim or a published scene. The Talent master remains external
law. Other serials’ figures, illness, UI and current states do not cross over.

## Which record to update

| Record in `state/` | Responsibility |
|---|---|
| CURRENT_STATE.json | Accepted present facts and readiness work; exact current values |
| TIMELINE.json | Relative event order and shared opening anchor |
| development_events.json | Original off-page causal milestones and state outputs |
| adaptation_events.json | Actual adaptive input, response, cost and integration |
| resource_events.json | Provision, supplier, purpose and resulting work |
| continuity_events.json | Only events actually written in fic scenes; currently empty |
| ring_candidates.json | Unaccepted future donor research, never automatic live rings |
| design_proposals.json | Deferred/rejected designs, not a second current build |
| FILE_MANIFEST.json | Generated inventory; do not maintain manually |

`canon/SOURCE_RECEIPTS.json` owns exact source evidence. Author wording belongs in
`operations/AUTHOR_RULINGS.json`. Dated migration/audit records describe their own
moment; they do not silently replace any of these owners.

## Before a chapter

1. Read current state, author rulings, open work and the scene’s subject owners.
2. Review actual source bodies/visual units and record edition, units and limits.
3. Check changed causes, private knowledge, chronology, ownership and witnesses.
4. Choose scene start/end, POV, place, participants and the change that matters.
5. Run the genuine readiness gate. No chapter while blockers remain.

## During and after writing

Write original prose, not a pasted translation. Show relevant background through
present action. Keep children age-appropriate and people independently motivated.
Measure local style targets, then read for naturalness, repetition, agency and
source logic. Mechanical success does not certify literary quality.

Record actual continuity, consumed resources, knowledge, injury, learning and
relationship changes. Update the one live state and regenerate views. No
in-prose system window is adopted; relevant measurements can appear naturally.
A display must distinguish owned item/design, craft/certificate and burst/sustained feat.

## Checks and publication

```sh
python3 tools/manage.py build
python3 tools/manage.py report
bash checks/run_all.sh
python3 tools/manage.py ready
```

`ready` exits two for genuine unresolved prerequisites and zero when resolved;
invalid data fails separately. Synthetic tests exercise both paths without claiming
real visual review. The present foundation-only lifecycle still rejects chapter
files/counts; a future authorized writing phase needs its explicit production
gates, not ad-hoc removal of protections.

Review a scoped diff, preserve unrelated work, commit, fetch/rebase and push
normally. No force-push. Public records must match actual shipped content. Keep
the rights notice. Do not touch Golden Lion or another serial’s files.

## Defects and history

Record a real defect’s date, affected owners, cause, correction, regression and
remaining uncertainty. Common failures to catch include empty heading coverage,
file counts mistaken for readiness, fake visual claims, weak-child resets,
ancestral secret teaching, private-history leakage and quietly decided romance.
Do not recreate deleted image-search or rejected media. Superseded subject texts
remain in the named public baseline commit, with a consolidation map in records;
keeping a second live copy would recreate the same ownership problem.
