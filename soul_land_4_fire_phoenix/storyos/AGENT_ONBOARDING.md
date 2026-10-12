# StoryOS — Agent Onboarding Contract

You are **taking over an existing StoryOS project, not starting a new story.**
Read this file first, then `foundation/STATUS_PANEL.md`, then `foundation/NO_MISTAKE_LIVE_RULES.md`.

## Phase 0 — before you write a word
Run the pre-draft gate. Do not skip it because the task "looks small".

```bash
python3 tools/storyos_validate.py --project . --phase pre
```
- `GATE: clear` → proceed.
- `errors=N` → **stop**, report each error, do not draft.

## LOAD → VERIFY → MAP
1. **LOAD** `foundation/CURRENT_STATE_MANIFEST.json` (schema `storyos-manifest/3`).
2. **VERIFY** it against `foundation/STATUS_PANEL.md` and the newest `audits/*` receipt.
   Newest dated receipt on the **active** branch wins.
3. **MAP** and state, in writing: **confirmed / missing / must reconstruct.**
   Do not present inferred material as confirmed.

## Authority order (high → low)
1. `foundation/STATUS_PANEL.md` — live state
2. `foundation/NO_MISTAKE_LIVE_RULES.md` — hard constraints (R01–R24)
3. `foundation/CANON_SOURCE_NUMBERING_MAP.md` — source boundary
4. `foundation/canon/locks/*.card.md` — user-locked decisions
5. `foundation/canon/characters/*.card.md` — per-character locked state
6. `codex/` — relationships, firewalls, butterfly effects
7. `canon_coverage/` — what each chapter actually consumed
8. newest dated `audits/` receipt for the live edge
9. everything else — **historical evidence only**

## Hard prohibitions
- Do not read a `quarantined-superseded` chapter as canon. It records a rejection.
- Do not continue from a receipt that claims a further edge than `edge.fic_chapter`.
- Do not let author knowledge become character knowledge.
- Do not nerf or inflate to force the OC plot; locked power floors are binding.
- Do not invent ceremonies, items, or reveals to justify consequences.
- Do not overwrite canon, locks, or firewalls without explicit user authorization.
- Do not present prose until `--phase post` passes on it.

## If you find a contradiction
Report it, cite both sources and their dates, propose the minimal correction, and wait.
A silent "fix" is how drift survives a handoff.

## After any accepted chapter
```bash
python3 scripts/scan_project.py <corpus_dir> .
python3 scripts/gen_docs.py
python3 scripts/build_site.py . site
python3 tools/storyos_validate.py --project . --phase full
```
The manifest, panel, ledgers, and control centre are **generated** — never hand-maintained.
