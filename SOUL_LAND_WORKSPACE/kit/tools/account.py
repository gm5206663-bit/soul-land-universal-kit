#!/usr/bin/env python3
"""ACCOUNT CONTROL CENTRE — one command for the state of every book on the account.

    python3 tools/account.py index   --root DIR
    python3 tools/account.py report  --root DIR [--out-prefix NAME] [--only a,b]
    python3 tools/account.py freeze  --root DIR --out baseline.json
    python3 tools/account.py diff    --root DIR --baseline baseline.json
    python3 tools/account.py selftest

WHAT THIS IS FOR
----------------
The account is eighteen repositories, dozens of books, well over a million words
of prose, and dozens of check scripts that mostly cannot see each other. The
gates answer one question well: *is this chapter sound?* Nothing answered the
questions above that level — is the live directory the one that ships; does the
published site match the book; has a text quietly been given a second home; does
the README still describe the book it sits next to; does the same paragraph
appear in three chapters.

This is that layer. It runs the detectors in `account_checks.py`, declares its
coverage, carries its evidence, and writes three artifacts: JSON for a machine,
Markdown for a reader, HTML for a glance. It never edits a manuscript.

WHY BASELINES
-------------
Findings have stable ids. `freeze` records today; every later run can say NEW,
FIXED or STILL OPEN per finding instead of re-printing a wall of the same
numbers. Progress becomes measurable and a number can never be re-reported as
though it were fresh — the failure this house has made twice.
"""

import datetime
import hashlib
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import live_book_gate as lbg        # noqa: E402
import account_checks as checks     # noqa: E402

SEV_ORDER = {'hard': 0, 'advisory': 1}
OWNER = os.environ.get('GITHUB_OWNER', 'gm5206663-bit')


def _token(args):
    """A token for the one detector that reads GitHub itself. Optional: without
    one, the pages detector still works on public sites, just rate-limited."""
    if '--token-file' in args:
        try:
            return open(args[args.index('--token-file') + 1], encoding='utf-8').read().strip()
        except OSError:
            return None
    return os.environ.get('GITHUB_TOKEN')


# --------------------------------------------------------------------------
def run(root, only=None, pages=None, owner=OWNER):
    books = checks.registry(root)
    runs = []
    if not books:
        # A report over nothing must not read as a clean report. The house has
        # made this mistake once already: a stage that built 0 of 52 chapters
        # and called itself a success.
        runs.append(dict(detector='discovery',
                         findings=[checks.finding('scope-refusal', '-', '-', root, 'root',
                                                  f'no book found anywhere under {root} — a report '
                                                  f'over nothing is not a clean report',
                                                  evidence=f'walked {root} and found no chapter directory')],
                         coverage=dict(checks=0, total=0, unit='book(s)',
                                       text='0 of 0 books — nothing was examined'),
                         note='discovery found nothing; the run is not evidence of health'))
    if not only or 'gate' in only:
        runs.append(checks.check_gate(books))
    if not only or 'dupes' in only:
        runs.append(checks.check_dupes(books))
    if not only or 'two-homes' in only:
        runs.append(checks.check_two_homes(books))
    if not only or 'receipts' in only:
        runs.append(checks.check_receipts(books))
    if not only or 'publication' in only:
        runs.append(checks.check_publication(books))
    if not only or 'housekeeping' in only:
        runs.append(checks.check_housekeeping(root))
    if ('pages' in (only or ())) or (pages and not only):
        runs.append(checks.check_pages(books, owner, token=pages))

    findings = [x for r in runs for x in r['findings']]
    findings.sort(key=lambda f: (SEV_ORDER[f['severity']], f['repo'], f['book'], f['kind']))
    facts = next((r.get('facts', []) for r in runs if r['detector'] == 'gate'), [])

    report = dict(
        tool='account-control-centre', version=checks.VERSION,
        generated=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
        root=os.path.abspath(root),
        books=[dict(repo=b['repo'], book=b['book'],
                    live=os.path.relpath(b['live'], root) if b['live'] else None,
                    dead=[os.path.relpath(d, root) for d in b['dead']], note=b['note'])
               for b in books],
        facts=facts,
        coverage=[dict(detector=r['detector'], note=r['note'],
                       **{k: v for k, v in r['coverage'].items()}) for r in runs],
        findings=findings,
        summary=dict(
            books=len(books),
            chapters=len(facts),
            words=sum(f['words'] for f in facts),
            spoken=sum(f['dlg'] for f in facts),
            hard=len([f for f in findings if f['severity'] == 'hard']),
            advisory=len([f for f in findings if f['severity'] == 'advisory']),
            by_kind=_tally(findings, 'kind'),
            by_repo=_tally(findings, 'repo'),
        ),
    )
    return report


