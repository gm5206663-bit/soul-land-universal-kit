#!/usr/bin/env python3
"""build_oc_status.py — THE OC STATUS SHEET, auto-generated and continuous.

Builds foundation/OC_STATUS.md (and, with --site, the library's dd-status.html)
for the Devouring Dragon serial. Everything on the sheet is READ FROM THE
SOURCES at run time — nothing here is hand-maintained:

  bible/HIS_STATUS_PANEL.md    the single authority (identity, cultivation,
                               body, attributes, skills, combat, shapes)
  foundation/CONTINUITY.md     the per-chapter recaps (last row per chapter wins)
  chapters/*.md footers        DL dates and measured word counts
  foundation/STATUS_PANEL.md + the serial's own live line is carried whole.

LAW (RAILS s55): OC_STATUS.md is GENERATED. Never hand-edit it. Re-run this
tool on every ship (the ship script does) — the Sentinel checks the sheet's
LIVE AS OF stamp against the chapter count on disk and fails the build if the
sheet is stale.

Usage:
  python3 soul_land_devouring_dragon/tools/build_oc_status.py
  python3 soul_land_devouring_dragon/tools/build_oc_status.py --site /path/to/site
"""
import glob, html, os, re, sys, datetime

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # serial root
KIT  = os.path.dirname(HERE)
SITE = None
for i, a in enumerate(sys.argv):
    if a == '--site' and i + 1 < len(sys.argv):
        SITE = os.path.abspath(sys.argv[i + 1])

PANEL = os.path.join(HERE, 'bible', 'HIS_STATUS_PANEL.md')
CONT  = os.path.join(HERE, 'foundation', 'CONTINUITY.md')
CHDIR = os.path.join(HERE, 'chapters')
SP    = os.path.join(HERE, 'foundation', 'STATUS_PANEL.md')
README= os.path.join(HERE, 'README.md')

def read(p):
    return open(p, encoding='utf-8').read() if os.path.exists(p) else ''

panel = read(PANEL); cont = read(CONT); sp = read(SP); readme = read(README)

# ── the live line (panel header) ────────────────────────────────────────────
m = re.search(r'Live after Chapter (\d+) "([^"]+)"(.*)', panel)
live_n, live_title = (int(m.group(1)), m.group(2)) if m else (0, '?')
live_note = (m.group(3).strip() if m else '')
live_dl = ''
md = re.search(r'\(DL ([\d–\- ]+)', live_note)
if md: live_dl = 'DL ' + md.group(1).rstrip(' –-')

# ── panel sections §1–§8, verbatim (the authority) ──────────────────────────
secs, cur = {}, None
for line in panel.split('\n'):
    h = re.match(r'## (\d)\. (.*)', line)
    if h:
        cur = h.group(1); secs[cur] = ['## ' + h.group(1) + '. ' + h.group(2)]
    elif cur:
        if line.startswith('## Chapter') or line.startswith('## Chapters'):
            cur = None; continue
        secs[cur].append(line)
sections = {k: '\n'.join(v).strip() for k, v in secs.items() if k in '12345678'}

# ── chapters: DL span + measured words from each footer ────────────────────
chapters = {}
for p in sorted(glob.glob(os.path.join(CHDIR, 'Chapter_*.md'))):
    t = read(p)
    mt = re.match(r'# Chapter (\d+): (.*)', t)
    if not mt: continue
    n = int(mt.group(1))
    dl = ''
    mdt = re.search(r'Chapter time: (DL [\d]+(?:[–\-][\d]+)?)', t)
    if mdt: dl = mdt.group(1)
    words = ''
    mw = re.search(r'Word count \(body\): ([\d,]+)', t)
    if mw: words = mw.group(1)
    chapters[n] = {'title': mt.group(2), 'dl': dl, 'words': words}
N = max(chapters) if chapters else 0

# ── CONTINUITY recaps (last row per chapter wins) ───────────────────────────
recaps = {}
for line in cont.split('\n'):
    mr = re.match(r'^\| ch(\d+)[a-z]? \|([^|]+)\|([^|]+)\|', line)
    if mr:
        recaps[int(mr.group(1))] = (mr.group(2).strip(), mr.group(3).strip())

# ── next chapter (story edge — the serial README's NEXT BEAT line is canonical) ──
next_n = N + 1
next_title, next_note = None, ''
mb = re.search(r'NEXT BEAT: Chapter (\d+) — ([^,;(\n]+)', readme)
if mb:
    next_n = int(mb.group(1)); next_title = mb.group(2).strip()
    mnb = re.search(r'NEXT BEAT:.*?(?:; (.*))?$', readme, re.S)
    if mnb and mnb.group(1): next_note = mnb.group(1).strip()
else:
    for src in (sp, readme):
        mn = re.search(rf'Ch {next_n}\s*[“"\']([^”"\']+)', src)
        if mn: next_title = mn.group(1); break
