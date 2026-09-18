import io, re, glob

def patch(path, pairs):
    t = io.open(path, encoding='utf-8').read()
    for old, new in pairs:
        assert t.count(old) == 1, (path, 'MISS x%d' % t.count(old), old[:70])
        t = t.replace(old, new)
    io.open(path, 'w', encoding='utf-8').write(t)
    print('fixed:', path, f'({len(pairs)})')

patch('chapters/chapter_79.md', [
 ('And then Gu Yue said, "How about I protect Xu Xiaoyan and you carry me on your back. It shouldn\'t be a problem with your physical strength. Xie Xie can then follow right behind us. That should work."',
  'And then Gu Yue said, "How about I protect Xu Xiaoyan — and Lin Hao carries me on his back. It shouldn\'t be a problem with his physical strength. Xie Xie can then follow right behind us. That should work."'),
 ('Wulin considered it — his own plan had been the more logical one, hers worked too, and something about it struck him as strange, so he eyed her suspiciously. A slight blush appeared on Gu Yue\'s face and was put away again just as fast.',
  'Wulin considered it — his own plan had been the more logical one, and hers spent the seams on carrying, which nobody could account for; he eyed her suspiciously anyway, brother to the boy being volunteered. A slight blush appeared on Gu Yue\'s face and was put away again just as fast.'),
 ('No time to change anything. She mounted his back;',
  'No time to change anything. She mounted Lin Hao\'s back;'),
 ('Gu Yue chanted, hands raised, clinging to Wulin\'s back with her legs.',
  'Gu Yue chanted, hands raised, clinging to Lin Hao\'s back with her legs.'),
 ('Wulin went last, Gu Yue on his back — and directly under the guillotine, the stone pillar collapsed.\n\nThe gigantic blade plunged down at them.',
  'Lin Hao ran the seams with Gu Yue on his back; Wulin held the line beside him — and directly under the guillotine, the stone pillar collapsed.\n\nThe gigantic blade plunged down at the two of them.'),
 ('Gu Yue shut her eyes and wrapped her arms around his neck as if she had no intention of leaving it — her heart racing, probably because of the tense situation; Wulin mostly felt her drawing closer, arms and legs around his neck and waist, and felt, himself, neither fear nor joy.',
  'Gu Yue shut her eyes and wrapped her arms around Lin Hao\'s neck as if she had no intention of leaving it — her heart racing, probably because of the tense situation. Lin Hao noted it the way he noted everything, at speed and without comment: the rows breathed in threes, and so did he.\n\nAnd Wulin was already moving — a step, a lunge, his shoulder under the falling iron his brother and his friend stood beneath.'),
 ('Tang Wulin caught it easily, squatting a little under the load. "Up!" — and his arm filled with strength and threw the blade high, and he stepped through his own gate with Gu Yue on his back.',
  'Tang Wulin caught it easily, squatting a little under the load. "Up!" — and his arm filled with strength and threw the blade high, and Lin Hao stepped through the gate with Gu Yue on his back, and the captain cleared his own beside them.'),
 ('**Gu Yue\'s arrangement — the back-ride — the suspicious eye — the slight blush** (canon\'s own beat, rendered uninterpreted)',
  '**Gu Yue\'s arrangement — the back-ride, RE-RECEIVERED to Lin Hao (the Receiver Law) — the suspicious eye (Wulin\'s, brother to the boy being volunteered) — the slight blush (hers, one direction, put away fast)**'),
 ('the pillar collapse under the gate — GU YUE\'S ARMS AROUND HIS NECK — the claw — THE CATCH',
  'the pillar collapse under the gate — GU YUE\'S ARMS AROUND LIN HAO\'S NECK — WULIN\'S DIVE, HIS BROTHER\'S IRON — the claw — THE CATCH'),
 ('Gu Yue\'s back-ride arrangement; Wulin\'s suspicion; the slight blush; the mounting; the green lights; Xiaoyan pale** — canon ch 258, verbatim.',
  'Gu Yue\'s back-ride arrangement; Wulin\'s suspicion; the slight blush; the mounting; the green lights; Xiaoyan pale** — canon ch 258, verbatim **except the RECEIVER: in canon she rides Wulin; the Receiver Law (session oo) gives the back-ride to Lin Hao — Wulin is out of the geometry, and free to make the catch over his brother and her.**'),
 ('Gu Yue\'s shut eyes and racing heart; Wulin feeling her closer, neither fear nor joy;',
  'Gu Yue\'s shut eyes and racing heart (on Lin Hao\'s back); *["Wulin feeling her closer, neither fear nor joy" — CUT: not his to feel, in this AU];*'),
 ('- **The blush kept canon\'s own:** Gu Yue\'s arrangement and the suspicious eye rendered exactly as written, uninterpreted — the wire DORMANT by law; the class does not comment; neither does the prose.',
  '- **THE RECEIVER LAW (session oo, user ruling): in this AU there is no Wulin×Gu Yue — none.** Canon\'s pairing beats are re-receivered, never copied. The back-ride: Lin Hao\'s (*"his physical strength"*); the suspicious eye: the brother\'s, for the boy being volunteered; the blush: hers, pointing one direction; the catch: Wulin\'s — over his brother and her, which is who Wulin is. **The old "wire dormant / uninterpreted" law is REPEALED — it was the door canon got copied through.**'),
 ('· trials 8·10 (canon\'s recall; the capped run) · **the arrangement and the blush — canon\'s own, uninterpreted** · as before',
  '· trials 8·10 (canon\'s recall; the capped run) · **the back-ride re-receivered to Lin Hao; the blush hers, one direction (the Receiver Law)** · as before'),
])