def label(f):
    """A book's full name once, not twice: repo/book only when they differ."""
    return f['repo'] if f['book'] in (f['repo'], '-') else f"{f['repo']}/{f['book']}"


def _tally(rows, key):
    out = {}
    for r in rows:
        out[r[key]] = out.get(r[key], 0) + 1
    return dict(sorted(out.items(), key=lambda kv: -kv[1]))


# --------------------------------------------------------------------------
def render_md(rep):
    s, L = rep['summary'], []
    A = L.append
    A(f"# ACCOUNT CONTROL CENTRE — {rep['generated']}")
    A('')
    A(f"`{rep['root']}` · tools v{rep['version']} · "
      f"**{s['books']} books · {s['chapters']} chapters · {s['words']:,} words · "
      f"{s['spoken']:,} spoken lines**")
    A('')
    A(f"**{s['hard']} hard finding(s)** — not the author's call · "
      f"**{s['advisory']} advisory** — the author decides.")
    A('')
    A('## 1. Coverage ledger')
    A('')
    A('Every detector states what it examined. A detector that examined nothing '
      'raises a finding instead of reporting a silent zero.')
    A('')
    A('| detector | scope | note |')
    A('|---|---|---|')
    for c in rep['coverage']:
        A(f"| {c['detector']} | {c['text']} | {c['note']} |")
    A('')
    A('## 2. Verdict by kind')
    A('')
    A('| kind | severity | law | count |')
    A('|---|---|---|---|')
    for k, n in s['by_kind'].items():
        sev, detail, doctrine = checks.law_of(k)
        A(f"| `{k}` | {sev} | {doctrine} | {n} |")
    A('')
    A('## 3. By repository')
    A('')
    A('| repository | findings | hard |')
    A('|---|---|---|')
    for r, n in s['by_repo'].items():
        hard = len([f for f in rep['findings'] if f['repo'] == r and f['severity'] == 'hard'])
        A(f"| {r} | {n} | {hard} |")
    A('')
    A('## 4. Findings')
    A('')
    cur = None
    for f in rep['findings']:
        head = f"{f['repo']} / {f['book']}"
        if head != cur:
            A(f"### {head}")
            A('')
            A('| severity | kind | where | what | evidence |')
            A('|---|---|---|---|---|')
            cur = head
        ev = f['evidence'].replace('|', '\\|').replace('\n', ' ')[:160]
        A(f"| {f['severity']} | `{f['kind']}` | {f['file']} | {f['detail']} | {ev} |")
    if not rep['findings']:
        A('_No findings._')
    A('')
    A('## 5. Books')
    A('')
    A('| repo | book | live directory | chapters | words | spoken | band |')
    A('|---|---|---|---|---|---|---|')
    by_book = {}
    for f in rep['facts']:
        by_book.setdefault((f['repo'], f['book']), []).append(f)
    for b in rep['books']:
        rows = by_book.get((b['repo'], b['book']), [])
        if not rows:
            A(f"| {b['repo']} | {b['book']} | {b['live'] or '—'} | 0 | — | — | — |")
            continue
        A(f"| {b['repo']} | {b['book']} | {b['live']} | {len(rows)} | "
          f"{sum(r['words'] for r in rows):,} | {sum(r['dlg'] for r in rows):,} | "
          f"{sorted({r['band'] for r in rows})} |")
    return '\n'.join(L) + '\n'


