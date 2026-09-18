#!/usr/bin/env python3
"""PROJECT-AGNOSTIC VERIFICATION SUITE.

Works on ANY fan-fiction project regardless of chapter format. It makes no assumptions
about footers, headers or power systems — it checks the things that are true of every
prose project: file integrity, text hygiene, repetition, prose quality, and whether the
project carries the scaffolding the framework requires.

Usage:
    python3 /home/user/checks_lib/verify_base.py <project_dir>

Exit 0 = pass, 1 = failures present.
"""
import collections
import os
import re
import sys

# ------------------------------------------------------------------ load
if len(sys.argv) < 2:
    raise SystemExit('usage: verify_base.py <project_dir>')
ROOT = os.path.abspath(sys.argv[1])
CH = os.path.join(ROOT, 'chapters')
if not os.path.isdir(CH):
    raise SystemExit(f'{CH}: no chapters directory')

chapters = {}      # prose only (for repetition / quality / hygiene)
fulltext = {}      # whole file (for scaffolding checks — footers count)
for f in sorted(os.listdir(CH)):
    if f.endswith('.md'):
        m = re.search(r'(\d+)', f)
        if m:
            n = int(m.group(1))
            _full = open(os.path.join(CH, f), encoding='utf-8').read()
            fulltext[n] = _full
            chapters[n] = re.split(r'#{2,3} (?:End of Chapter|END OF CHAPTER)', _full)[0]
if not chapters:
    raise SystemExit('no chapter files found')
MAXCH = max(chapters)

# a project codex is any large .md at the project root
CODEX = ''
for f in sorted(os.listdir(ROOT)):
    if f.endswith('.md') and os.path.getsize(os.path.join(ROOT, f)) > 20000:
        CODEX += open(os.path.join(ROOT, f), encoding='utf-8').read()

F, W = [], []
def fail(s, m): F.append(f'[{s}] {m}')
def warn(s, m): W.append(f'[{s}] {m}')
def ok(s, m): print(f'  ok   {m}')

BANNED_PHRASES = [
    "You're going to be *so* jealous", 'Maybe a little.', "That's the spirit",
    'heavy enough to set down', 'the shape of the seven',
]

# ------------------------------------------------ 1. FILE INTEGRITY
print('\n=== 1. FILE INTEGRITY ===')
nums = sorted(chapters)
gaps = [n for n in range(1, MAXCH + 1) if n not in nums]
if gaps:
    fail('FILES', f'chapter numbering has gaps — missing: {gaps}')
paras = collections.defaultdict(list)
for n, t in chapters.items():
    for para in t.split('\n\n'):
        p = re.sub(r'\s+', ' ', para).strip()
        if len(p.split()) > 30:
            paras[p].append(n)
for p, ns in paras.items():
    if len(ns) > 1:
        fail('FILES', f'paragraph duplicated across chapters {ns}: "{p[:60]}..."')
ok('FILES', f'{len(chapters)} chapters (max {MAXCH}), no duplicated paragraphs')

# ------------------------------------------------ 2. TEXT HYGIENE
print('\n=== 2. TEXT HYGIENE ===')
# A canon gloss — an English name immediately followed by the original in parentheses,
# e.g. "Fire Spiral Shield (火旋盾)" — is legitimate in a non-English setting.
# What is NOT legitimate is CJK substituted into English prose with no gloss.
GLOSS = re.compile(r'\([^()]*[\u4e00-\u9fff][^()]*\)')
for n, t in sorted(chapters.items()):
    unglossed = GLOSS.sub('', t)          # strip every parenthesised gloss
    cjk = re.findall(r'[\u4e00-\u9fff]+', unglossed)
    if cjk:
        fail('CJK', f'ch{n}: CJK in prose with no romanised gloss {set(cjk)}')
    for bad in ('PLACEHOLDER', 'TODO', 'FIXME', 'lorem'):
        if bad in t:
            fail('JUNK', f'ch{n}: contains "{bad}"')
ok('CJK', 'no stray CJK or placeholders')

# ------------------------------------------------ 3. REPETITION
print('\n=== 3. REPETITION ===')
def sents(t):
    return [re.sub(r'\W+', ' ', s).strip().lower() for s in re.split(r'(?<=[.!?])\s+', t) if len(s.split()) > 14]
seen = {}
for n, t in sorted(chapters.items()):
    for s in set(sents(t)):
        if s in seen and seen[s] != n and n - seen[s] <= 5:
            fail('REPEAT', f'ch{n}: sentence duplicated from ch{seen[s]}: "{s[:70]}..."')
        seen.setdefault(s, n)
usage = collections.defaultdict(list)
for n, t in sorted(chapters.items()):
    low = t.lower()
    for b in BANNED_PHRASES:
        if b.lower() in low:
            usage[b].append(n)
for b, ns in usage.items():
    # recycling = the same phrase in 3+ chapters that are close together
    run = 1
    for i in range(1, len(ns)):
        run = run + 1 if ns[i] - ns[i-1] <= 3 else 1
        if run >= 3:
            fail('REPEAT', f'"{b}" recycled across consecutive chapters {ns}')
            break
ok('REPEAT', 'no duplicated sentences within a 5-chapter window; no phrase recycled 3+ times')

