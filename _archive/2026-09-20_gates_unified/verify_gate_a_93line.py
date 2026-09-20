#!/usr/bin/env python3
"""verify.py — the kit's machine gates (07_PROSE_LAW §8, 02 filename law).
Rebuilt from kit references; originals not in this upload.

Usage:  python3 verify.py <project_root>

Every check is a named function and prints what it touched (00_START_HERE:
"a check that executes nothing verifies nothing").

HARD gates (failure = not done):
  check_cjk_sweep        zero non-Latin-script characters in any .md
  check_literal_bsn      zero literal backslash-n two-char sequences
  check_filename_law     ASCII letters/digits/underscores/dots only
  check_digits_in_prose  zero digits in the prose body (before '## Footer',
                         excluding the '# Chapter N' title line)
ADVISORY (reported, ruling pending — see project's NO_MISTAKE_LIVE_RULES):
  report_footer          kit panel discipline says slim top panel, no footer
  report_dialogue        kit prose law wants >=3 spoken dialogue lines
"""
import re, sys, pathlib

CJK = re.compile(r'[\u3040-\u30ff\u31f0-\u31ff\u3400-\u4dbf\u4e00-\u9fff'
                 r'\uf900-\ufaff\uff00-\uffef\uac00-\ud7af]')
BSN = re.compile(re.escape(chr(92)) + 'n')  # literal backslash-n pair, not a newline
FNAME = re.compile(r'^[A-Za-z0-9_.]+$')
DIGIT = re.compile(r'\d')
SPEECH = re.compile(r'[\u201c"][^\u201c"\n]{2,}[\u201d"]')

def check_cjk_sweep(root, files):
    bad = {str(f): len(CJK.findall(f.read_text())) for f in files if CJK.search(f.read_text())}
    print(f'[check_cjk_sweep]       scanned {len(files)} md files -> ' +
          (f'FAIL: {bad}' if bad else 'clean'))
    return not bad

def check_literal_bsn(root, files):
    bad = [str(f) for f in files if BSN.search(f.read_text())]
    print(f'[check_literal_bsn]     scanned {len(files)} md files -> ' +
          (f'FAIL: {bad}' if bad else 'clean'))
    return not bad

def check_filename_law(root, files):
    bad = [str(f) for f in files if not FNAME.match(f.name)]
    print(f'[check_filename_law]    scanned {len(files)} filenames -> ' +
          (f'FAIL: {bad}' if bad else 'clean'))
    return not bad

def check_digits_in_prose(root, files):
    """Digits forbidden in PROSE ONLY: body before '## Footer', title line exempt."""
    bad = []
    chapters = sorted((root / 'chapters').glob('*.md')) if (root / 'chapters').is_dir() else []
    for f in chapters:
        body = f.read_text().split('## Footer')[0]
        lines = [l for l in body.splitlines() if not l.startswith('# ')]
        hits = [(i + 1, l.strip()[:70]) for i, l in enumerate(lines) if DIGIT.search(l)]
        if hits:
            bad.append((str(f), hits))
    print(f'[check_digits_in_prose] scanned {len(chapters)} chapter bodies -> ' +
          (f'FAIL: {bad}' if bad else 'clean'))
    return not bad

def report_footer(root, files):
    chapters = sorted((root / 'chapters').glob('*.md')) if (root / 'chapters').is_dir() else []
    withf = [f.name for f in chapters if '## Footer' in f.read_text()]
    print(f'[report_footer]         chapters carrying a footer: {len(withf)}/{len(chapters)} '
          f'(kit says no footer — ruling pending)')

def report_dialogue(root, files):
    chapters = sorted((root / 'chapters').glob('*.md')) if (root / 'chapters').is_dir() else []
    for f in chapters:
        body = f.read_text().split('## Footer')[0]
        n = len(SPEECH.findall(body))
        flag = 'ok ' if n >= 3 else 'LOW'
        print(f'[report_dialogue]       {f.name}: {n} spoken lines [{flag}]')

def main():
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    files = [p for p in root.rglob('*.md')
             if not any(part.startswith('.') for part in p.parts)]
    print(f'verify.py — root: {root} — {len(files)} md files\n')
    results = [
        check_cjk_sweep(root, files),
        check_literal_bsn(root, files),
        check_filename_law(root, files),
        check_digits_in_prose(root, files),
    ]
    print()
    report_footer(root, files)
    report_dialogue(root, files)
    print('\nVERDICT: ' + ('PASS — all hard gates clean' if all(results) else 'FAIL — fix hard gates'))
    sys.exit(0 if all(results) else 1)

if __name__ == '__main__':
    main()