CHIP = {'hard': ('#8b1a1a', '#fdecec'), 'advisory': ('#7a5a00', '#fff7e0')}


def render_html(rep):
    s = rep['summary']
    e = html.escape
    rows = []
    for f in rep['findings']:
        fg, bg = CHIP[f['severity']]
        rows.append(
            f"<tr><td><span class=chip style='color:{fg};background:{bg}'>{f['severity']}</span></td>"
            f"<td class=k>{e(f['kind'])}</td><td>{e(f['repo'])}<br><span class=d>{e(f['book'])}</span></td>"
            f"<td class=d>{e(f['file'])}</td><td>{e(f['detail'])}"
            f"<div class=ev>{e(f['evidence'])}</div></td><td class=d>{e(f['law'])}</td></tr>")
    cov = ''.join(f"<tr><td class=k>{e(c['detector'])}</td><td>{e(c['text'])}</td>"
                  f"<td class=d>{e(c['note'])}</td></tr>" for c in rep['coverage'])
    kinds = ''.join(f"<tr><td class=k>{e(k)}</td>"
                    f"<td><span class=chip style='color:{CHIP[checks.law_of(k)[0]][0]};"
                    f"background:{CHIP[checks.law_of(k)[0]][1]}'>{checks.law_of(k)[0]}</span></td>"
                    f"<td>{e(checks.law_of(k)[2])}</td><td class=n>{n}</td></tr>"
                    for k, n in s['by_kind'].items())
    repos = ''.join(f"<tr><td class=k>{e(r)}</td><td class=n>{n}</td>"
                    f"<td class=n>{len([f for f in rep['findings'] if f['repo'] == r and f['severity'] == 'hard'])}</td></tr>"
                    for r, n in s['by_repo'].items())
    facts = ''.join(
        f"<tr><td class=k>{e(f['repo'])}<br><span class=d>{e(f['book'])}</span></td>"
        f"<td class=d>{e(f['file'])}</td><td class=n>{f['words']:,}</td><td class=n>{f['dlg']}</td>"
        f"<td class=n>{f['per_k']}</td><td>{e(f['band'])}</td><td class=n>{f['over60']}</td>"
        f"<td>{'exempt' if f['exempt'] else ''}</td></tr>" for f in rep['facts'])
    return f"""<!DOCTYPE html><html lang=en><head><meta charset=utf-8>
<title>Account Control Centre — {e(rep['generated'])}</title>
<style>
:root{{--ink:#14161a;--dim:#6b7280;--line:#e5e7eb;--bg:#fbfbfc;--card:#fff}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);
 font:15px/1.55 ui-serif,Georgia,'Times New Roman',serif}}
header{{padding:34px 30px 22px;border-bottom:3px solid var(--ink);background:var(--card)}}
h1{{margin:0 0 6px;font-size:27px;letter-spacing:-.2px}}
h2{{margin:38px 0 10px;font-size:17px;text-transform:uppercase;letter-spacing:1.4px;
 border-bottom:1px solid var(--line);padding-bottom:6px}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 30px 70px}}
.sub{{color:var(--dim);font-size:14px}}
.kpi{{display:flex;flex-wrap:wrap;gap:10px;margin:20px 0 0}}
.kpi div{{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 14px;min-width:150px}}
.kpi b{{display:block;font-size:22px}}
.kpi span{{color:var(--dim);font-size:12px;text-transform:uppercase;letter-spacing:1px}}
table{{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--line);
 border-radius:8px;overflow:hidden;font-family:ui-sans-serif,system-ui,Segoe UI,sans-serif;font-size:13px}}
th{{text-align:left;background:#f3f4f6;padding:9px 11px;font-size:11px;text-transform:uppercase;
 letter-spacing:.9px;color:#374151}}
td{{padding:9px 11px;border-top:1px solid var(--line);vertical-align:top}}
tr:hover td{{background:#fcfcfd}}
.chip{{display:inline-block;padding:1px 8px;border-radius:99px;font-size:11px;font-weight:600;
 letter-spacing:.4px;text-transform:uppercase}}
.k{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px}}
.d{{color:var(--dim)}}
.n{{text-align:right;font-variant-numeric:tabular-nums}}
.ev{{margin-top:5px;color:#374151;font-style:italic;border-left:2px solid var(--line);padding-left:8px}}
.legend{{color:var(--dim);font-size:13px;margin:8px 0 0}}
details{{margin:26px 0}}summary{{cursor:pointer;font-weight:600}}
footer{{border-top:1px solid var(--line);margin-top:44px;padding-top:14px;color:var(--dim);font-size:12.5px}}
</style></head><body>
<header><div class=wrap style="padding-bottom:0">
<h1>Account Control Centre</h1>
<div class=sub>{e(rep['root'])} · generated {e(rep['generated'])} · tools v{e(rep['version'])} ·
 detectors declare their own coverage, carry their evidence, and keep stable ids</div>
<div class=kpi>
 <div><b>{s['books']}</b><span>books</span></div>
 <div><b>{s['chapters']}</b><span>chapters</span></div>
 <div><b>{s['words']:,}</b><span>words</span></div>
 <div><b>{s['spoken']:,}</b><span>spoken lines</span></div>
 <div><b style="color:#8b1a1a">{s['hard']}</b><span>hard findings</span></div>
 <div><b style="color:#7a5a00">{s['advisory']}</b><span>advisory</span></div>
</div></div></header>
<div class=wrap>

<h2>1 · Coverage — what was actually read</h2>
<table><tr><th>detector</th><th>scope examined</th><th>note</th></tr>{cov}</table>
<p class=legend>A detector that examined nothing would say so here and raise a finding.
 Absence is never reported as health.</p>

<h2>2 · Verdict by kind</h2>
<table><tr><th>kind</th><th>severity</th><th>the law behind it</th><th>count</th></tr>{kinds}</table>
<p class=legend><b>Hard</b> is not the author's call. <b>Advisory</b> is reported, not fatal —
 the band, the dialogue bar, a refrain that may be deliberate.</p>

<h2>3 · By repository</h2>
<table><tr><th>repository</th><th>findings</th><th>hard</th></tr>{repos}</table>

<h2>4 · Findings, with evidence</h2>
<table><tr><th>severity</th><th>kind</th><th>where</th><th>file</th><th>what · evidence</th>
<th>law</th></tr>{''.join(rows)}</table>

<details><summary>5 · Every chapter measured ({len(rep['facts'])} files)</summary>
<table><tr><th>repo / book</th><th>chapter</th><th>words</th><th>spoken</th><th>per 1k</th>
<th>band</th><th>over 60</th><th></th></tr>{facts}</table></details>

<footer>Generated by <span class=k>tools/account.py</span> on the house gate
 (<span class=k>tools/live_book_gate.py</span>). Detectors never edit a manuscript;
 everything hard is reported for the author or repaired deliberately, never silently.</footer>
</div></body></html>"""


