#!/usr/bin/env python3
# THE BRIEFING — one command, the whole cockpit. Runs Layer 8 (world tick) and the
# board + divergence engine, and prepends the chapter targets: position, the
# dialogue dial, the cliff-rotation rule, the prewrite checklist. Output is also
# written to BRIEF.md so the brief itself is citable.
# Usage:  python3 checks/brief.py     (MANDATORY STEP 0 before every chapter)
import io, json, re, subprocess, sys, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W = print
out = []
def P(s=''):
    out.append(s); W(s)

st = json.load(io.open('checks/state.json', encoding='utf-8'))
cur = max(int(k) for k in st)
e = st[str(cur)]
lastf = f'chapters/chapter_{cur:02d}.md'
t = io.open(lastf, encoding='utf-8').read()
tail = [l for l in t[:t.find('## End of Chapter')].strip().split('\n') if l.strip() and set(l.strip()) - set('-*')][-1]

P('=' * 62)
P(f'THE BRIEFING — for chapter {cur+1} (position: end of chapter {cur})')
P(f'  carry: rank {e.get("rank")} · SP {e.get("sp")} · hawk {e.get("hawk")} · ledger {e.get("ledger")}')
P(f'  last line on record: "{tail[:96]}{"…" if len(tail) > 96 else ""}"')
P('  TARGETS (STYLE_GOLD — the dial, not a default):')
P('    · dialogue: lesson 44–66% · hush 8–15% · standard 13–30% — pick by chapter type, say which')
P('    · cliff: ROTATE — after a short-stark cliff prefer long-lyrical or ongoing-process; never the same weapon twice')
P('    · gold: 1–2 patterns breathing (the board tracks the motifs); never a checklist')
P('    · LH voice ≥ 4 turns; presence ≥ 5 markers (Law oo); footer: D-rows cited (Layer 7)')
P('    · COVERAGE IS ELASTIC (LAW pp §7): spend 1–3 canon chapters as the scenes demand; fetch ahead mid-arc; declare the span in the header')
P('    · THE RECORD STACK: 3+ qualified eyes on a page = the stack reads aloud (POWER_MODEL §RECORD STACK) — never unwritten again')
P('  CHECKLIST: [ ] answer the world pressure  [ ] answer the FORWARD-TICK  [ ] fetch canon (as ORE)')
P('              [ ] derive, don\'t obey — and don\'t manufacture  [ ] numbers need sources  [ ] sync all docs')
P('=' * 62)
P('  🔴 THE ORIGINAL-LIFE COCKPIT (LAW bh1 — canon is the spine; the OC\'s life between canon beats is OURS to CREATE):')
P('    [ ] INVENT THIS CHAPTER — name at least one ORIGINAL thing the OC\'s stage of life demands:')
P('        an original scene · character · object · place · craft beat · institution beat · a lesson that exists for HIM')
P('    [ ] What does HIS life need today that canon never builds? (the forge life, the Shrek courtyards, the medic')
P('        exam, the boys\' room, the second soul\'s maturing (crossings, not trickles), the convergence body (five')
P('        lines — anvil/hawk/jiao/intent/adaptation — medics get five signatures, no bracket), the SPIRITUAL SEA')
P('        shown (the jiao\'s dark water below, the hawk\'s storm-sky above), the hawk\'s bloodline steps, his own')
P('        arts) — check SHREK_ORIGINAL_LIFE_DOSSIER.md (outer original life) + INNER_COUNTRY.md')
P('        (the spiritual-sea narrative system: geography, threads C0-C6, the Abyssal Syllable, K3 rehearsal);')
P('        grow both files when something new is born.')
P('    [ ] GROWTH-NEVER-STILL (LAW bh2): every tracked organ is either shown growing/learning/saving/upgrading')
P('        today OR is knowingly rested with cause — nothing freezes; a held lock is not a frozen organ.')
P('    [ ] A thing learned is a thing UPGRADED on-page; a thing paid for is a thing SAVED into the docs.')
P('  🔴 UNBOUNDED BRIEF (bh4): the assignment is never the perimeter — sweep for what was NEVER flagged; extend')
P('    this teaching past its words; BUILD the thing the story needs that does not exist yet; propose original material.')
P('=' * 62)

for cmd in ['python3 checks/world_tick.py', 'python3 checks/prewrite_board.py', 'python3 checks/divergence_engine.py']:
    r = subprocess.run(cmd.split(), capture_output=True, text=True)
    P(r.stdout.rstrip())
    if r.returncode:
        P(f'  !! {cmd.split()[1]} exited {r.returncode}')

io.open('BRIEF.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