patch('RELATIONSHIPS.md', [
 ("ch71's confession received in silence — the wire dormant by law",
  "ch71's confession received in silence — silence ≠ refusal: her answer was acts; one-directional by the Receiver Law"),
 ("- **ch71: THE CONFESSION — her answer was silence, accepted as no-things, as before; the wire is DORMANT by law; the ordinariness is the wound's exact shape, and it is his.**",
  "- **ch71: THE CONFESSION — her answer was silence, accepted as no-things, as before; THE RECEIVER LAW (session oo): one direction, no triangle, ever; the ordinariness is the wound's exact shape, and it is his.**"),
 ("| **73–79** | The exam: nothing forced, nothing read, nothing spent of it. **ch75's juice box is canon's own beat between her and WULIN** (canon 253, verbatim) — rendered uninterpreted, as law demands. ch79's arrangement and blush: likewise canon's own. The wire stays dormant; the ordinariness is the wound's exact shape, and it is his. |",
  "| **73–79** | The exam: nothing forced, nothing read, nothing spent of it. **Session oo — THE RECEIVER LAW: canon's Wulin-pairing beats (the ch75 juice box, the ch79 back-ride) were RE-RECEIVERED to Lin Hao** — retroactively, on the user's ruling. Wulin is out of the geometry: the brother who has known for years, and guards it. Her thread runs one direction; the ordinariness is the wound's exact shape, and it is his. |"),
 ("- 🔴 **THE WIRE (canon's eventual Wulin×Gu Yue, series-level fact):** dormant at thirteen, spent nowhere on-page. In canon the boy he confessed to is the other end of that future. **Do not spend casually; the walked years own it.**",
  "- 🔴 **REPEALED (session oo, user ruling) → THE RECEIVER LAW:** canon's eventual Wulin×Gu Yue DOES NOT EXIST in this AU — not dormant, not touched-on, nothing. Every romantic coding runs toward **Lin Hao**. Wulin is never romantically coded with Gu Yue: he is the brother who has known for years and guards the thread. Canon pairing beats are **re-receivered or neutralized, never copied.** The ch75/ch79 violations were found and fixed the same session."),
 ("- **The wires, intact:** the Lin Hao thread open and unhurried; canon's eventual Wulin×Gu Yue dormant and untouched — her silence spent nothing.",
  "- **The wires, intact:** the Lin Hao thread open and unhurried — and the ONLY thread, by the Receiver Law (session oo); her silence spent nothing, and her acts spent plenty."),
 ("- **Gu Yue — the renunciation, canon verbatim:** the substitute offer; the rebuke (*\"you shouldn't be so naive\"*); *\"If Wulin can't go, I won't go either. If he can't join Shrek, I also refuse to join.\"* Observed, not interpreted — her resolve aimed outward is the same resolve he watched aim nowhere two nights ago; the wire stays dormant and the prose does not push it.",
  "- **Gu Yue — the renunciation, canon verbatim:** the substitute offer; the rebuke (*\"you shouldn't be so naive\"*); *\"If Wulin can't go, I won't go either. If he can't join Shrek, I also refuse to join.\"* Observed, not interpreted — her resolve aimed outward is the same resolve he watched aim nowhere two nights ago; loyalty, not pairing (the Receiver Law holds; the prose does not push)."),
 ("- **The car (canon's own, uninterpreted):** the seat arrangement by Gu Yue's invisible hand; the bag that needed no thanks; the juice box; *\"happiness flashed in Gu Yue's eyes before she closed them to rest\"*; cool arm against warm. The front seat had the manners not to report. The wire stays dormant.",
  "- **The car (RE-RECEIVERED, session oo):** the seat arrangement by Gu Yue's very visible hand — seating HERSELF beside Lin Hao; the bag that needed no thanks; the juice box — Lin Hao's now; *\"happiness flashed in Gu Yue's eyes before she closed them to rest\"*; cool shoulder against warm arm. The back seat had the manners not to report."),
 ("- **The blush, canon's own, untouched:** Gu Yue's arrangement (the back-ride), Wulin's suspicious eye, the slight blush put away — rendered exactly as canon wrote it, and the class did not comment, and neither did the prose. The wire stays dormant; canon's beats still breathe.",
  "- **The back-ride, re-receivered (session oo):** canon gave Gu Yue's arrangement and the blush to Wulin; the Receiver Law gives the ride to Lin Hao (*\"his physical strength\"*), keeps the suspicious eye as Wulin's — brother to the boy being volunteered — keeps the blush as hers, pointing one direction, and gives Wulin the catch: over his brother and her. Which is who he is."),
])