# --------------------------------------------------------------------------
def code_hash():
    import hashlib as _h
    here = os.path.dirname(os.path.abspath(__file__))
    src = b''.join(open(os.path.join(here, f), 'rb').read()
                   for f in ('account_checks.py', 'live_book_gate.py')
                   if os.path.isfile(os.path.join(here, f)))
    return _h.sha1(src).hexdigest()[:12]


def freeze(rep, path):
    base = dict(frozen=rep['generated'], root=rep['root'],
                tools_version=rep['version'], code=code_hash(),
                findings={f['id']: dict(kind=f['kind'], severity=f['severity'], repo=f['repo'],
                                        book=f['book'], file=f['file'], detail=f['detail'])
                          for f in rep['findings']})
    json.dump(base, open(path, 'w', encoding='utf-8'), indent=1)
    return len(base['findings'])


def diff(rep, path):
    base = json.load(open(path, encoding='utf-8'))
    old, now = base['findings'], {f['id']: f for f in rep['findings']}
    new = [f for i, f in now.items() if i not in old]
    fixed = [old[i] for i in old if i not in now]
    still = [f for i, f in now.items() if i in old]
    out = [f"vs baseline frozen {base['frozen']} ({len(old)} finding(s), code {base.get('code', '?')})"]
    if base.get('root') and os.path.abspath(base['root']) != os.path.abspath(rep['root']):
        # A 10-book root diffed against a 24-book baseline reported "875 fixed"
        # the first time this was tried. Different roots are different accounts;
        # the comparison is meaningless and has to say so.
        out.append(f"  WARNING: this baseline was frozen against {base['root']}, you are diffing "
                   f"{rep['root']} — different roots are different accounts. "
                   f"NEW/FIXED here mean nothing until the roots match.")
    if base.get('code') and base['code'] != code_hash():
        out.append('  WARNING: the detectors changed since this baseline was frozen — '
                   'NEW/FIXED are not comparable. Re-freeze after any change to a detector.')
    out += [
           f"  NEW        {len(new)}", f"  FIXED      {len(fixed)}",
           f"  STILL OPEN {len(still)}"]
    for f in sorted(new, key=lambda f: (SEV_ORDER[f['severity']], f['repo'])):
        out.append(f"    + [{f['severity']}] {label(f)} {f['kind']}: {f['detail'][:110]}")
    for f in sorted(fixed, key=lambda f: f['repo']):
        out.append(f"    - [{f['severity']}] {label(f)} {f['kind']}: {f['detail'][:110]}")
    return '\n'.join(out), len(new)