next_line = f'Chapter {next_n} ' + (f'"{next_title}"' if next_title else '(not yet titled)')

# ── glance fields out of the panel ──────────────────────────────────────────
def field(pat, src=None):
    src = src if src is not None else panel
    m = re.search(pat, src)
    if not m: return '—'
    val = m.group(1).strip()
    # join wrapped continuation lines (indented, not a new bullet; blank lines
    # inside a wrapped entry are skipped)
    for ln in src[m.end():].split('\n'):
        s = ln.rstrip()
        if not s.strip():
            continue
        if s.startswith((' ', '\t')) and not s.strip().startswith(('- ', '## ')):
            val = (val[:-1] if val.endswith('-') and not val.endswith('--') else val + ' ') + s.strip()
        else:
            break
    return re.sub(r'\s+', ' ', val).strip()
def block(prefix):
    m = re.search(re.escape(prefix) + r'[^\n]*(\n(?!\s*- )[^\n]*)*', panel)
    out = m.group(0) if m else '—'
    return re.sub(r'\s+', ' ', out.replace(prefix, '', 1)).strip()

def glance(v, cap=170):
    v = re.sub(r'\s+', ' ', v).strip().rstrip(';')
    if len(v) > cap:
        v = v[:cap].rsplit(' ', 1)[0] + ' …'
    return v

f_name  = field(r'- Name: (.*)')
f_race  = field(r'- Race: (.*)')
f_born  = field(r'- Born: (.*)')
f_age   = field(r'- Real age now: (.*)')
f_tier  = field(r'- Tier: (.*)')
f_cult  = field(r'- Cultivation-age estimate: (.*)')
f_ring  = field(r'- Ring of him if killed now: (.*)')
f_bar1  = field(r'- First barrier [^:]*: (.*)')
f_barn  = field(r'- Next barrier: (.*)')
f_len   = field(r'- Length[^:]*: (.*)')
f_wt    = field(r'- Weight: (.*)')
f_scales= field(r'- Scales: (.*)')
f_terr  = block('- Territory now:')
terr_short = f_terr.split(';')[0].split('←')[0].strip()

NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
STAMP = f'LIVE AS OF: Chapter {N} "{chapters.get(N, {}).get("title", "?")}"' + (f' ({live_dl})' if live_dl else '')

GLANCE = [
    ('Name', glance(f_name, 120)), ('Race', glance(f_race)), ('Born', glance(f_born)),
    ('Real age now', glance(f_age)), ('Cultivation class', glance(f_tier)),
    ('Cultivation-age', glance(f_cult)), ('Ring if killed now', glance(f_ring)),
    ('First barrier', glance(f_bar1)), ('Next barrier', glance(f_barn)),
    ('Length / weight', glance(f"{f_len} · {f_wt}")), ('Scales', glance(f_scales)),
    ('Where he is now', glance(terr_short, 200)), ('Next chapter', next_line),
]

# ── markdown sheet ──────────────────────────────────────────────────────────
L = []
A = L.append
A('# OC STATUS — THE DEVOURING DRAGON (DD)')
A('')
A('> **The one clean sheet of everything about him. AUTO-GENERATED — never hand-edit.**')
A('> Sources, read fresh on every run: `bible/HIS_STATUS_PANEL.md` (the authority) · '
  '`foundation/CONTINUITY.md` (chapter recaps) · chapter footers (DL dates, measured counts).')
A('> Regenerated on every ship by `tools/build_oc_status.py`; the Sentinel fails the build if this sheet is stale.')
A('')
A(f'GENERATED: {NOW}')
A(f'{STAMP}')
A(f'NEXT: {next_line}')
A('')
A('---')
A('')
A('## AT A GLANCE')
A('')
A('| Field | Status |')
A('|---|---|')
for k, v in GLANCE:
    A(f'| **{k}** | {v} |')
A('')
A('---')
A('')
names = {'1':'IDENTITY','2':'CULTIVATION','3':'BODY','4':'ATTRIBUTES',
         '5':'SKILLS & POWERS','6':'COMBAT POWER','7':'WHAT HE IS NOT','8':'KEPT SHAPES'}
A('## THE FULL SHEET (from HIS_STATUS_PANEL — the single authority)')
A('')
A('*(sections carried verbatim from the panel — the panel is right if anything here reads oddly; design estimates are the author\'s to correct)*')
A('')
for k in '12345678':
    if k in sections:
        A(sections[k])
        A('')
A('')
A('---')
A('')
A('## LIFE LEDGER — every chapter, in order')
A('')
A('| # | DL | Title | Words | Where it left him |')
A('|---|---|---|---|---|')
for n in sorted(chapters):
    c = chapters[n]
    short = recaps.get(n, ('', ''))[0]
    A(f"| {n} | {c['dl']} | {c['title']} | {c['words']} | {short} |")
