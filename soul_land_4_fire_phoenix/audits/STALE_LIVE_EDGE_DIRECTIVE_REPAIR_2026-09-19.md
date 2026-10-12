# Stale Live-Edge Directive Repair — 2026-09-19

Type: repair + validator hardening
Scope: active tree (`foundation/`, `bible/`, `canon_coverage/`), `tools/`
Live edge before and after: **Chapter51 `The Cost of Quiet`** (unchanged)
Canon consumed: Chapter176 `Be harder on yourself` (unchanged)
Validator before: `PERFECT_CONTINUATION_SKILL_CHECK_V2: PASS`, `active_stale_issues=0`
Validator after: `PERFECT_CONTINUATION_SKILL_CHECK_V2: PASS`, `active_stale_issues=0`
Independent drift scan after: `0 findings / 165 active files`

No chapter prose, character value, lock, firewall or learned rule was altered. Only
stale *live-edge directives* were corrected, and the validator was taught to see them.

---

## 1. The defect

Eight active-tree files asserted a current live edge other than Chapter51, while the
project's own validator reported `active_stale_issues=0`.

| File | Line | Claimed | Truth |
|---|---|---|---|
| `bible/YAN_SHUOER_IDENTITY_AND_APPEARANCE.md` | 182 | after Chapter33 | after Chapter51 |
| `bible/PROTAGONIST.md` | 86 | after Chapter34 | after Chapter51 |
| `bible/PROTAGONIST.md` | 98 | after Chapter35 | after Chapter51 |
| `canon_coverage/Phoenix_Dragon_Canon_Dossier.md` | 1 | `CURRENT OVERRIDE after Chapter35` | after Chapter51 |
| `bible/ADAPTATION_TALENT_LOCAL.md` | 129 | after Chapter49 | after Chapter51 |
| `bible/FIRST_RING_ACQUISITION.md` | 99 | after Chapter49 | after Chapter51 |
| `foundation/DAWNFLAME_FORM_AND_SOUL_SPIRIT_FUSION_RULES.md` | 143 | after Chapter49 | after Chapter51 |
| `foundation/FIRE_LIGHT_ATTRIBUTE_LOCK.md` | 103 | after Chapter49 | after Chapter51 |
| `foundation/PRECISION_AND_GROWTH_LOCKS.md` | 109 | after Chapter49 | after Chapter51 |

`Phoenix_Dragon_Canon_Dossier.md` was the most dangerous: line 1 was a
`> CURRENT OVERRIDE after Chapter35:` block carrying superseded power values
(Yan Rank34/SP689, Dawnflame Phoenix Kite 2,800, Dawn-Iron Phoenix Roc 3,600, Purple Flame
Eidolon Bird 6,000, Song Rank23/SP122, Luo Rank22/SP150), while line 3 of the same file
said it "is a support receipt, not the current live-status source". An override and a
disclaimer in one header.

A ninth file, `SOUL_LAND_4_FIRE_PHOENIX_NEXT_STEPS_FOR_CONTINUATION.md`, sits at the
*workspace root* — outside this project directory — and claimed "Live edge: after
Chapter35" plus "Before Chapter36". No per-project scan can reach it. Repaired separately
in the `soul-land-universal-kit` repository, which is where it lives.

## 2. Why the validator missed all of them

Three independent causes, each verified by replaying the validator's own logic:

**(a) `allowed_historical()` exempts by filename + 4 lines of context + the line.**
`bible/PROTAGONIST.md:86` reads:

> After Chapter32, Yan Shuo'er/public Yan Shuo was Rank29/SP392 … At that historical point,
> the Purple Flame Eidolon Bird had not yet been fused. **Current live edge is after
> Chapter34**, with cocoon day twenty-one underway.

The word "historical" appears three sentences *before* the stale claim, on the same line,
so the whole line was exempted. Every one of the eight files was hidden this way.

**(b) Neither built-in live-edge regex matches these phrasings.**
`Live edge:[^\n]*Chapter(\d+)` requires a literal colon, so `Live edge is after ChapterNN`
never matched. `Current(?:-| )?(?:controlling state |status |scene |values |valid
measurements |state rule )?after Chapter(\d+)` allows only those six prefixes, so
`Current live edge is after ChapterNN` never matched.

**(c) `canon_coverage/` was not in `active_markdown_dirs`.**

## 3. The fix — and why it is in the tool, not the manifest

`active_stale_regexes` are **absolute**: `check_active_files` does
`if regex.search(line): add(issues, …)` with no comparison against `state.latest_fic`. Only
`dynamic_stale_checks_for_line()` compares numbers.

