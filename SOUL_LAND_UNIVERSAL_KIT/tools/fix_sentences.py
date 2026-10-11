#!/usr/bin/env python3
"""SENTENCE REPAIR — split over-long sentences without changing one word.

    python3 fix_sentences.py --report  FILE|DIR...
    python3 fix_sentences.py --apply   FILE|DIR...
    python3 fix_sentences.py --selftest

The house law (tools/ship_chapter.py, style_gate.py, FOUNDATION) caps a
sentence at 60 words. A 154-word sentence is not a style choice inside a
pipeline that dies on it — it is a defect that got past a gate.

This tool splits such a sentence at a boundary the prose already contains:
after an em dash, at a semicolon, before ", and / but / so / because / which …",
or at a plain comma when nothing stronger exists. It moves no words and drops
none; it converts the boundary into a full stop and capitalises the continuation.

WHAT IT REFUSES TO DO
---------------------
  * It never splits inside a quoted span. A split that lands mid-dialogue
    changes who is speaking; the tool checks quote parity at every candidate
    and skips the ones inside quotes.
  * It never leaves a fragment. Both halves must keep at least 12 words.
  * It never touches a heading, a panel line, a planning line, or the
    production block after the footer.
  * It never guesses silently: a sentence with no usable boundary is REPORTED
    as needing a writer, not mechanically butchered.

Every applied edit is verified before it is written: the file's word sequence,
its quote count, and every other sentence must be identical afterwards, and the
sentence it touched must be under the cap. A repair that cannot prove it
changed nothing but punctuation does not get written.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import live_book_gate as lbg   # noqa: E402

CAP = 60
MIN_PART = 12                  # a split half smaller than this is a fragment

#: Boundaries, strongest first. The tool prefers a boundary that carries
#: meaning — a dash, a semicolon, a subordinating conjunction — and falls back
#: to a plain comma only when the sentence offers nothing better.
STRONG = re.compile(
    r'(?<=\s)—\s+|(?<=\s)--\s+|;\s+'
    r'|,\s+(?:and|but|so|then|yet|or|because|while|though|although|after|before|'
    r'as|when|where|which|who|why|if|since|that|and then|and yet|and so)\s+',
    re.I)
PLAIN = re.compile(r',\s+')
#: Last resort: a conjunction with no comma at all. The supergirl serial is
#: written almost entirely without commas, so without this the tool would report
#: every long sentence there as unsplittable.
BARE = re.compile(r'\s+(?:and|but|so|because|while|though|although|then|yet)\s+', re.I)


def tokens(t):
    """The count the LAW uses. live_book_gate measures a sentence with
    len(s.split()) — every whitespace token, including a dash standing alone.
    This tool first counted only real words, so it saw a 59-word sentence where
    the gate saw 61 and reported a file clean while the gate still refused it.
    A repair tool that measures differently from the law it repairs for is
    repairing to its own opinion. Cap decisions use this function."""
    return len(t.split())


def words_of(t):
    return [re.sub(r'\W+', '', w).lower() for w in t.split() if re.sub(r'\W+', '', w)]


def quote_balanced(t):
    """True when the text so far sits outside any quoted span."""
    return (t.count('"') % 2 == 0
            and t.count('\u201c') == t.count('\u201d'))


def candidates(sent, rx):
    out = []
    for m in rx.finditer(sent):
        before, after = sent[:m.start()], sent[m.end():]
        if len(words_of(before)) < MIN_PART or len(words_of(after)) < MIN_PART:
            continue
        if not quote_balanced(before):
            continue
        out.append(m)
    return out


def split_once(sent):
    """One split, or None if this sentence offers no safe boundary."""
    n = tokens(sent)
    for rx in (STRONG, PLAIN, BARE):
        cs = candidates(sent, rx)
        if not cs:
            continue
        # prefer the boundary whose split point sits nearest the middle
        def score(m):
            left = len(words_of(sent[:m.start()]))
            return abs(left - n * 0.45)
        m = min(cs, key=score)
        # The tail starts at m.start(), not m.end(): the connector ("and",
        # "then", "but") is part of the prose and must survive the split. Ending
        # the tail at m.end() deleted it — a repair tool that quietly removes a
        # word is worse than the defect it was written to fix.
        head = sent[:m.start()].rstrip()
        tail = re.sub(r'^[\s,;—\-]+', '', sent[m.start():])
        tail = tail[0].upper() + tail[1:] if tail and tail[0].islower() else tail
        # Return TWO parts, not one joined string. Returning the joined text and
        # appending it as a single unit is why this tool re-split the same
        # sentence six times, gave up, and reported every sentence as
        # unsplittable while its own selftest watched.
        return head.rstrip(' ,;—-') + '.', tail
    return None


def split_all(sent, log):
    """Split until under the cap. Returns (text, splits) or None if impossible."""
    splits = 0
    work = [sent]
    for _ in range(6):                     # a 400-word sentence needs a few
        nxt, changed = [], False
        for s in work:
            if tokens(s) > CAP:
                got = split_once(s)
                if got:
                    nxt.extend(got)
                    splits += 1
                    changed = True
                    continue
                nxt.append(s)
            else:
                nxt.append(s)
        work = nxt
        if not changed:
            break
    if any(tokens(s) > CAP for s in work):
        log.append(('unsplittable', sent))
        return None
    return (' '.join(work), splits)


QUOTE_CHARS = '"\u201c\u201d\u2019'


def sentence_spans(s):
    """Sentence spans that keep their closing quote.

    lbg.sentences() consumes a closing quote as part of the separator between
    sentences — harmless when you only measure lengths, fatal when you REBUILD
    the line: joining the sentences back with a space deleted every closing
    quote that followed a full stop. That is how this tool's own guard caught
    it (\"quote count changed\"), on a line reading `... "No soul power.
    Cannot cultivate." The boy ...`. Spans fix it at the source: everything
    outside a span is copied through byte for byte.
    """
    out, start = [], 0
    for m in lbg.SENT_SPLIT.finditer(s):
        end = m.start()
        if end < len(s) and s[end] in QUOTE_CHARS:
            end += 1                       # the closing quote belongs to the sentence
        out.append((start, end))
        start = m.end()
    out.append((start, len(s)))
    return out


def repair_text(body, log):
    """Rewrite one body, copying every separator exactly. Returns (text, splits)."""
    out, touched = [], 0
    for line in body.split('\n'):
        s = line.strip()
        if (not s or re.match(r'#+\s', s) or s.startswith(('>', '|', '- ', '* '))
                or lbg.PLAN_LINE_RX.search(line)):
            out.append(line)
            continue
        spans = sentence_spans(line)
        if not any(tokens(line[a:b]) > CAP for a, b in spans):
            out.append(line)
            continue
        pieces, changed, prev = [], False, 0
        for a, b in spans:
            pieces.append(line[prev:a])            # the separator, verbatim
            text = line[a:b]
            if tokens(text) > CAP:
                got = split_all(text, log)
                if got:
                    pieces.append(got[0])
                    touched += got[1]
                    changed = True
                else:
                    pieces.append(text)
            else:
                pieces.append(text)
            prev = b
        pieces.append(line[prev:])
        out.append(''.join(pieces) if changed else line)
    if not touched:
        return None
    return '\n'.join(out), touched


def repair_file(path, apply=False, verbose=False):
    """Returns a dict describing what was (or would be) done."""
    raw = open(path, encoding='utf-8').read()
    # The body ends only where the house gate says it ends. The first version
    # cut at the first '---' anywhere — so a chapter with a scene-break rule
    # was only repaired down to that rule, and the tool silently did half its
    # job. Same footer definition as live_book_gate.body_of().
    m = lbg.FOOTER_SPLIT.search(raw)
    body, sep, rest = (raw[:m.start()], raw[m.start():], '') if m else (raw, '', '')
    log = []
    got = repair_text(body, log)
    result = dict(path=path, splits=0, unsplittable=len(log),
                  unsplittable_examples=[t[:110] for _, t in log[:3]])
    if not got:
        return result
    new_body, touched = got
    # ---- PROOF BEFORE WRITE -------------------------------------------------
    if words_of(body) != words_of(new_body):
        raise SystemExit(f'REFUSED {path}: the word sequence changed — bug in the splitter')
    for q in ('"', '\u201c', '\u201d'):
        if body.count(q) != new_body.count(q):
            raise SystemExit(f'REFUSED {path}: quote count changed — bug in the splitter')
    # PER-LINE, WORD-FOR-WORD. The first version of this guard demanded every
    # new sentence be a raw substring of an old one — but a split puts a full
    # stop where a comma stood, so even a perfect split failed it and the tool
    # refused to write anything at all. Word sequence is the honest invariant:
    # if the tool dropped, added or reordered a single word, this catches it;
    # if it only moved punctuation, this passes.
    old_lines, new_lines = body.split('\n'), new_body.split('\n')
    if len(old_lines) != len(new_lines):
        raise SystemExit(f'REFUSED {path}: line count changed')
    for i, (a, b) in enumerate(zip(old_lines, new_lines)):
        if words_of(a) != words_of(b):
            raise SystemExit(f'REFUSED {path}: line {i + 1} changed its words')
    # counted the way the house gate counts: prose lines only, or panel and
    # planning lines would report as "still over the cap" forever and make the
    # tool look as if it had failed.
    prose_lines = [l for l in new_body.split('\n')
                   if l.strip() and not re.match(r'#+\s', l.strip())
                   and not l.strip().startswith(('>', '|', '- ', '* '))
                   and not lbg.PLAN_LINE_RX.search(l)]
    still = [(len(words_of(l[a:b])), l[a:b][:90])
             for l in prose_lines for a, b in sentence_spans(l)
             if tokens(l[a:b]) > CAP]
    result.update(splits=touched, remaining=len(still), remaining_examples=[t for _, t in still[:3]])
    if apply and touched:
        open(path, 'w', encoding='utf-8').write(new_body + sep + rest)
    return result


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
    """Fixtures are generated at exact lengths — a test whose input is shorter
    than the cap proves nothing. (The first version of this selftest passed a
    53-word '70-word' sentence and failed its own tool.)"""
    ok = True

    def case(name, text, want_splits, want_longest):
        nonlocal ok
        log = []
        got = repair_text(text, log)
        new = got[0] if got else text
        splits = got[1] if got else 0
        longest = max((tokens(x) for x in lbg.sentences(new)), default=0)
        good = (splits == want_splits and (want_longest is None or longest == want_longest)
                and words_of(new) == words_of(text)
                and new.count('"') == text.count('"')
                and new.count('\u201c') == text.count('\u201c'))
        ok &= good
        print(f"  [{'ok ' if good else 'FAIL'}] {name:54s} splits={splits} longest={longest}")

    def filler(n, start=0):
        return ' '.join(f'w{i+start}' for i in range(n))

    # 70 words with a strong boundary after 30
    s70 = f'{filler(30)}, and then {filler(38, 30)}.'
    case('a 70-word sentence splits at its strong boundary', s70, 1, 40)

    # 130 words, two strong boundaries
    s130 = f'{filler(40)}, and then {filler(40, 40)}, and then {filler(46, 80)}.'
    case('a 130-word sentence splits twice', s130, 2, 48)

    case('a short sentence is untouched', 'He walked east. The road was long.', 0, 4)

    # a boundary that sits INSIDE a quoted span must be skipped
    quoted = ('She said, "I will walk with you to the gate and then I will come back to the house '
              f'and wait the way I have waited {filler(20)}", and then she did exactly that before '
              'the week was over and nobody who saw it was surprised at all.')
    case('a split never lands inside speech — and the quoted span survives',
         quoted, 1, None)

    # REGRESSION: a closing quote that follows a full stop must survive a split
    # elsewhere in the same line. The first span-based rebuild deleted it.
    quote_line = ('He came down red-faced and the attendant said, in the voice he used for most of '
                  'them, "No soul power. Cannot cultivate." The boy came down red-faced, and his '
                  f'father put a hand on his head, and that was the shape of most of them, {filler(45)}.')
    case('a closing quote after a full stop survives a split elsewhere',
         quote_line, 1, None)
    assert 'Cannot cultivate."' in repair_text(quote_line, [])[0], 'closing quote lost'

    # and the case the tool refuses on purpose: the only boundary outside the
    # quotes would leave a 61-word half, so no edit is made at all
    toobig = ('She said, "I will walk with you to the gate and then I will come back to the house '
              f'and put the kettle on and wait the way I have waited {filler(30)}", and then she did '
              'exactly that before the week was over and nobody who saw it was surprised at all.')
    case('a split that would leave a half still over the cap is refused entirely',
         toobig, 0, None)

    # 65 words, no comma, no dash, no conjunction — nothing to split on
    noway = filler(65) + '.'
    case('no usable boundary: reported, not butchered', noway, 0, 65)

    # comma-only fallback
    s65 = f'{filler(30)}, {filler(34, 30)}.'
    case('a plain comma is used when nothing stronger exists', s65, 1, 34)

    sbare = f'{filler(28)} and {filler(35, 28)}.'
    case('comma-less prose falls back to the bare conjunction', sbare, 1, 36)

    print()
    print('SENTENCE REPAIR SELFTEST ' + ('PASSED' if ok else 'FAILED'))
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    if '--selftest' in args:
        return selftest()
    mode = 'report'
    if '--apply' in args:
        mode = 'apply'
    targets = [a for a in args if not a.startswith('-')]
    if not targets:
        print(__doc__)
        return 0
    files = 0, 0, 0, 0
    applied = splits = remaining = unsplit = 0
    for f in walk(targets):
        if not f.endswith('.md'):
            continue
        r = repair_file(f, apply=(mode == 'apply'))
        files = files[0] + 1, 0, 0, 0
        if r['splits'] or r.get('remaining') or r['unsplittable']:
            applied += 1 if r['splits'] else 0
            splits += r['splits']
            remaining += r.get('remaining', 0)
            unsplit += r['unsplittable']
            tag = 'APPLIED' if (mode == 'apply' and r['splits']) else 'would fix'
            print(f"  {tag} {r['splits']:3d}  left {r.get('remaining', 0):2d}  "
                  f"no boundary {r['unsplittable']:2d}  {os.path.relpath(f)}")
    print(f"\n{mode.upper()}: {splits} split(s) across {applied} file(s) · "
          f"{remaining} still over the cap · {unsplit} with no usable boundary")
    return 0


if __name__ == '__main__':
    sys.exit(main())