patch('THE_CODEX.md', [
 ("· **at Shrek — trials 8·10 (canon's recall; the capped run); the arrangement + the blush ch79 were canon's own, uninterpreted** ·",
  "· **at Shrek — trials 8·10 (canon's recall; the capped run); ch79's back-ride RE-RECEIVERED to Lin Hao (the Receiver Law)** ·"),
 ("🔴 **ch62: he told her the whole of it and she said nothing · ch71: THE CONFESSION — her silence kept, the wire dormant by law** ·",
  "🔴 **ch62: he told her the whole of it and she said nothing · ch71: THE CONFESSION — her silence kept; her answer was acts (the metal); ONE direction, by the Receiver Law (session oo)** ·"),
])

patch('CHARACTER_STATS.md', [
 ("· **ch71: the confession received — and answered with SILENCE: nothing said, nothing done, accepted as no-things, like before (the canon wire stays dormant)** ·",
  "· **ch71: the confession received — answered with a silence that is NOT refusal: her answer was acts, not words (the metal; the looks); ONE direction by the Receiver Law (session oo: no Wulin×Gu Yue exists in this AU — none)** ·"),
 ("· **the arrangement and the blush — canon's own, uninterpreted** · as before",
  "· **the back-ride re-receivered to Lin Hao; the blush hers, one direction (the Receiver Law)** · as before"),
])

