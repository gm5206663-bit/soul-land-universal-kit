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

## Complete foundation navigation

Start with the [foundation index](FOUNDATION_INDEX.md): it groups the practical
file set into character, relationships, timeline, setting, powers, continuity,
source research and production. [CODEX.md](CODEX.md) lists every project file.

Expanded relationship dossiers cover [parents](relationships/PARENTS.md),
[elders](relationships/ELDERS.md), [Ma Xiaotao](relationships/MA_XIAOTAO.md),
[the stream party](relationships/STREAM_PARTY.md), and
[ancestry/later contacts](relationships/ANCESTRY_AND_CONTACTS.md).
The [family tree](foundation/FAMILY_TREE.md), [timeline](foundation/TIMELINE.md),
[cast](foundation/CHARACTERS.md), [places](foundation/PLACES.md) and
[continuity guide](foundation/CONTINUITY.md) are separate working owners.

The author-requested `image-search` directory and all eight research pictures
were deleted. They are not copied into this project. GitHub’s existing foundation
patterns were [reviewed](research/GITHUB_FOUNDATION_REVIEW.md) for structure,
not for importing another OC’s powers or history.

## Read in this order

1. [Foundation](foundation/FOUNDATION.md): the premise and its authority boundaries.
2. [Character](foundation/CHARACTER.md) and [relationships](foundation/RELATIONSHIPS.md).
3. [Adaptation Talent module](foundation/ADAPTATION_MODULE.md).
4. [Opening build](OPENING_BUILD.md) and [development derivation](foundation/DEVELOPMENT_DERIVATION.md): an authored causal route, not a canon calculator.
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
  does not mean the chapter’s visual-source prerequisites are resolved.

## Not falsely settled

The [pre-chapter review](audits/PRECHAPTER_REVIEW.md) records the corrections.
The opening build, original donors/skills, actual devices, witnesses and trip now
have an explicitly delegated off-page history. They are author-revisable fiction,
not canon-deduced numbers or a new direct author choice. No numbered engineering
certificate is asserted without its actual rule/test.

Novel parts 1.1–1.4, 2.1–2.4, 9.4 and 10.1–10.2 have been read. The official
manhua reader and donghua EP1 leads were accessed without completed panel/scene
review; the official YouTube source reports a country restriction. No visual
range is fabricated or listed as consumed.
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
checks structural integrity and matches the CLI result to the actual blocker list.
Regression fixtures prove both honest refusal and a genuinely resolved synthetic path.

No pictures, videos, audio, generated covers or media packages belong in this
project. The rejected Fire Phoenix assets were removed and are not a reference.

[File map](CODEX.md) · [Writing rules](foundation/WRITING_RULES.md) · [Rights notice](NOTICE.md)