A('')
A('---')
A('')
A('## LIVE EDGE — where the story stands')
A('')
note_inner = live_note.strip().lstrip('(').rstrip(')')
note_inner = re.sub(r'^DL [\d–\- ]+\s*[—-]\s*', '', note_inner)
A(f'**{STAMP}.** {note_inner}')
A('')
A(f'**Next: {next_line}**')
A('')
md_out = '\n'.join(L) + '\n'
open(os.path.join(HERE, 'foundation', 'OC_STATUS.md'), 'w', encoding='utf-8').write(md_out)
print(f'OC_STATUS.md written: {N} chapters, live at Ch {N}, next {next_line}')

# ── site page ───────────────────────────────────────────────────────────────
if SITE:
    def esc(s): return html.escape(s, quote=False)
    css = ('body{background:#0a0e14;color:#c8d6e5;font:15px/1.75 ui-sans-serif,system-ui,Helvetica,sans-serif;margin:0}'
           '.wrap{max-width:900px;margin:0 auto;padding:34px 20px 60px}h1{font-size:25px;color:#e8f0fa}h1 span{color:#f0b429}'
           '.sub{color:#8b9db3;font-size:14px;margin:4px 0 8px}.stamp{color:#4fd1c5;font-size:13px;border:1px solid #2a3a4d;'
           'border-radius:8px;padding:8px 14px;display:inline-block;margin:10px 0 4px}'
           'h2{font-size:18px;color:#f0b429;margin:30px 0 10px}table{border-collapse:collapse;width:100%;font-size:13.5px}'
           'th,td{border:1px solid #2a3a4d;padding:6px 9px;text-align:left;vertical-align:top}th{color:#8b9db3;font-weight:600}'
           'td b{color:#e8f0fa}details{border:1px solid #2a3a4d;border-radius:8px;padding:10px 16px;margin:10px 0}'
           'summary{cursor:pointer;color:#f0b429;font-weight:600}pre{white-space:pre-wrap;font:inherit;color:inherit;margin:8px 0 0}'
           'a{color:#4fd1c5;text-decoration:none}.foot{color:#5d7186;font-size:12.5px;margin-top:30px}')
    rows = '\n'.join(f'<tr><td><b>{n}</b></td><td>{esc(c["dl"])}</td><td>{esc(c["title"])}</td>'
                     f'<td>{esc(c["words"])}</td><td>{esc(recaps.get(n, ("", ""))[0])}</td></tr>'
                     for n, c in sorted(chapters.items()))
    glance = '\n'.join(f'<tr><td><b>{esc(k)}</b></td><td>{esc(v)}</td></tr>' for k, v in GLANCE)
    det = ''
    order = {'1':'IDENTITY','2':'CULTIVATION','3':'BODY','4':'ATTRIBUTES',
             '5':'SKILLS & POWERS','6':'COMBAT POWER','7':'WHAT HE IS NOT (anti-inflation locks)','8':'KEPT SHAPES (the map of his world)'}
    for k in '12345678':
        if k in sections:
            det += f'<details{" open" if k in "12" else ""}><summary>{k}. {order[k]}</summary><pre>{esc(sections[k])}</pre></details>\n'
    page = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Devouring Dragon — OC status</title>
<meta name="description" content="The one clean sheet of everything about the Devouring Dragon — auto-generated, always current.">
<link rel="canonical" href="https://gm5206663-bit.github.io/soul-library/dd-status.html">
<style>{css}</style></head><body><div class="wrap">
<h1>The Devouring Dragon <span>·</span> OC status</h1>
<p class="sub">The one clean sheet of everything about him — auto-generated from the serial's authority files on every ship, never hand-edited. <a href="index.html">← The Library</a></p>
<div class="stamp">GENERATED {esc(NOW)} · {esc(STAMP)} · NEXT: {esc(next_line)}</div>
<h2>At a glance</h2>
<table>{glance}</table>
<h2>The full sheet</h2>
<p class="sub">Carried verbatim from HIS_STATUS_PANEL — the single authority (design estimates are the author's to correct).</p>
{det}
<h2>Life ledger — every chapter</h2>
<table><tr><th>#</th><th>DL</th><th>Title</th><th>Words</th><th>Where it left him</th></tr>{rows}</table>
<h2>Live edge</h2>
<p><b>{esc(STAMP)}.</b> {esc(note_inner)}</p>
<p><b>Next: {esc(next_line)}.</b></p>
<p class="foot">Staleness is enforced: the Sentinel checks this page's LIVE stamp against the chapters on disk. Source: soul-land-universal-kit · soul_land_devouring_dragon.</p>
</div></body></html>'''
    open(os.path.join(SITE, 'dd-status.html'), 'w', encoding='utf-8').write(page)
    print('dd-status.html written to site')