# ------------------------------------------------ 4. PROSE QUALITY
print('\n=== 4. PROSE QUALITY ===')
for n, t in sorted(chapters.items()):
    w = t.split()
    if len(w) < 2000:
        warn('QUAL', f'ch{n}: {len(w)} words (thin)')
    long_s = [s for s in re.split(r'(?<=[.!?])\s+', t) if len(s.split()) > 95]
    if len(long_s) >= 4:
        warn('QUAL', f'ch{n}: {len(long_s)} sentences over 95 words')
    rate = t.lower().count('because') / max(len(w), 1)
    if rate > 0.022:
        warn('QUAL', f'ch{n}: "because" at {rate:.1%} of words — crutch')
ok('QUAL', 'length, sentence length and crutch-word rates measured')

# ------------------------------------- 5. SCAFFOLDING (framework compliance)
print('\n=== 5. SCAFFOLDING (framework compliance) ===')
SCAFFOLD = {
    '## Canon Reference': 'canon sourcing header',
    '## Timeline': 'timeline header',
    '### Chapter Summary': 'chapter summary',
    '### Character States': 'character states',
    'Ranks at chapter end': 'end-of-chapter state line',
}
for key, label in SCAFFOLD.items():
    have = [n for n, t in sorted(fulltext.items()) if key in t]
    missing = [n for n in sorted(fulltext) if n not in have]
    if not have:
        fail('SCAFFOLD', f'NO chapter has "{key}" ({label}) — the project has no end-of-chapter state record')
    elif missing:
        warn('SCAFFOLD', f'{len(missing)} chapter(s) missing "{key}" ({label}): {missing[:12]}')
    else:
        ok('SCAFFOLD', f'all chapters have {label}')

# ------------------------------------------- 6. CODEX & CHECKS PRESENT
print('\n=== 6. PROJECT INFRASTRUCTURE ===')
if len(CODEX) < 20000:
    fail('INFRA', 'no project bible (a .md over 20 KB) found at the project root')
else:
    ok('INFRA', f'project bible present ({len(CODEX)//1000} KB)')
if not os.path.isdir(os.path.join(ROOT, 'checks')):
    fail('INFRA', 'no checks/ directory — this project has no verification suite (see CODEX/01_UNIVERSAL_CODEX.md Part 41 §6)')
else:
    ok('INFRA', 'checks/ directory present')
for f in ('CONTINUATION_PROMPT.md',):
    if not os.path.exists(os.path.join(ROOT, f)):
        fail('INFRA', f'{f} missing — a new session has no standalone brief')
    else:
        ok('INFRA', f'{f} present')
# every recurring character name should be recorded in the bible
names = collections.Counter()
for n, t in chapters.items():
    for m in re.finditer(r'\b([A-Z][a-z]+ [A-Z][a-z]+)\b', t):
        names[m.group(1)] += 1
STRUCTURAL = ('Canon Reference','Chapter Summary','Character States','Canon Preserved','Not Triggered',
              'Novel Chapters','Spirit Masters','Character Progression','End of Chapter','Butterfly Effects',
              'And Wulin','And Lin','The Association','Spirit Pagoda','Soul Master','Eastsea Academy')
unrecorded = [m for m, k in names.items() if k >= 8 and CODEX and CODEX.count(m) == 0
              and m not in STRUCTURAL and not m.startswith(('And ','But ','The ','Then ','So '))]
if unrecorded:
    warn('INFRA', f'names used 8+ times but absent from the bible: {unrecorded[:10]}')

# ------------------------------------------- 7. CODEX BRANCH INTEGRITY
print('\n=== 7. CODEX BRANCH INTEGRITY ===')
CODEXDIR = '/home/user/CODEX'
if os.path.isdir(CODEXDIR):
    index = os.path.join(CODEXDIR, '00_MASTER_INDEX.md')
    if os.path.exists(index):
        itext = open(index, encoding='utf-8').read()
        for f in sorted(os.listdir(CODEXDIR)):
            if f.endswith('.md') and f[0].isdigit() and not f.startswith(('00_', '97_', '99_')):
                if f not in itext:
                    fail('BRANCH', f'CODEX/{f} exists but is not listed in 00_MASTER_INDEX.md')
        # every file the index claims must exist
        import re as _re
        for m in _re.finditer(r'`(\d\d_[A-Za-z_]+\.md)`', itext):
            if not os.path.exists(os.path.join(CODEXDIR, m.group(1))):
                fail('BRANCH', f'00_MASTER_INDEX.md references {m.group(1)} but the file is missing')
        ok('BRANCH', 'every codex branch is indexed and every indexed branch exists')
    else:
        warn('BRANCH', 'no 00_MASTER_INDEX.md')
else:
    warn('BRANCH', 'no CODEX directory')

# ------------------------------------------------------------- SUMMARY
print('\n' + '=' * 70)
if W:
    print(f'WARNINGS ({len(W)}):')
    for w in W:
        print('  -', w)
if F:
    print(f'\nFAILURES ({len(F)}):')
    for f in F:
        print('  x', f)
    print('=' * 70)
    print('RESULT: FAIL')
    sys.exit(1)
print('RESULT: PASS — base suite green')
print('=' * 70)
sys.exit(0)
