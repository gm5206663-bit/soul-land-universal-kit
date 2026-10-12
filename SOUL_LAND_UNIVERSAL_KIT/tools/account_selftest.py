#!/usr/bin/env python3
"""ACCOUNT CONTROL CENTRE — selftest.

A detector that has only ever been seen to pass is a detector nobody tested.
Every case here builds a small account, injects ONE defect, and requires the
detector that owns that defect to fire — and the clean tree to stay silent, so a
detector cannot pass by simply flagging everything.

Run:  python3 tools/account_selftest.py
"""

import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import account as ac          # noqa: E402
import account_checks as checks  # noqa: E402

OK = True

CH = {
    1: 'The road east was {long} and the boy counted every stone along the way before dark.\n\n'
       '"Sit," she said. "Eat," he said. "Now," she said.\n\n'
       'That was the whole lesson and he carried it {far} like a folded map.\n',
    2: 'He mended the {long} fence at noon and the farmer watched him work without speaking.\n\n'
       '"Good," the farmer said. "Fast," the woman said. "Fair," the child said.\n\n'
       'He took {far} bread for it and walked on before the sun turned.\n',
    3: 'The third village smelled of {long} smoke and wet straw when he came down the hill.\n\n'
       '"Here," the smith said. "Rest," his wife said. "Work," the smith said.\n\n'
       'He slept by the {far} forge and left at first light without waking anyone.\n',
    4: 'Snow came to the {long} pass and he learned to read the drifts before he crossed.\n\n'
       '"Wait," the guide said. "Now," the guide said. "Go," the guide said.\n\n'
       'The far side was {far} warmer and he was glad of the road behind him.\n',
}


def chapter(n, longw='grey', farw='thin'):
    return CH[n].format(long=longw, far=farw)


def write(p, text):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(text)


def as_repo(r, name='alpha-repo'):
    write(os.path.join(r, name, '.git', 'HEAD'), 'ref: refs/heads/main')


def book(root, repo, name, chapters=4, longw='grey', farw='thin', readme=None, docs=True):
    d = os.path.join(root, repo, name)
    for n in range(1, chapters + 1):
        t = chapter(n, longw, farw)
        write(os.path.join(d, 'chapters', f'Chapter_{n:02d}.md'), t)
        write(os.path.join(d, 'manuscript', f'Chapter_{n:02d}.md'), t)
    write(os.path.join(d, 'README.md'),
          readme if readme is not None
          else f'# {name}\n\nUpdated 2026-10-11 · chapters 1–{chapters}\n')
    if docs:
        for n in range(1, chapters + 1):
            write(os.path.join(d, 'docs', f'chapter_{n:02d}.html'), '<html></html>')
    return d


def build(root):
    shutil.rmtree(root, ignore_errors=True)
    book(root, 'alpha-repo', 'Book_One', longw='grey', farw='thin')
    book(root, 'beta-repo', 'Book_Two', longw='ochre', farw='warm')


def kinds(rep):
    return {f['kind'] for f in rep['findings']}


def case(name, mutate, expect_kind, want=True, only=None):
    global OK
    root = os.path.join(TMP, 'root')
    build(root)
    mutate(root)
    rep = ac.run(root, only=only)
    got = kinds(rep)
    good = (expect_kind in got) == want
    OK &= good
    label = f"{'expects' if want else 'expects NOT'} {expect_kind}"
    print(f"  [{'ok ' if good else 'FAIL'}] {name:56s} {label}")
    if not good:
        print(f"        kinds seen: {sorted(got)}")
        for f in rep['findings'][:4]:
            print(f"        · {f['severity']} {f['kind']}: {f['detail'][:90]}")


TMP = tempfile.mkdtemp()

# ---------------------------------------------------------------- clean tree
root = os.path.join(TMP, 'root')
build(root)
rep = ac.run(root)
hard = [f for f in rep['findings'] if f['severity'] == 'hard']
print(f"  [{'ok ' if not hard else 'FAIL'}] a clean account of two books reports no hard finding "
      f"{'':8s} (0 hard)")
OK &= not hard
for f in hard:
    print(f"        · {f['kind']}: {f['detail'][:100]}")
print(f"        coverage: " + ' | '.join(c['text'] for c in rep['coverage']))

# ---------------------------------------------------------------- 1 accident
case('a sentence repeated twice INSIDE one chapter is hard',
     lambda r: write(os.path.join(r, 'alpha-repo', 'Book_One', 'chapters', 'Chapter_01.md'),
                     chapter(1) + '\n' + 'The road east was grey and the boy counted every stone '
                     'along the way before dark.\n'),
     'repeat-in-file')

# ---------------------------------------------------------------- 2 refrain
case('a sentence repeated across chapters is advisory, not hard',
     lambda r: write(os.path.join(r, 'alpha-repo', 'Book_One', 'chapters', 'Chapter_02.md'),
                     chapter(2) + '\n' + 'The road east was grey and the boy counted every stone '
                     'along the way before dark.\n'),
     'repeat-across')

