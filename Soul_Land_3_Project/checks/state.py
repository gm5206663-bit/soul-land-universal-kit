#!/usr/bin/env python3
"""STATE — single source of truth for the protagonist's progression lines.

Derived FROM the chapter footers (which are the authoritative record), then written to
checks/state.json. verify.py, verify2.py, verify_ensemble.py and build_status.py all read
that file, so nothing is hardcoded in two places.

Usage:
    python3 checks/state.py            # rebuild checks/state.json from the chapters
    python3 checks/state.py --show     # print the derived state
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, 'chapters')
OUT = os.path.join(ROOT, 'checks', 'state.json')

RE_RANK = re.compile(r'Ranks at chapter end:\*\*\s*Lin Hao \*{0,2}(\d\d)')
# 🔴 `*` MUST be in the character class. Footers write the chain as
#   "spiritual power **281 → 289**"
# and without `*` the class stopped after "281 → ", so derive() silently recorded the
# START of the chain as the chapter's value. ch62 was read as 281 instead of 289, and the
# error was invisible because the footer was self-consistent.
RE_SP = re.compile(r'spiritual power \*{0,2}([\d\s→,().a-z\-*]*)')

# The rank brackets and their titles (THE_CODEX.md Cultivation Order)
BRACKETS = [(1, 10, 'Soul Scholar'), (11, 20, 'Soul Master'), (21, 30, 'Soul Grandmaster'),
            (31, 40, 'Soul Elder'), (41, 50, 'Soul Ancestor'), (51, 60, 'Soul King'),
            (61, 70, 'Soul Emperor'), (71, 80, 'Soul Sage'), (81, 90, 'Soul Douluo'),
            (91, 100, 'Titled Douluo')]

# 🔴 DERIVED, NOT HARDCODED (changed 2026-08-30, ch71 — §4.13: one source, everything else derived).
# This used to be `EFFECTIVE_REALM = 'Soul King'` / `51, 60`, and that exact string was ALSO
# hardcoded in build_status.py, build_continuation.py, verify_ensemble.py and two doc generators —
# five copies of one belief. The fourth ring changes the belief, so all five had to be found by
# hand. It is now computed from his rank and ring count, and every consumer reads state.json.
#
# THE TWO AXES (THE_CODEX.md §4.12) — the OVERALL COMBAT axis:
#   3 purple rings + Sword Intent + the Adaptation Talent => +11..20 ranks above paper  (ch40-ch70)
#   4th ring BLACK + top-level martial soul + the Domain    => +16..25 ranks above paper  (ch71+)
# Rationale, on the record: the fourth ring is ten-thousand-year (a tier canon reserves for people
# like Wu Zhangkong), the martial soul goes peak-high -> TOP-LEVEL, and the Domain is the martial
# soul's innate ability. Canon's own benchmark is that a battle armor master is "twenty soul ranks
# stronger than any soul master of the same soul power rank" (c227) — he is now in that neighbourhood
# without wearing a stitch of armor. He does NOT go further: he still has not used his full power.
def effective_of(rank, ring_count):
    if ring_count >= 4:
        return 'Soul Emperor', rank + 16, rank + 25
    return 'Soul King', rank + 11, rank + 20

SMITH_TITLES = [(1, 2, 'Master'), (3, 4, 'Grandmaster'), (5, 6, 'Master Craftsman'),
                (7, 8, 'Saint Craftsman'), (9, 9, 'Divine Craftsman')]


def realm_of(rank):
    return next((t for lo, hi, t in BRACKETS if lo <= rank <= hi), 'unranked')


def smith_title(rk):
    return next((t for lo, hi, t in SMITH_TITLES if lo <= rk <= hi), '')


def _last_num(pattern, text, cast=int):
    hits = re.findall(pattern, text)
    return cast(hits[-1]) if hits else None


def derive():
    ranks, sps, hawks, smith, rings = {}, {}, {}, {}, {}
    ledgers = {}          # 🔴 per-chapter: the ledger is a progression, not a constant
    ledger, latest = None, 0

    for f in sorted(os.listdir(CH)):
        if not f.endswith('.md'):
            continue
        n = int(f[8:10])
        full = open(os.path.join(CH, f), encoding='utf-8').read()
        footer = full.split('## End of Chapter')[1] if '## End of Chapter' in full else ''
        latest = max(latest, n)

        m = RE_RANK.search(footer)
        if m:
            ranks[n] = int(m.group(1))

        # 🔴 Scope spiritual power to LIN HAO's own line. The ensemble block added by
        # apply_ensemble.py lists Gu Yue's canon 153 and Wang Jinxi's 18, and an unscoped search
        # picked Gu Yue's 153 up as HIS value for ch10-20 — feeding wrong data into every
        # downstream check. Cut the ensemble block off before searching.
        lh_footer = footer.split("### Ensemble — canon-verified state")[0]
        # 🔴 take the LAST match that actually CONTAINS a number. ch62's Chapter Summary
        # contains the narrative phrase "eight points from spiritual power from WATCHING" and
        # RE_SP matched it first, captured "from ", found no digits, and the chapter silently
        # recorded no spiritual power at all — so state.json reported ch61's value as current.
        cands = [mm for mm in RE_SP.finditer(lh_footer) if re.search(r'\d{3}', mm.group(1))]
        m = cands[-1] if cands else None
        if m:
            # Footer forms seen in the wild:
            #   "spiritual power 145"                  -> 145
            #   "spiritual power 145 -> 152"           -> 152  (the END of the chain)
            #   "spiritual power 124 (was 118 at ...)" -> 124  (the parenthetical is the PAST)
            span = re.sub(r'\(\s*was\b[^)]*', '', m.group(1))
            # 🔴 take the LAST 3-digit number in the span, always. The span can be
            #   "281 → 289**"   (chain — want 289)
            #   "289**"         (single — want 289)
            #   "281 (281 → 289" (parenthetical restatement — want 289)
            # The old code special-cased the arrow with a regex that could not see through the
            # `**` sitting between the arrow and the number, and then fell back to nums[0] —
            # the START of the chain. ch62 was recorded as 281 instead of 289.
            nums = re.findall(r'\d{3}', span)
            if nums:
                sps[n] = int(nums[-1])

        # hawk age — "hawk 1,399" / "🌪 hawk 934 → 942"
        h = re.findall(r'hawk\D{0,6}([\d,]{3,6})\s*(?:→\s*([\d,]{3,6}))?', footer)
        if h:
            val = (h[-1][1] or h[-1][0]).replace(',', '')
            if val.isdigit():
                hawks[n] = int(val)

        # Smithing rank — MUST be anchored to the 🔨 marker and to Lin Hao's own line.
        # An unanchored r'(\d)(?:st|nd|rd|th) rank' picks up "a fifth-rank teacher" and
        # returns 5 when the true rank is 4. That bug shipped once; do not reintroduce it.
        sm = re.findall(r'🔨[^\n]{0,20}?(\d)\s*(?:st|nd|rd|th)\s*rank', footer)
        if sm:
            smith[n] = int(sm[-1])
        else:
            li2 = footer.find('Lin Hao:')
            if li2 >= 0:
                sm2 = re.findall(r'(\d)\s*(?:st|nd|rd|th)\s*rank', footer[li2:li2 + 500])
                if sm2:
                    smith[n] = int(sm2[0])

        # ring count + colour, from Lin Hao's own state line
        li = footer.find('Lin Hao:')
        seg = footer[li:li + 500] if li >= 0 else footer
        # 🔴 EXTENDED ch71 (2026-08-30). The regex used to stop at "three ... purple", which was
        # correct for 70 chapters and wrong the moment the fourth ring arrived. The FOURTH RING
        # LAW locks it as BLACK (ten-thousand-year => black, canon c260). The count is what
        # derives the rank ceiling, so it records the colour of the HIGHEST ring.
        # 🔴 FIXED 2026-08-30 (ch71). TWO bugs here, and I introduced the second one myself.
        #
        # BUG 1 (mine, this morning): I rewrote the pattern to `(N)\s*(colour)\s*rings?` and took
        # the MAX match. But ch71's footer writes the TOTAL unqualified — "FOUR rings — three
        # purple, one BLACK" — and "FOUR rings" has no colour word before "rings", so the pattern
        # matched NOTHING and the chapter inherited ch70's three rings. A check I "fixed" without
        # running it against the string it had to parse. The lesson is §4.8: run the real thing.
        #
        # BUG 2 (original): the old pattern was the same shape, so before ch71 it happened to work
        # only because every footer said "three purple rings" with the colour adjacent.
        #
        # The correct parse: count and colour are INDEPENDENT. Take the largest ring count
        # mentioned (the total, whether qualified or not), and take the highest-tier colour
        # present, since the ceiling is driven by the count and the colour is descriptive.
        _NUM = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
        _cnts = [int(w) if w.isdigit() else _NUM[w.lower()]
                 for w in re.findall(r'\b(four|three|two|one|4|3|2|1)\s*rings?\b', seg, re.I)]
        _cols = [c.lower() for c in
                 re.findall(r'\b(black|purple|yellow|white)\s*rings?\b', seg, re.I)]
        # a mixed set is written "three purple rings and one black ring" — singular counts too
        if _cnts:
            _TIER = ['white', 'yellow', 'purple', 'black']
            _col = max(_cols, key=_TIER.index) if _cols else 'purple'
            rings[n] = {'count': max(_cnts), 'colour': _col}

        # 🔴 Scoped to Lin Hao's own part of the footer. The ensemble block lists other
        # characters' numbers and an unscoped search can pick the wrong one up.
        # 🔴 take the LAST number, not the first: the Character Progression block writes a
        # chain ("ledger 107 → 109") and the Character States block writes the end value.
        # re.search returned the chain's START and ch62 was recorded as 107 instead of 109.
        lm = re.findall(r'ledger[^\n]{0,24}?(\d+)', lh_footer)
        if lm:
            ledger = int(lm[-1])
            ledgers[n] = ledger

    if not ranks:
        raise SystemExit('state.py: no chapter footers parsed — check the footer format')

    cur_rank = ranks[max(ranks)]
    cur_rings = rings[max(rings)] if rings else {'count': 0, 'colour': None}

    # The ceiling is DERIVED from the ring count, never hardcoded. Hardcoding 30 here is
    # exactly what went stale: the third ring was bestowed in ch40 and the wall moved to 40.
    # Bracket law (THE_CODEX.md Cultivation Order): N rings covers ranks N*10+1 .. (N+1)*10.
    #   1 ring 11-20 Soul Master | 2 rings 21-30 Soul Grandmaster | 3 rings 31-40 Soul Elder
    n = cur_rings['count']
    floor, ceiling = n * 10 + 1, (n + 1) * 10
    band = realm_of(ceiling)
    if cur_rank >= ceiling:
        reason = (f"AT THE WALL — {n} rings cover ranks {floor}-{ceiling} ({band}); "
                  f"the {n+1}th ring is required to pass {ceiling}")
    else:
        reason = (f"{n} rings cover ranks {floor}-{ceiling} ({band}); "
                  f"{ceiling - cur_rank} ranks of headroom before the {n+1}th ring is needed")

    _eff_realm, _eff_lo, _eff_hi = effective_of(cur_rank, cur_rings['count'])

    return {
        'latest_chapter': latest,
        'current_rank': cur_rank,
        'current_realm': realm_of(cur_rank),
        'current_spiritual_power': sps[max(sps)],
        'current_ledger': ledger,
        'current_hawk_years': hawks[max(hawks)] if hawks else None,
        'current_smith_rank': smith[max(smith)] if smith else None,
        'current_smith_title': smith_title(smith[max(smith)]) if smith else None,
        'rings': cur_rings,
        # 🔴 effective combat power — DERIVED from rank + ring count (see effective_of above).
        # THE_CODEX.md §THE TWO AXES. Every consumer reads this, none of them hardcode it.
        'effective_realm': _eff_realm,
        'effective_rank_band': [_eff_lo, _eff_hi],
        'effective_rank_delta': [_eff_lo - cur_rank, _eff_hi - cur_rank],
        'rank_ceiling': ceiling,
        'rank_ceiling_reason': reason,
        'ledger_by_chapter': {str(k): v for k, v in sorted(ledgers.items())},
        'rank_by_chapter': {str(k): v for k, v in sorted(ranks.items())},
        'spiritual_power_by_chapter': {str(k): v for k, v in sorted(sps.items())},
        'hawk_by_chapter': {str(k): v for k, v in sorted(hawks.items())},
        'smith_by_chapter': {str(k): v for k, v in sorted(smith.items())},
    }


def main():
    st = derive()
    if '--show' in sys.argv:
        print(json.dumps(st, indent=2))
        return
    with open(OUT, 'w', encoding='utf-8') as fh:
        json.dump(st, fh, indent=2)
    print(f"state.json written — ch{st['latest_chapter']}: rank {st['current_rank']} "
          f"({st['current_realm']}), spiritual power {st['current_spiritual_power']}, "
          f"ledger {st['current_ledger']}, hawk {st['current_hawk_years']}, "
          f"{st['rings']['count']} {st['rings']['colour']} rings, "
          f"smith {st['current_smith_rank']} ({st['current_smith_title']}), "
          f"effective {st['effective_realm']} {st['effective_rank_band']}")


if __name__ == '__main__':
    main()
