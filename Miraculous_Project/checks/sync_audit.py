#!/usr/bin/env python3
# Layer 5 — SYNC AUDIT. The sync ritual: after every chapter the writer updates
# state.json AND the footer; this layer cross-checks the two against each other
# for EVERY chapter (the chain, not just the newest).
import io, re, glob, os, sys, json
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W = print
fails = []

nums = sorted(int(re.findall(r'\d+', f)[0]) for f in glob.glob('chapters/chapter_*.md'))
W('=' * 62)
W('== Layer 5: sync_audit.py (state.json vs every footer) ==')
if not nums:
    W('  no chapters yet — nothing to cross-check; state.json is the opening board.')
    st = json.load(io.open('checks/state.json', encoding='utf-8'))
    if st.get('chapter', 0) != 0:
        fails.append(f'state.json chapter={st["chapter"]} but disk has 0 chapters')
    for x in fails: print('  FAIL', x)
    print(f'sync_audit: {len(fails)} FAIL' if fails else 'sync_audit: OK (0 chapters)')
    sys.exit(1 if fails else 0)

st = json.load(io.open('checks/state.json', encoding='utf-8'))
for n in nums:
    t = io.open(f'chapters/chapter_{n:02d}.md', encoding='utf-8').read()
    rec = st.get(str(n))
    if rec is None:
        fails.append(f'ch{n}: no record in state.json (sync ritual skipped?)')
        continue
    checks = {
        'resonance': (re.search(r'resonance:\s*\*\*(\d+)\*\*/100', t), lambda m: int(m.group(1))),
        'cuff': (re.search(r'Cuff:\s*\*\*([^*]+)\*\*', t), lambda m: m.group(1).strip()),
        'evolution': (re.search(r'Evolution:\s*\*\*([^*]+)\*\*', t), lambda m: m.group(1).strip()),
        'akuma': (re.search(r'akumatized this chapter:\s*\*\*(\d+)\*\*', t), lambda m: int(m.group(1))),
        'butterflies': (re.search(r'Butterflies shown:\s*\*\*(\d+)\*\*', t), lambda m: int(m.group(1))),
    }
    for k, (m, conv) in checks.items():
        if not m:
            fails.append(f'ch{n}: footer missing field {k}')
            continue
        if rec.get(k) is not None and rec[k] != conv(m):
            fails.append(f'ch{n}: footer {k}={conv(m)} but state.json says {rec[k]}')
    mk = re.search(r'^Kamé:\s*\*\*([^*]+)\*\*', t, re.M)
    if mk and rec.get('kame') is not None and mk.group(1).strip() != rec['kame']:
        fails.append(f'ch{n}: footer Kamé="{mk.group(1).strip()}" but state.json says "{rec["kame"]}"')
    mo = re.search(r'OC Voice[:\s]*\*?\*?(\d+)\s*turns', t)
    if mo and rec.get('oc_turns') is not None and int(mo.group(1)) != rec['oc_turns']:
        fails.append(f'ch{n}: footer OC turns={mo.group(1)} but state.json says {rec["oc_turns"]}')
    md = re.search(r'D-rows Cited[:\s]*(.+)', t)
    if md:
        cited = {x.strip() for x in md.group(1).replace('，', ',').split(',') if re.match(r'^[A-Z]+-\d+$|^REVEAL-[A-Z]+$', x.strip())}
        if rec.get('d_rows') is not None and cited != set(rec['d_rows']):
            fails.append(f'ch{n}: footer D-rows {sorted(cited)} but state.json says {sorted(rec["d_rows"])}')
    e = t.find('## End of Chapter')
    foot = t[e:] if e != -1 else ''
    if not re.search(r'###\s*Panel\b', foot):
        fails.append(f'ch{n}: footer missing "### Panel" line (L-17 perspective panel — name the non-Keal beat, or the reason the surface was unreachable)')

W(f'  cross-checked {len(nums)} chapters against state.json')
for x in fails: print('  FAIL', x)
print(f'sync_audit: {len(fails)} FAIL' if fails else 'sync_audit: OK')
sys.exit(1 if fails else 0)
