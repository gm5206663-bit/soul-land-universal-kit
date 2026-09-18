#!/usr/bin/env python3
import subprocess
p='CODEX/06_PROJECT_SOUL_LAND_2.md'
s=open(p,encoding='utf-8').read()
s=s.replace("**VERSION 7.6 — THE THREE-SOURCE MAP (novel + donghua + manhua) (2026-08-26)**",
"**VERSION 7.7 — CH 15 REBUILT: THE ANGRY AUDIENCE (2026-08-26)**",1)
a=s.find("**Chapter 15: (REBUILD NEXT")
b=s.find("### FOUNDATION CHANGELOG")
rec = (
"**Chapter 15: The Ledger of Two Fires (REBUILT - canon ch 15-1/2 held; the user's directed anger scene)**\n"
"- **Canon receipts:** the pill-scheduling debate (Wang Dong's lecture: 'you don't serve the next course into a full bowl'); his green pill THAT NIGHT (21->22/23); "
"the three-month montage (the stall 20->30, one each, no price-rise; the fame; Nannan's single queue; Xu Sanshi the faithful regular); **67 of 91 survive - the academy's predicted third shattered; "
"Yuhao's unchallenged monitorship and why**\n"
"- **THE ANGRY AUDIENCE (user-directed):** the OC alone at the administrator hall; the two questions ('where in the contract is the remedy a pill and a threat?' / "
"'if the rank-11 orphan had died, who answers - to anyone?'); the honest answer ('the inner court governs itself'); 'the pills were a receipt'; "
"'I'm the one who fixes things - it's on me to know which things this academy fixes and which it just seals'; THE MEMO ripple\n"
"- **THE FOX'S DOCTRINE (beast-knowledge):** institutions = 'a beast with ten thousand stomachs and no single throat to blame'; "
"'You cannot fix an institution. But you can make it irrelevant to the people you love. THAT IS THE CRAFTSMAN'S REVENGE.' / 'Get stronger than the jar.'\n"
"- **Ranks at month's end:** Yuhao past the teens; Wang Dong 23; Jiang Che 25+ (AT compounding)\n\n"
"**Chapter 16: (NEXT - canon ch 15-3/4 + ch 16-17: the NEW-STUDENT ASSESSMENT [manhua ch 16]; Xiao Xiao's debut [the twin-soul girl]; research-first: fetch book/15445-15453 + manhua check)**\n\n"
)
if a>0 and b>a:
    s=s[:a]+rec+s[b:]
s=s.replace("### FOUNDATION CHANGELOG\n",
"### FOUNDATION CHANGELOG\n- **v7.7 (2026-08-26): CH 15 REBUILT - 'The Ledger of Two Fires.'** The user's directed anger built as craft (two questions, no shouting, no leaks) + direction (the craftsman's revenge: outgrow the jar). Canon 15-1/2 held whole (the pills; the montage; 67 of 91). All files updated; integrity clean.\n",1)
open(p,'w',encoding='utf-8').write(s)
print("codex -> v7.7")
subprocess.run(['cp','CODEX/06_PROJECT_SOUL_LAND_2.md','Soul_Land_2_Project/THE_CODEX.md'])
p2='CODEX/00_INDEX.md'
s2=open(p2,encoding='utf-8').read()
s2=s2.replace('v7.5 CH 14 REBUILT (full stack; Ma Xiaotao + the extreme-ice file)','v7.7 CHAPTERS 1-15 (full stack; the Angry Audience; the craftsman\\'s revenge)',1)
open(p2,'w',encoding='utf-8').write(s2)
print("index -> v7.7")