# ---------------------------------------------------------------- 3 copies
case('reader edition drifting from the author edition',
     lambda r: write(os.path.join(r, 'alpha-repo', 'Book_One', 'manuscript', 'Chapter_01.md'),
                     chapter(1) + '\nA sentence the author never wrote sits only in the reader copy.\n'),
     'copies-drift')

# ---------------------------------------------------------------- 4 orphan
case('a published chapter with no author edition',
     lambda r: write(os.path.join(r, 'alpha-repo', 'Book_One', 'manuscript', 'Chapter_09.md'),
                     'An orphan chapter that nobody wrote in the author edition at all today.\n'),
     'source-orphan')

# ---------------------------------------------------------------- 5 receipts
case('a README claiming more chapters than exist',
     lambda r: write(os.path.join(r, 'alpha-repo', 'Book_One', 'README.md'),
                     '# Book_One\n\nUpdated 2026-10-11 · chapters 1–9\n'),
     'receipt-drift')

# ---------------------------------------------------------------- 6 a floor
case('a deliberate floor (220+) is not a pinned count',
     lambda r: write(os.path.join(r, 'alpha-repo', 'Book_One', 'README.md'),
                     '# Book_One\n\nUpdated 2026-10-11 · 220+ chapters live\n'),
     'receipt-drift', want=False)

# ---------------------------------------------------------------- 7 publish
case('the published site missing a chapter the book has',
     lambda r: os.remove(os.path.join(r, 'alpha-repo', 'Book_One', 'docs', 'chapter_04.html')),
     'publish-drift')

# ---------------------------------------------------------------- 8 homes
case('one text living in two books',
     lambda r: write(os.path.join(r, 'beta-repo', 'Book_Two', 'chapters', 'Chapter_01.md'),
                     chapter(1)) or
     write(os.path.join(r, 'beta-repo', 'Book_Two', 'manuscript', 'Chapter_01.md'), chapter(1)),
     'two-homes', only=['two-homes'])

# ---------------------------------------------------------------- 8b derived
case('a book and its own published copy are one home, not two',
     lambda r: write(os.path.join(r, 'beta-repo', 'published-site', 'Book_Two',
                                  'chapters', 'Chapter_01.md'), chapter(1)),
     'two-homes', want=False, only=['two-homes'])

# ---------------------------------------------------------------- 8d duplicates
case('a published copy repeating its source is one home, not a duplicate',
     lambda r: write(os.path.join(r, 'beta-repo', 'published-site', 'Book_Two',
                                  'chapters', 'Chapter_01.md'), chapter(1, 'ochre', 'warm')),
     'repeat-across', want=False, only=['dupes'])

# ---------------------------------------------------------------- 8f links
case('a link to a file that is not there is reported',
     lambda r: as_repo(r) or
     write(os.path.join(r, 'alpha-repo', 'README.md'),
           '# Book_One\n\n[the missing chapter](chapters/Chapter_99.md)\n'),
     'dead-link', only=['links'])

case('a link that resolves is not reported',
     lambda r: as_repo(r) or
     write(os.path.join(r, 'alpha-repo', 'README.md'),
           '# Book_One\n\n[the real chapter](Book_One/chapters/Chapter_01.md)\n'),
     'dead-link', want=False, only=['links'])

case('a placeholder in prose is not a dead link',
     lambda r: as_repo(r) or
     write(os.path.join(r, 'alpha-repo', 'README.md'),
           'Always cite with [id](url) when using search results.\n'),
     'dead-link', want=False, only=['links'])

case('fenced code and script blocks are not navigation',
     lambda r: as_repo(r) or
     write(os.path.join(r, 'alpha-repo', 'README.md'), '```\n[ex](nope.md)\n```\n') or
     write(os.path.join(r, 'alpha-repo', 'page.html'),
           '<script>var h = \'href="moved.html"\';</script><p>ok</p>\n'),
     'dead-link', want=False, only=['links'])

# ---------------------------------------------------------------- 8g generated
case('a stamped view whose source changed is reported',
     lambda r: as_repo(r) or
     write(os.path.join(r, 'alpha-repo', 'foundation', 'SRC.json'), '{"v": 1}\n') or
     write(os.path.join(r, 'alpha-repo', 'VIEW.md'),
           '<!-- GENERATED from foundation/SRC.json; SHA256: '
           + '0' * 64 + ' -->\n\n# View\n'),
     'stale-generated', only=['generated'])

case('a stamp that matches its source is silent',
     lambda r: as_repo(r) or
     write(os.path.join(r, 'alpha-repo', 'foundation', 'SRC.json'), '{"v": 1}\n') or
     write(os.path.join(r, 'alpha-repo', 'VIEW.md'),
           '<!-- GENERATED from foundation/SRC.json; SHA256: '
           + __import__('hashlib').sha256(b'{"v": 1}\n').hexdigest() + ' -->\n\n# View\n'),
     'stale-generated', want=False, only=['generated'])