patch('CONTINUATION_PROMPT.md', [
 ("Gu Yue's back-ride arrangement + the blush (canon's own, uninterpreted);",
  "Gu Yue's back-ride arrangement — RE-RECEIVERED to Lin Hao — + the blush (hers, one direction);"),
 ("the wire DORMANT (the blush was canon's own, uninterpreted);",
  "THE RECEIVER LAW (no Wulin×Gu Yue in this AU, none — canon's pairing beats are re-receivered, never copied; the old dormant-wire law is REPEALED);"),
 ("- **canon's eventual Wulin×Gu Yue (series-level fact) is the untouched wire** — dormant at 10, spent nowhere; recorded in ch66's footer as the project's largest open butterfly. Do not spend it casually",
  "- **THE RECEIVER LAW (session oo, user ruling): canon's Wulin×Gu Yue DOES NOT EXIST in this AU.** Every romantic coding runs toward Lin Hao; Wulin is never romantically coded with her — he is the brother who has known for years and guards it. Canon pairing beats: re-receiver or neutralize, never copy. (Supersedes the old \"untouched wire\" note; ch66's footer line is historical.)"),
])

patch('BUTTERFLY_REGISTRY.md', [
 ("| **The confession + silence** | ch71/72 | wire DORMANT by law | ch75 (the juice box — canon's own, uninterpreted) | do NOT force; the next beat is HERS, whenever canon moves it |",
  "| **The confession + silence → THE RECEIVER LAW** | ch71/72 | silence ≠ refusal (her answer: acts — the metal, the looks); ALL romantic coding runs toward Lin Hao; **no Wulin×Gu Yue exists in this AU** | ch79 (the re-receivered back-ride) | her thread resolves on-page — direction fixed, TIMING the user's call (asked session oo) |"),
])

io.open('THE_CODEX.md', 'a', encoding='utf-8').write("""

---

## 🔴 THE RECEIVER LAW (user ruling, session oo, 2026-09-01: *"in relationship there it already said Gu Yue and Wulin have nothing — but you showed it, forcing, no logic; Lin Hao told Wulin he likes Gu Yue years before; Wulin would NEVER"*)

1. **In this AU there is no Wulin×Gu Yue — none.** Not dormant, not foreshadowed, not "canon's own
   beat rendered uninterpreted." The old dormant-wire law is **REPEALED** — it was the door canon's
   pairing beats got copied through (ch75 juice box, ch79 back-ride: both found, both re-receivered).
2. **Every romantic coding runs toward Lin Hao.** Canon beats whose receiver is Wulin are
   **re-receivered to Lin Hao or neutralized — never copied.** The receiver is the butterfly.
3. **Wulin is the brother.** He has known for YEARS — and he guards the thread. He is never a rival,
   never a fallback, never romance-coded with her. The ch79 catch is now literally him holding the
   blade over his brother and her. That is who he is.
4. **Gu Yue's silence was not rejection.** Her answer was acts — the metal, the looks; *"naming was a
   spend, and she had never once spent early… you do not open a purse in the street."* One direction,
   no triangle. Resolution timing: the user's call.
""")
print('CODEX law appended')
io.open('CODEX/05_PROJECT_SOUL_LAND_3.md', 'w', encoding='utf-8').write(io.open('THE_CODEX.md', encoding='utf-8').read())
print('mirror synced')

bad = []
for f in sorted(glob.glob('chapters/*.md')) + ['RELATIONSHIPS.md','THE_CODEX.md','CHARACTER_STATS.md','CONTINUATION_PROMPT.md','BUTTERFLY_REGISTRY.md','LIN_HAO_STATUS.md','POWER_MODEL.md']:
    for i, l in enumerate(io.open(f, encoding='utf-8').read().split('\n')):
        if re.search(r'uninterpreted|wire stays dormant|Hogging Wulin|hogging Wulin|wire is DORMANT|wire DORMANT by law', l):
            bad.append((f, i+1, l.strip()[:76]))
print('leftovers:', bad if bad else 'NONE')
