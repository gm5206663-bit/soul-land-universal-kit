# Soul Land II — Dragon and Phoenix

**Working title · foundation stage · no chapter published.**
Fanfiction by **Gaurav Meena**. Unofficial, non-commercial Soul Land fan work.

A native boy born to Yan Shaozhe and Cai Mei’er grows up within Shrek’s circle
with Bright Phoenix and Evil-Dispelling Dragon Soul Spear martial souls,
dragon–phoenix inheritance, and Adaptation Talent present from conception.
He first meets Huo Yuhao alongside Tang Ya and Bei Bei—not as an old childhood
friend. His place in the world must have real consequences without replacing
the source characters with an audience for his greatness.

**Working protagonist name:** Yan Jingheng (言景衡), selected under the author’s
“you give” naming delegation. The book title is an agent working title, not an
author-quoted title. Both can be revised without rewriting a supposed ruling.

## Read in this order

1. [Foundation](foundation/FOUNDATION.md): the premise and its authority boundaries.
2. [Character](foundation/CHARACTER.md) and [relationships](foundation/RELATIONSHIPS.md).
3. [Adaptation Talent module](foundation/ADAPTATION_MODULE.md).
4. [Opening-state review](foundation/OPENING_STATE_REVIEW.md): derive strength, do not guess it.
5. [Source crosswalk](foundation/SOURCE_CROSSWALK.md) and [first chapter plan](canon_coverage/CHAPTER_001_PLAN.md).
6. [Status](STATUS.md), [remaining work](foundation/OPEN_WORK.md), [agent handoff](HANDOFF.md).

## What this foundation does

- Records the author’s exact words and selected choices in [the rulings ledger](foundation/AUTHOR_RULINGS.json).
- Separates current state, design proposals, source receipts and future possibilities.
- Establishes the martial souls, bloodlines, resource logic, combat/engineering
  disciplines, prenatal development, family relationships and knowledge boundaries.
- Uses the novel as the narrative spine and tracks the manhua and donghua separately.
- Explicitly adopts Cai Mei’er’s donghua spear design without calling it a named novel martial soul.
- Preserves the strong starting advantages. High energy demand is not an excuse to
  erase adaptive efficiency, resources, good teaching or accumulated growth.
- Supplies a technical gate and tested failure cases. A passing foundation check
  does not mean the unfinished opening state is ready for prose.

## Not falsely settled

Exact opening cultivation, ring donors/ages, engineered equipment, combat feats
and engineer certification still require a supported development ledger. There
are no invented live numbers. The opening evaluation compares strong-development
scenarios; it is not a ceiling or an accepted power panel.

Official novel opening parts 1.1–1.4 have been read. The official manhua catalog
and donghua Episode 1 listing have been located. Their panels, scene ranges and
timestamps have **not** been reviewed, so they are not listed as consumed.
The [source receipt register](research/SOURCE_RECEIPTS.json) states these limits.

## Checks — Python standard library only

```sh
cd soul_land_2_dragon_phoenix
python3 tools/manage.py build
python3 tools/manage.py verify
python3 -m unittest discover -s tools -p 'test_*.py' -v
python3 tools/manage.py ready
```

`ready` deliberately exits **2** while research blockers remain. Never change a
blocked chapter to “ready” merely to obtain a green badge. The [CI workflow](../.github/workflows/dragon-phoenix-foundation.yml)
checks structural integrity and verifies this expected readiness refusal.

No pictures, videos, audio, generated covers or media packages belong in this
project. The rejected Fire Phoenix assets were removed and are not a reference.

[File map](CODEX.md) · [Writing rules](foundation/WRITING_RULES.md) · [Rights notice](NOTICE.md)
