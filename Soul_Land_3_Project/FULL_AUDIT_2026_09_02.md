# FULL WORKSPACE AUDIT — 2026-09-02

**Mandate (the user):** *"There is too many mistakes, please check everything carefully slowly every word every line every file please everything."*
**Method:** machine sweep of every file class (cross-file numbers, arithmetic, structure, staleness, typography), then careful re-reads of the surfaces machines cannot judge (ch86–92 dialogue and prose). **8 real defects found and fixed; 6 verification layers now green; the largest defect class is now machine-banned.**

---

## Scope — every file class, checked

| Class | Count | Checks applied |
|---|---|---|
| chapters/ | 92 | footer vs state.json (ALL history, rank/SP/hawk/ledger) · trial arithmetic · Layer 4 zero-tolerance · Layer 5 presence · grammar spot-read ch86–92 · soft hyphens · banned phrases |
| checks/ | 7 scripts | all executed; board re-derived truthfully |
| canon_extract/ | 49 chapter files + index + slug map | contiguity 229–275 (isolated: 28, 218 — by design) · range claims vs disk · numbering-map NEXT vs disk · source-typo normalization (Gue→Gu checked; none present) |
| Live docs (9 + mirror) | STATUS · PANELS · STATS · CODEX ×2 · PROMPT · POWER_MODEL · CANON_ACCESS · REGISTRY | live-block uniqueness · vector arithmetic · range/NEXT freshness · debt-list freshness |
| library/ | 86 files | dispositions (LESSONS_ABSORBED) · no stale claims about deleted uploads |
| archive/ | 1 + README | frozen by policy (history, not live truth) |
| state.json | 92 keys | every key vs its chapter footer |

## The 8 real defects found — and fixed

1. **LIN_HAO_STATUS ghost line (worst):** a stale duplicate "Current soul rank… = 70" survived five syncs — my chapter-sync *inserted* a new position block but never removed the old one, and later blanket number-replacements kept refreshing its surface so it looked alive. **Fixed:** the position section now holds exactly one header + one line.
2. **Four stacked "current" lines:** the same insert-without-delete bug left four more orphan "Current soul rank" lines (ch88–ch91 eras, all claiming 2,918). **Fixed:** all removed; one truth remains.
3. **CANON_ACCESS stale range:** said 229–268 while disk holds 229–275 — five syncs' range-updates silently missed (the search string had already drifted). **Fixed:** 229–275.
4. **CANON_ACCESS stale numbering-map NEXT:** said "NEXT canon 270" (next is 276 = ID 10716121). My first fix attempt no-op'd (replace without assert). **Fixed with assertion.**
5. **CONTINUATION_PROMPT stale debt:** playfulness listed as owed — PAID in ch87. **Fixed.**
6. **PREWRITE_MANIFEST stale debt:** same. **Fixed.**
7. **library/INDEX.md stale claim:** "originals untouched in uploads/" — uploads were deleted 09-02 after hash-verified absorption. **Fixed.**
8. **ch90 soft hyphen:** "stiflened" carried an invisible U+00AD typing artifact. **Fixed** → "stifled".

## The new machinery (so this class of rot cannot return silently)

**Layer 6 — `checks/workspace_audit.py`** (wired into run_all; caught defect #4 live during this audit):
state-vs-ALL-footers · trial-vector sums in every live doc · CANON_ACCESS range + NEXT-map vs actual disk · **live-block uniqueness (the ghost-duplicate guard)** · soft-hyphen ban · hygiene (DOULOLO / deleted-uploads claims). The suite is now **six layers**: locks → canon-locks → sync → zero-tolerance → presence → workspace.

## Verification (end state)

- `run_all`: **exit 0** — all six layers green.
- Board: all eight defect-scan categories ✅; working set 229–275; NEXT canon 276 (expected title printed from the index).
- Dialogue spot-read ch86–92: attributions track; no crossed names; no broken quotes.
- Doubled-word scan of all chapters: only legitimate English ("had had", "that that") and the name "Xie Xie".

## Honest exclusions

- `archive/` is frozen history — its old numbers are period-accurate and marked as archive.
- The registry intentionally retains superseded entries (with supersession notes) — the project does not burn its history.
- Canon extracts quote the source faithfully, including its own typos where marked; we normalize only names we transcribe.
- My first audit regex produced ~5,100 false positives (it flagged the surname doubling in "Xie Xie") — recorded here as the lesson: **a noisy check hides real defects; precision first.**
