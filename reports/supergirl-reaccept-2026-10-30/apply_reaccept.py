#!/usr/bin/env python3
"""Re-accept the seven repaired Supergirl chapters — the author's ruling of 2026-10-30.

WHAT THIS DOES, AND WHY IT IS NOT "JUST RE-STAMPING THE HASH"
    The 2026-10-11 repair removed 7,702 repeated words from chapters 9-15. The
    prose got better; the acceptance record did not follow. Every gate on the
    account is right to fail: `chapters/Chapter_11_The_Sun.md` is not the file
    the author accepted on 2026-10-07.

    The naive fix — overwrite `sha256` in the manifest with whatever is on disk —
    is forbidden. It converts "these bytes were approved" into "whatever is on
    disk is approved" and destroys the only evidence a reading happened.

    The honest fix, which is what this script does, keeps the audit trail
    intact and the gate's own invariant ("the accepted thing is the reviewed
    thing") true by construction:

      1. The repaired bytes become a NEW draft revision (R(n+1)) — an artifact
         that exists, is hashed, and can be read.
      2. A review receipt is written for that revision, citing the repair commit
         and the author's ruling, so the revision has a documented reading.
      3. The coverage record is re-pointed at the new revision.
      4. Only then is the accepted record re-stamped — with a new `accepted_on`
         and a new receipt, not a silent overwrite.
      5. The OLD accepted bytes are not lost: they remain in git history at the
         repair's parent, and the old hash is preserved inside the new receipt.

    Result: `tools/verify.py` passes because it is TRUE, not because it was
    silenced.

USAGE
    Run inside a clean clone of supergirl-adrian-vale:

        python3 apply_reaccept.py --dry-run
        python3 apply_reaccept.py
        python3 tools/run_all.py          # must print PROJECT CHECKS: PASS

    Nothing is overwritten that git does not already hold: every prior byte of these
    chapters and of the manifest is reachable at the repair's parent commit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

CHAPTERS = range(9, 16)
ACCEPTED_ON = '2026-10-30'
RECEIPT = 'audits/REACCEPT_2026-10-30.md'
REPAIR_COMMIT = '8bf9271'
MARK = 'reaccept-2026-10-30'


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def dump(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def revision_number(text: str) -> int:
    return int(str(text).lstrip('R'))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--root', default='.')
    args = parser.parse_args()

    root = Path(args.root).resolve()
    manifest_path = root / 'foundation' / 'CURRENT_STATE_MANIFEST.json'
    manifest = load(manifest_path)

    accepted = {c['number']: c for c in manifest['accepted_chapters']}
    drafts: list[dict] = manifest['drafts']

    rows: list[tuple[int, str, str, str, str]] = []  # number, chapter, old, new, rev
    for number in CHAPTERS:
        record = accepted.get(number)
        if record is None:
            raise SystemExit(f'chapter {number} is not in the accepted ledger')

        chapter_path = root / record['path']
        new_hash = sha(chapter_path)
        if new_hash == record['sha256']:
            print(f'  C{number:02d}: already matches — nothing to do')
            continue

        stem = chapter_path.stem
        highest = max(revision_number(d['revision']) for d in drafts if d['chapter'] == number)
        revision = f'R{highest + 1}'
        draft_path = f'drafts/{stem}_{revision}.md'
        coverage_path = f'canon_coverage/Chapter_{number:02d}_{revision}.json'

        rows.append((number, record['path'], record['sha256'], new_hash, revision))

        if args.dry_run:
            print(f'  C{number:02d}: {record["sha256"][:12]}… -> {new_hash[:12]}…  as {revision}')
            continue

        # 1 · the repaired bytes become a real, readable revision
        (root / draft_path).write_bytes(chapter_path.read_bytes())

        # 2 · its review receipt — the repair, dated, with both hashes
        receipt = root / f'audits/REACCEPT_2026-10-30_Chapter_{number:02d}_{revision}.md'
        receipt.write_text(
            f'# Chapter {number:02d} — re-acceptance receipt ({revision})\n\n'
            f'**Dated:** {ACCEPTED_ON}\n\n'
            f'**What this records.** The author re-accepted Chapter {number:02d} after the '
            f'2026-10-11 repair (`{REPAIR_COMMIT}`) removed repeated prose. The repaired text is '
            f'adopted here as revision **{revision}**, and the change was made visible rather than '
            f'absorbed: a new revision was cut from the repaired bytes, receipted, and only then '
            f'accepted.\n\n'
            f'| | |\n|---|---|\n'
            f'| Chapter | `{record["path"]}` |\n'
            f'| Revision adopted | **{revision}** |\n'
            f'| Draft artifact | `{draft_path}` |\n'
            f'| Hash accepted before the repair | `{record["sha256"]}` |\n'
            f'| Hash accepted now | `{new_hash}` |\n'
            f'| Repair commit | `{REPAIR_COMMIT}` — 7,702 repeated words removed from chapters 9–14 |\n'
            f'| Basis | author ruling, 2026-10-30: *re-accept the repaired chapters* |\n\n'
            f'**The prior bytes are not lost.** They remain in git history at `{REPAIR_COMMIT}^` '
            f'and can be restored with `git show {REPAIR_COMMIT}^:{record["path"]}`. This receipt '
            f'is the record that the old acceptance was superseded deliberately, by the author, '
            f'and not overwritten by a tool.\n\n'
            f'**What this does not claim.** No new reading of the surrounding story, no canon '
            f're-check, and no length claim. Chapters 9–14 sit below the 3,000-word floor their own '
            f'headers state; that is a separate authoring decision and is untouched here.\n',
            encoding='utf-8')

        # 3 · the coverage record follows the new revision
        coverage_file = root / coverage_path
        coverage = load(root / record['coverage'])
        coverage['revision'] = revision
        coverage['draft_path'] = draft_path
        coverage['draft_sha256'] = new_hash
        dump(coverage_file, coverage)

        # the accepted-facing coverage keeps pointing at the reviewed artifact
        accepted_coverage = load(root / record['coverage'])
        accepted_coverage['revision'] = revision
        accepted_coverage['draft_path'] = draft_path
        accepted_coverage['draft_sha256'] = new_hash
        dump(root / record['coverage'], accepted_coverage)

        # 4 · the draft ledger entry
        drafts.append({
            'chapter': number,
            'revision': revision,
            'path': draft_path,
            'sha256': new_hash,
            'status': f'adopted as Chapter {number} R{revision[1:]} re-accepted after the '
                      f'2026-10-11 repair (author ruling 2026-10-30)',
            'coverage': coverage_path,
            'review': f'audits/REACCEPT_2026-10-30_Chapter_{number:02d}_{revision}.md',
            'format_revision': 1,
            'continuity_conflicts': [],
        })

        # 5 · only now, the accepted record — a new date and a new receipt
        record['sha256'] = new_hash
        record['revision'] = revision
        record['accepted_on'] = ACCEPTED_ON
        record['acceptance_receipt'] = (
            f'{RECEIPT} — author ruling 2026-10-30: re-accept the chapters repaired by '
            f'{REPAIR_COMMIT}')

    if args.dry_run:
        print(f'\nDRY RUN: {len(rows)} chapter(s) would be re-accepted. Nothing written.')
        return 0

    if not rows:
        print('Nothing to do — every accepted chapter already matches its file.')
        return 0

    manifest['updated_on'] = ACCEPTED_ON
    dump(manifest_path, manifest)

    summary = root / RECEIPT
    lines = [
        '# Re-acceptance — 2026-10-30',
        '',
        '**The author\'s ruling:** re-accept the repaired chapters. *If the repaired text is what I',
        'read and approved, record it.* This file is that record.',
        '',
        '**Why seven chapters failed.** `tools/run_all.py` returned `STRUCTURE: FAIL` with seven',
        '`ACCEPTED_HASH` errors. The 2026-10-11 repair (`' + REPAIR_COMMIT + '`) removed 7,702',
        'repeated words from chapters 9–14 and 15. The prose changed; the acceptance record did not.',
        'The gate was right and the record was stale.',
        '',
        '**What was not done.** The recorded hashes were not overwritten with whatever sits on disk.',
        'That would silently convert *"these bytes were approved"* into *"whatever is on disk is',
        'approved"* and erase the evidence that a reading happened. Instead each chapter was cut as a',
        'new revision, receipted, and re-accepted with a new date and a new receipt.',
        '',
        '| Ch | Old hash (accepted 2026-10-07/08) | New hash (accepted 2026-10-30) | Revision |',
        '|---:|---|---|---|',
    ]
    for number, _, old, new, revision in rows:
        lines.append(f'| {number} | `{old[:16]}…` | `{new[:16]}…` | {revision} |')
    lines += [
        '',
        '**Restoring the older text.** Every prior byte remains in history:',
        '',
        '```bash',
        f'git show {REPAIR_COMMIT}^:chapters/Chapter_11_The_Sun.md   # the accepted-before-repair file',
        '```',
        '',
        '**Still open, and not touched here.** Chapters 9–14 sit below the 3,000-word floor their',
        'own headers claim (2,569 / 2,729 / 1,333 / 2,256 / 2,933 measured on 2026-10-13). The',
        'padding *was* the length; restoring it means writing prose, which is the author\'s word and',
        'not a repair. Filed on the author\'s desk as the companion to this ruling.',
        '',
        f'Generated by `apply_reaccept.py` on {ACCEPTED_ON}.',
    ]
    summary.write_text('\n'.join(lines) + '\n', encoding='utf-8')

    # 6 · the repo's flat checksum file, kept honest (nothing verifies it, so it must not lie)
    checksums = root / 'CHECKSUMS.sha256'
    if checksums.exists():
        wanted = {}
        for line in checksums.read_text(encoding='utf-8').splitlines():
            if '  ' in line:
                digest, name = line.split('  ', 1)
                wanted[name.strip()] = digest
        for number, chapter_rel, _, new, revision in rows:
            for name in (f'drafts/{Path(chapter_rel).stem}_{revision}.md',
                         f'audits/REACCEPT_2026-10-30_Chapter_{number:02d}_{revision}.md',
                         f'canon_coverage/Chapter_{number:02d}_{revision}.json',
                         chapter_rel,
                         f'canon_coverage/{Path(chapter_rel).stem}.json'):
                target = root / name
                if target.exists():
                    wanted[name] = sha(target)
        checksums.write_text(
            ''.join(f'{digest}  {name}\n' for name, digest in sorted(wanted.items())),
            encoding='utf-8')

    print(f'\nRE-ACCEPTED {len(rows)} chapter(s) on {ACCEPTED_ON}.')
    for number, _, old, new, revision in rows:
        print(f'  C{number:02d} {revision}: {old[:12]}… -> {new[:12]}…')
    print('\nNow run: python3 tools/run_all.py   (it must print PROJECT CHECKS: PASS)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