# --------------------------------------------------------------------------
def main():
    args = sys.argv[1:]
    if '--selftest' in args:
        os.execv(sys.executable, [sys.executable,
                                  os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                               'account_selftest.py')])
    cmd = args[0] if args and not args[0].startswith('-') else 'report'
    root = args[args.index('--root') + 1] if '--root' in args else os.getcwd()
    only = args[args.index('--only') + 1].split(',') if '--only' in args else None
    prefix = args[args.index('--out-prefix') + 1] if '--out-prefix' in args else 'account_report'

    if cmd == 'index':
        books = checks.registry(root)
        for b in books:
            n = len(checks.book_files(b))
            print(f"  {b['repo']:34s} {b['book']:34s} "
                  f"{os.path.relpath(b['live'], root) if b['live'] else 'REFUSED':38s} {n:3d} ch")
        print(f"\n  {len(books)} book(s) under {os.path.abspath(root)}")
        return 0

    rep = run(root, only, pages=_token(args) if ('--pages' in args or 'pages' in (only or [])) else None)

    if cmd == 'freeze':
        out = args[args.index('--out') + 1] if '--out' in args else 'baseline.json'
        n = freeze(rep, out)
        print(f"baseline frozen: {n} finding(s) → {out}")
        return 0

    if cmd == 'diff':
        path = args[args.index('--baseline') + 1] if '--baseline' in args else 'baseline.json'
        text, new = diff(rep, path)
        print(text)
        return 1 if new else 0

    json.dump(rep, open(prefix + '.json', 'w', encoding='utf-8'), indent=1)
    open(prefix + '.md', 'w', encoding='utf-8').write(render_md(rep))
    open(prefix + '.html', 'w', encoding='utf-8').write(render_html(rep))
    s = rep['summary']
    print(f"ACCOUNT CONTROL CENTRE — {s['books']} books · {s['chapters']} chapters · "
          f"{s['words']:,} words · {s['spoken']:,} spoken lines")
    for c in rep['coverage']:
        print(f"  COVERAGE {c['detector']:12s} {c['text']}")
    print(f"  VERDICT: {s['hard']} hard · {s['advisory']} advisory")
    for k, n in s['by_kind'].items():
        print(f"    {n:4d}  {k}  [{checks.law_of(k)[0]}]")
    print(f"  wrote {prefix}.json · {prefix}.md · {prefix}.html")
    return 1 if s['hard'] else 0


if __name__ == '__main__':
    sys.exit(main())