A manifest regex therefore cannot express "chapter ≠ current". This was tested, not
assumed: adding
`Live edge:\s*\**\s*after Chapter(\d+)` to `active_stale_regexes` produced **73 issues, 48
of them false positives** — it flagged all 48 *correct* `Live edge: **after Chapter51**`
headers in `foundation/`. That manifest change was reverted.

Adding `canon_coverage` to `active_markdown_dirs` was also tested and rejected: it surfaces
roughly 20 false positives from per-chapter coverage receipts (`Canon_Coverage_Chapter_41.md`
legitimately says "next chapter should cover Chapter159"), because that mechanism has no
per-chapter exemption. Note the validator already special-cases `foundation/CANON_LEDGER.md`
for exactly this class of false positive.

So the fix went into `tools/perfect_continuation_skill_check.py` as a new
**directive class**, checked *before* the historical exemption:

- `LIVE_EDGE_DIRECTIVE_REGEXES` — four phrasings: `Live edge: [after] ChapterNN`,
  `live edge is after ChapterNN`, `Current live edge is after ChapterNN`,
  `CURRENT OVERRIDE after ChapterNN`
- `live_edge_directive_problems()` — compares the claimed chapter to `state.latest_fic`,
  exempts a file whose own name carries that chapter number (per-chapter receipt), and
  deduplicates so one sentence is not reported twice
- Rationale: a directive tells the reader what is true **now**. It cannot be made historical
  by an adjacent clause, so the exemption must not apply to it. Historical *values* remain
  exempt exactly as before.

Because it compares against `state.latest_fic`, it needs **no regeneration when the edge
moves** — unlike `active_stale_regexes`, several of which hard-code Chapter52/53/176.

## 4. Content repairs

Historical text was preserved; only the stale directive was corrected. Example
(`bible/PROTAGONIST.md:86`):

```
- At that historical point, … Current live edge is after Chapter34, with cocoon day
- twenty-one underway.
+ At that historical point, … Current live edge is after Chapter51 `The Cost of Quiet`;
+ the cocoon day twenty-one state described above is historical. Use
+ `foundation/STATUS_PANEL.md`.
```

`Phoenix_Dragon_Canon_Dossier.md` line 1 was relabelled from `CURRENT OVERRIDE` to
`HISTORICAL SUPERSEDED OVERRIDE (as of Chapter35) — NOT CURRENT`, with every superseded
value named as superseded and a pointer to `STATUS_PANEL.md` and
`CURRENT_STATE_MANIFEST.json`. The historical values were kept, not deleted, per the
standing rule *archive/mark, don't erase*.

## 5. Regression tests

Run against the patched validator, then the probe file was deleted:

| Probe | Expected | Result |
|---|---|---|
| stale directive behind historical wording (the original bug) | FAIL | **FAIL, 1 issue, correct line** |
| `Live edge: **after Chapter35, …**` | FAIL | **FAIL, 2 issues** (new rule + existing built-in) |
| `> CURRENT OVERRIDE after Chapter35:` | FAIL | **FAIL, 1 issue** |
| control: `Live edge: **after Chapter51**` + `Current live edge is after Chapter51` | PASS | **PASS, 0 issues** |

The control matters: `active_stale_issues=0` was also the *buggy* answer, so a PASS alone
proved nothing. The validator now fails on stale directives and still passes on correct ones.

## 6. Changed files

```
bible/ADAPTATION_TALENT_LOCAL.md                          | 2 +-
bible/FIRST_RING_ACQUISITION.md                           | 2 +-
bible/PROTAGONIST.md                                      | 4 +-
bible/YAN_SHUOER_IDENTITY_AND_APPEARANCE.md               | 2 +-
canon_coverage/Phoenix_Dragon_Canon_Dossier.md            | 2 +-
foundation/DAWNFLAME_FORM_AND_SOUL_SPIRIT_FUSION_RULES.md | 2 +-
foundation/FIRE_LIGHT_ATTRIBUTE_LOCK.md                   | 2 +-
foundation/PRECISION_AND_GROWTH_LOCKS.md                  | 2 +-
tools/perfect_continuation_skill_check.py                 | 52 ++++++++++++++++
```

`foundation/CURRENT_STATE_MANIFEST.json` is **unchanged** — the tested manifest approach
was reverted. No prose, lock, firewall, character value or learned rule was touched.

## 7. Still open

- The three stale copies of this project elsewhere in the GitHub account
  (`soul-land-universal-kit/soul_land_4_fire_phoenix/`,
  `soul-land-universal-kit/sl4_fire_phoenix/`, and
  `soul-land-projects/sl4_fire_phoenix/soul_land_4_fire_phoenix/`) stop at Chapter31.
  Being archived and marked, not deleted.
- Source Chapter177 `1,000-year Purple Zoysia` is still absent, so Chapter52 remains
  blocked. Reported missing, not invented.