# ---------------------------------------------------------------- 8h enforcement
case('a repo with gates and no workflow is reported',
     lambda r: as_repo(r) or
     write(os.path.join(r, 'alpha-repo', 'tools', 'chapter_gate.py'), 'print("gate")\n'),
     'ci-gap', only=['enforcement'])

case('a repo with a workflow is not reported as a gap',
     lambda r: as_repo(r) or
     write(os.path.join(r, 'alpha-repo', 'tools', 'chapter_gate.py'), 'print("gate")\n') or
     write(os.path.join(r, 'alpha-repo', '.github', 'workflows', 'gate.yml'), 'name: gate\n'),
     'ci-gap', want=False, only=['enforcement'])

# ---------------------------------------------------------------- 8e housekeeping
case('a committed .pyc is reported as housekeeping',
     lambda r: as_repo(r) or
     write(os.path.join(r, 'alpha-repo', 'tools', '__pycache__', 'x.pyc'), 'x'),
     'housekeeping', only=['housekeeping'])

case('an archive frozen in the repo is reported as housekeeping',
     lambda r: as_repo(r) or
     write(os.path.join(r, 'alpha-repo', 'snapshot.zip'), 'PK'),
     'housekeeping', only=['housekeeping'])

case('a clean account has no housekeeping finding',
     lambda r: as_repo(r),
     'housekeeping', want=False, only=['housekeeping'])

case('text only a published copy carries is still a duplicate',
     lambda r: write(os.path.join(r, 'beta-repo', 'published-site', 'Book_Two',
                                  'chapters', 'Chapter_01.md'),
                     chapter(1, 'ochre', 'warm') + '\nA line that lives only in the '
                     'published copy and nowhere in the author source today.\n\n'
                     'A line that lives only in the published copy and nowhere in '
                     'the author source today.\n'),
     'repeat-in-file', only=['dupes'])

# ---------------------------------------------------------------- 8c history
case('a historical note is not a claim about the live book',
     lambda r: write(os.path.join(r, 'alpha-repo', 'Book_One', 'README.md'),
                     '# Book_One\n\n## The chapters — V1 ARCHIVED (9 chapters, pre-rebuild, '
                     'kept for reference)\n'),
     'receipt-drift', want=False, only=['receipts'])

# ---------------------------------------------------------------- 8d subset
case('a subset reference is not a claim about the book',
     lambda r: write(os.path.join(r, 'alpha-repo', 'Book_One', 'README.md'),
                     '# Book_One\n\nChapters 1\u20133 sit over the band on the author\'s desk.\n'),
     'receipt-drift', want=False, only=['receipts'])

# ---------------------------------------------------------------- 8e another book
case('a line about a DIFFERENT book is not a claim about this one',
     lambda r: write(os.path.join(r, 'alpha-repo', 'Book_One', 'README.md'),
                     '# Book_One\n\nSome_Other_Book status: all 24 chapters live in the kit.\n'),
     'receipt-drift', want=False, only=['receipts'])

# ---------------------------------------------------------------- 8f live edge
case('a stale live-edge claim IS caught',
     lambda r: write(os.path.join(r, 'alpha-repo', 'Book_One', 'README.md'),
                     '# Book_One\n\nLive edge: after Chapter 2, \"Round One.\"\n'),
     'receipt-drift', only=['receipts'])

# ---------------------------------------------------------------- 9 refusal
def two_dirs(r):
    write(os.path.join(r, 'alpha-repo', 'Book_One', 'chapters_rebuilt', 'Chapter_01.md'), chapter(1))
    write(os.path.join(r, 'alpha-repo', 'Book_One', 'README.md'), '# Book_One\n\nA book.\n')


case('two chapter directories and nothing to disambiguate them',
     two_dirs, 'scope-refusal')

# ---------------------------------------------------------------- 10 nothing
case('a report over nothing is not a clean report',
     lambda r: [shutil.rmtree(os.path.join(r, 'alpha-repo')), shutil.rmtree(os.path.join(r, 'beta-repo'))],
     'scope-refusal')

# ---------------------------------------------------------------- 11 dead dir
def with_dead(r):
    write(os.path.join(r, 'alpha-repo', 'Book_One', 'chapters_old', 'Chapter_01.md'), chapter(1))
    write(os.path.join(r, 'alpha-repo', 'Book_One', 'README.md'),
          '# Book_One\n\nUpdated 2026-10-11 · chapters 1–4\nchapters_old/ is superseded — do not use.\n')


case('a dead directory is skipped, not gated',
     with_dead, 'scope-refusal', want=False)

print()
shutil.rmtree(TMP, ignore_errors=True)
print('ACCOUNT SELFTEST ' + ('PASSED' if OK else 'FAILED — do not trust these detectors'))
sys.exit(0 if OK else 1)
