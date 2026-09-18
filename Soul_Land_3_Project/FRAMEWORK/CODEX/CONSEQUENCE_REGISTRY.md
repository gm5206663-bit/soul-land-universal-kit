# CONSEQUENCE REGISTRY

Every premise that has entered the story, and what must follow from it.

**A premise stays OPEN until every one of its consequences has either landed on-page or been
explicitly decided against.** Silence is not a decision.

`python3 CODEX/consequence.py check` greps the chapters for each open consequence and reports what
has not landed.

---


## P001 — Both of Lin Hao's rings re-formed PURPLE and a third ring was bestowed (hawk 1,164 at the crossing)

- **chapter:** 40
- **status:** CLOSED
- **follows:** Gale Talon and Hawk-Soul Union both upgrade to thousand-year tier
- **follows:** OWED (F1): the thousand-year tier is SHOWN on-page in a scene, not merely recorded in the docs
- **follows:** [docs] The soul-skill count is recorded: a thousand-year soul provides THREE skills
- **follows:** [docs] The rank ceiling is recorded as 40, not 30
- **scan:** thousand[- ]year (soul )?skill
- **scan:** (Gale Talon|Hawk-Soul Union)[^\n]{0,120}(thousand[- ]year|evolv|upgrad)
- **scan:** THREE soul skills
- **scan:** ceiling[^\n]{0,40}\b40\b

## P002 — The rank-30 hard wall opened

- **chapter:** 40
- **status:** OPEN
- **follows:** [docs] The tracking docs describe the ceiling as 40, and the wall as opened at ch40
- **scan:** ceiling[^\n]{0,40}\b40\b

## P003 — Wang Jinxi has left; Zhang Yangzi stays; class zero is five and Shrek invites five

- **chapter:** 60
- **status:** OPEN
- **follows:** Every count of the group says five, not six
- **follows:** Zhang Yangzi is at Eastsea but out of class zero
- **scan:** all five of (us|you)|All five of you|the five of them
- **scan:** Zhang Yangzi[^\n]{0,90}(stays|still at Eastsea|out of class zero)

## P004 — Gu Yue teaches Lin Hao elemental fusion. Wind + lightning become ONE idea about distance, not two taking turns.

- **chapter:** 57
- **status:** OPEN
- **follows:** The fused stroke must be usable on-page from ch58 onward, and it must cost more than either voice alone
- **follows:** It is a TECHNIQUE, not a soul skill - the sword does it, the rings do not. It must not be confused with Hawk-Soul Union
- **follows:** [docs] His techniques panel lists it, and Gu Yue is credited as the one who taught it
- **follows:** [docs] RECORDED: Gu Yue has now given him something, which reverses three years of her giving him nothing to read. In RELATIONSHIPS.md §10 and the techniques panel.
- **scan:** (gone from the waist up|take the something out|two things with .*different ideas about distance|seam in \*\*yourself)
- **scan:** (not a soul skill|the sword does it|TECHNIQUE)
- **scan:** (fusion|Two Voices|the seam in yourself)
- **scan:** Gu Yue[\s\S]{0,400}(taught|teach)

## P005 — LOCKED FUTURE ARC: the second spirit soul (ice+water dragon, ten-thousand-year) and the month-long absorption. Rank 40 -> 45.

- **chapter:** 61
- **status:** 🔴 **LANDED — ch69 (the jiao found, the month begins) and ch71 (the emergence).** Every
  locked element is on-page and measured in THE_CODEX.md's ch71 record. Still open downstream:
  **Hawk-Soul Union must be re-thought** (the hawk now shares him with something older), **DOMINEER
  (「镇」) has not been used on-page**, and **nobody has named the Frost Abyss Domain**.
- **status-note:** left OPEN deliberately — the arc's *consequences* are still unspent. Do not close it.
- **follows:** [docs] Nothing may write him past rank 40 before the arc, and the rank ceiling stays 40 until it
- **follows:** [docs] The APPEARANCE LAW must treat this as its biggest single event - he changes physically and it must be witnessed
- **follows:** [docs] The small personality change must be shown through OTHER people noticing, never stated
- **follows:** [docs] Hawk-Soul Union must be revisited: the hawk now shares him with something older
- **follows:** [docs] THE TIMELINE RULE: the absorption month does NOT get invented story time. Canon events happen WITHOUT him; butterfly effects flow naturally; the ensemble carries the month.
- **follows:** [docs] He is ELEVEN at the fourth-ring arc, not ten. The 11th birthday falls in the run-up and is OWED.
- **scan:** rank 4[1-5]
- **scan:** appearance
- **scan:** personality
- **scan:** Hawk-Soul Union
- **scan:** age

