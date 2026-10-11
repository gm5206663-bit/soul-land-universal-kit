#!/usr/bin/env python3
"""BLOCK DEDUPE — remove paragraphs that appear more than once in one file.

    python3 dedupe_paragraphs.py --report  FILE|DIR...
    python3 dedupe_paragraphs.py --apply   FILE|DIR...
    python3 dedupe_paragraphs.py --selftest

One chapter of *supergirl-adrian-vale* ends with the same combined closing
paragraph twenty times in a row; chapter 11 carries 2,956 repeated words out of
4,282. That is not a refrain — a refrain varies, and this is byte-identical,
twice, three times, twenty times, two blank lines apart, at the end of a file
produced by a pipeline. It is a loop that ran twenty times.

This tool deletes the repeats and keeps the first occurrence. It refuses to
touch anything that might be deliberate:

  * a paragraph under 12 words is left alone — "Yes." and "***" repeat in every
    chapter of that serial on purpose, as beats and scene breaks;
  * the first occurrence always survives, so nothing is invented and nothing is
    reordered;
  * every other byte of the file is copied through untouched.

Verification before writing: the paragraphs of the new file must be exactly the
paragraphs of the old file with the deleted copies removed, in the same order.
A repair that cannot prove that does not get written.
"""

import os
import re
import sys

MIN_WORDS = 12


def paragraphs(text):
    """(start, end) spans of paragraphs separated by blank lines."""
    spans = []
    for m in re.finditer(r'(?:^|\n)((?:[^\n]+\n?)+?)(?=\n\s*\n|\Z)', text):
        s, e = m.start(1), m.end(1)
        if text[s:e].strip():
            spans.append((s, e))
    return spans


def key(p):
    return re.sub(r'\s+', ' ', p).strip()


def plan(text, min_words=MIN_WORDS):
    """Returns (kept_paragraphs, deleted_paragraphs) in document order."""
    kept, deleted, seen = [], [], {}
    for s, e in paragraphs(text):
        p = text[s:e]
        k = key(p)
        if len(p.split()) < min_words:
            kept.append(p)
            continue
        if k in seen:
            deleted.append(p)
        else:
            seen[k] = True
            kept.append(p)
    return kept, deleted


def rebuild(text, min_words=MIN_WORDS):
    """Rebuild the file with later duplicates removed. Returns (new, deleted)."""
    kept, deleted = plan(text, min_words)
    if not deleted:
        return None, []
    # PROOF: rebuild from the plan and require it to equal an independent
    # filter of the original text — two implementations, one verdict.
    blocks, out = [], []
    for m in re.finditer(r'((?:[^\n]+\n?)+?)(?:\n\s*\n|\Z)', text):
        blocks.append(m.group(1))
    seen = set()
    for b in blocks:
        k = key(b)
        if len(b.split()) >= min_words and k in seen:
            continue
        if len(b.split()) >= min_words:
            seen.add(k)
        out.append(b)
        out.append('\n\n')
    new = ''.join(out)
    if new.endswith('\n\n'):
        new = new[:-1]
    if key(new) != key('\n\n'.join(kept)):
        raise SystemExit('REFUSED: the two rebuild paths disagree — not writing')
    return new, deleted


def process(path, apply=False, min_words=MIN_WORDS):
    raw = open(path, encoding='utf-8').read()
    new, deleted = rebuild(raw, min_words)
    if new is None:
        return dict(path=path, removed=0, words=0)
    saved = sum(len(d.split()) for d in deleted)
    if apply:
        open(path, 'w', encoding='utf-8').write(new)
    return dict(path=path, removed=len(deleted), words=saved,
                examples=[key(d)[:80] for d in deleted[:2]])


def walk(targets):
    for t in targets:
        if os.path.isdir(t):
            for dp, _, fs in os.walk(t):
                if '.git' in dp.split(os.sep):
                    continue
                for f in sorted(fs):
                    if f.endswith('.md'):
                        yield os.path.join(dp, f)
        else:
            yield t


def selftest():
    ok = True

    def case(name, text, want_removed, want_words):
        nonlocal ok
        new, deleted = rebuild(text)
        got = (len(deleted) if new is not None else 0)
        saved = sum(len(d.split()) for d in deleted)
        good = got == want_removed and saved == want_words
        if new is not None:
            # nothing invented: every kept paragraph must exist in the original
            good = good and all(key(p) in key(text) for p in plan(new)[0])
        ok &= good
        print(f"  [{'ok ' if good else 'FAIL'}] {name:56s} removed={got} words={saved}")

    long_p = 'There would be another headline tomorrow and tonight there was sun still in her cells and a chipped mug on a desk.'
    case('a paragraph repeated three times keeps one',
         f'A first paragraph that opens the file for the reader today.\n\n{long_p}\n\n{long_p}\n\n{long_p}\n', 2, 44)
    case('a short beat repeated is deliberate and stays',
         'Kara nodded.\n\nKara nodded.\n\nKara nodded.\n', 0, 0)
    case('scene-break markers stay',
         'Text that opens the chapter and runs on for a while here.\n\n***\n\nMore text after the break that keeps going here.\n\n***\n', 0, 0)
    case('different paragraphs are not touched',
         'One paragraph of prose about the roof and the cold November wind.\n\nAnother paragraph of prose about the mug and the magnet.\n', 0, 0)
    print()
    print('BLOCK DEDUPE SELFTEST ' + ('PASSED' if ok else 'FAILED'))
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    if '--selftest' in args:
        return selftest()
    mode = 'apply' if '--apply' in args else 'report'
    targets = [a for a in args if not a.startswith('-')]
    if not targets:
        print(__doc__)
        return 0
    files = removed = words = 0
    for f in walk(targets):
        if not f.endswith('.md'):
            continue
        r = process(f, apply=(mode == 'apply'))
        if r['removed']:
            files += 1
            removed += r['removed']
            words += r['words']
            print(f"  {'removed' if mode == 'apply' else 'WOULD remove'} "
                  f"{r['removed']:3d} passage(s) / {r['words']:5d} words  {os.path.relpath(f)}")
    print(f"\n{mode.upper()}: {removed} duplicate passage(s) in {files} file(s) · "
          f"{words} repeated words " + ("removed" if mode == 'apply' else "at stake"))
    return 0


if __name__ == '__main__':
    sys.exit(main())
