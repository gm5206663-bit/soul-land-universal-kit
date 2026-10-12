#!/usr/bin/env python3
"""THE REGISTER — every book and every chapter-bearing tree on this account.

    python3 register.py --root DIR --out REGISTER.md

Why this exists: on 2026-10-12 the account's own tools turned out to have been
registering what they happened to look at, not what was there — the largest
serial in the account (116 chapters), the Soul Land 3 / Lin Hao project
(101 chapters), an entire library shelf and a whole workshop had never been seen
by any of them. This tool prints the whole disk: every book with its size and
its defects, and every tree outside the register with its classification. It is
generated, never hand-typed, and it regenerates in one command.
"""
import os
import sys
import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import live_book_gate as lbg        # noqa: E402
import account_checks as checks     # noqa: E402


def measure_book(b):
    files = checks.book_files(b)
    words = over = dlg = floor_hits = 0
    for p in files:
        m = lbg.measure(p)
        words += m['words']; over += len(m['over']); dlg += m['dlg']
        if m['dlg'] < lbg.DIALOGUE_FLOOR:
            floor_hits += 1
    return len(files), words, over, dlg, floor_hits


def main():
    args = sys.argv[1:]
    root = args[args.index('--root') + 1] if '--root' in args else '.'
    out = args[args.index('--out') + 1] if '--out' in args else None
    label = args[args.index('--label') + 1] if '--label' in args else os.path.abspath(root)
    books = checks.registry(root)
    sight = checks.check_sightings(root, books)
    lines = []
    add = lines.append
    add('# THE REGISTER — every book, every tree')
    add('')
    add(f'*Generated {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} by '
        f'`tools/register.py` over `{label}`. Regenerate it; never edit it.*')
    add('')
    tot_ch = tot_w = tot_over = 0
    rows = []
    for b in books:
        ch, w, over, dlg, floor = measure_book(b)
        tot_ch += ch; tot_w += w; tot_over += over
        rows.append((w, ch, b, over, dlg, floor))
    rows.sort(key=lambda r: -r[0])
    add(f'**{len(books)} registered books · {tot_ch:,} chapters · {tot_w:,} words · '
        f'{tot_over:,} sentences over 60 words.**')
    add('')
    add('| words | ch | book | over 60 | spoken | floor hits | status |')
    add('|---:|---:|---|---:|---:|---:|---|')
    for w, ch, b, over, dlg, floor in rows:
        label = f"{b['repo']} / {b['book']}" if b['book'] != b['repo'] else b['repo']
        status = 'registered where found' if b.get('promoted') else 'gated book'
        if b.get('readonly') or 'reference copy' in (b['note'] or ''):
            status += ' · read-only'
        add(f'| {w:,} | {ch} | {label} | {over} | {dlg:,} | {floor} | {status} |')
    add('')
    add('## Every tree outside the register, classified')
    add('')
    add('Nothing on this disk holding chapter prose is unnamed. Each line below is a '
        'tree that is not gated as a book — named, counted, and deliberately not gated.')
    add('')
    for f in sight['findings']:
        if f['kind'] == 'sighting':
            add(f"- **{f['detail'].split('— ')[1].split(';')[0].strip()}** — "
                f"{f['detail'].split('— ')[0].strip()}: {f['evidence']}")
    for f in sight['findings']:
        if f['kind'] == 'orphan-work':
            add(f"- **registered where found** — {f['detail']}")
    add('')
    add('## The guarantee')
    add('')
    add(f"- coverage: {sight['coverage']['text']}")
    add(f"- note: {sight['note']}")
    add('')
    add('*A register that only lists what it happened to look at is a register of the '
        'looking. This one lists the disk.*')
    text = '\n'.join(lines) + '\n'
    if out:
        open(out, 'w', encoding='utf-8').write(text)
        print(f'  wrote {out}  ({len(text)} B)')
    else:
        print(text)


if __name__ == '__main__':
    main()