## P006 — THE FORM (ch59) - Lin Hao writes 'Comprehensive' in the blank line under the six squares. He founds a category in eleven seconds and does not know it.

- **chapter:** 59
- **status:** OPEN
- **follows:** He is the FOUNDER of the Comprehensive System. In SL4 it is the highest formal tier; in his lifetime it is one line on one form in a harbour city.
- **follows:** Nobody knows, including him. He cannot be congratulated on founding something when the founding was a word on a form nobody read.
- **follows:** [docs] THE MECHANISM: a System is whatever is on the form. Gu Yue wrote 'Elementalist' in the same blank line and it has been true ever since, unquestioned.
- **follows:** His journal records the loneliness: he has a word he invented four hours ago that nobody knows the meaning of - including him. This must not be un-said.
- **scan:** Comprehensive
- **scan:** founded|founder|invented a category
- **scan:** Elementalist
- **scan:** made up four hours ago|including me

## P007 — SKY ICE (ch62) - Wu Zhangkong reveals a two-word battle armor in front of the whole Alliance, and Xie Xie decides out loud that Lin Hao will make the metal

- **chapter:** 62
- **status:** OPEN
- **follows:** The BATTLE ARMOR SYSTEM is now known to Lin Hao: four levels, a word each, 5/6/7/9 rings minimum, twenty ranks above the wearer's paper.
- **follows:** Xie Xie's declaration is a PROMISE and must not be dropped: 'you're going to make the metal, and I'm going to be a mecha master.' It opens the battle-armor-smithing thread.
- **follows:** [docs] Mu Chen's canon line must be connected to Lin Hao: 'the foundation of a battle armor master stems from being a first-rank blacksmith.' The metal ladder IS the blacksmith ladder.
- **follows:** [docs] Lin Hao may NOT wear battle armor: one-word needs five rings and he has three. He may only ever be shown MAKING it.
- **follows:** He now knows he is not the only person alive who is a lie on paper. Wu Zhangkong is twenty ranks above his; Lin Hao is fifteen. The loneliness of being the only one is over and he has not said so.
- **scan:** battle armor
- **scan:** twenty ranks
- **scan:** make the metal
- **scan:** spirit refined|soul refined|divine refined
- **scan:** same shape|not the only|lie on paper

## P008 — SHEN YI IS WU ZHANGKONG'S TEACHER (ch62) - she says 'Congratulations, Zhangkong' on the page, and 'Now this is the real him'

- **chapter:** 62
- **status:** OPEN
- **follows:** She has known him long enough to have seen Sky Ice before, and it had been ages. Their history is a live thread and is still unexplored.
- **follows:** Wu Zhangkong's origin is STILL not named. Shrek stays locked to the canon ch204 reveal. Her presence makes the lock load-bearing, not decorative.
- **follows:** [docs] It is why her ch61 verdict on Lin Hao lands on Wu Zhangkong as HIS TEACHER's verdict, and why he answers her rather than deflecting.
- **follows:** She said congratulations to a man wearing an expression devoid of joy, and neither of them said anything about the other thing. That silence is owed an explanation eventually.
- **scan:** Shen Yi
- **scan:** Congratulations, Zhangkong
- **scan:** my teacher

## P009 — HE TOLD GU YUE THE WHOLE OF IT (ch62) - no goal, no destination, three better options never mentioned, and 'But I wanted to tell you. Or I -'

- **chapter:** 62
- **status:** OPEN
- **follows:** The blank page INVERTS. Ledger line 109 is her, and it is not a technique. Line 108 is Wu Zhangkong. The ledger is no longer only about how to win.
- **follows:** Line 109 is DELIBERATELY UNFINISHED: 'Or I -'. Nothing may complete that sentence in the ledger. Only he can say it, out loud, to her.
- **follows:** SHE KNOWS THE END OF IT and does not say it. Nobody has named the thing between them. Whether and when that changes is the USER's decision, not mine.
- **follows:** He has three better options he has never told Wulin about, because Wulin already feels he owes him. That is now a stated fact and cannot be un-said.
- **follows:** [docs] For forty chapters she gave and he received. In ch62 he gave and she received. The distance did not close - it CHANGED HANDS.
- **scan:** or I
- **scan:** wanted to tell you
- **scan:** better options
- **scan:** journey
