#!/usr/bin/env python3
import subprocess
p='CODEX/06_PROJECT_SOUL_LAND_2.md'
s=open(p,encoding='utf-8').read()
s=s.replace("**VERSION 6.4 — CHAPTER 13 WRITTEN: THE FIFTH (2026-08-26)**",
"**VERSION 6.5 — CHAPTER 14 WRITTEN: THE LAKE (2026-08-26)**",1)
a=s.find("**Chapter 14: (NEXT")
b=s.find("### FOUNDATION CHANGELOG")
rec = (
"**Chapter 14: The Lake (WRITTEN - canon ch 14-1/2 held whole; the OC's witness-structure butterfly)**\n"
"- **Canon receipts:** the red-masked attacker (running on water; the fire-sea; Wang Dong's wings curling); the ice-auto-shield; "
"**Skydream's possession** (white eyes; the ring turning GOLD; the hundred-meter freeze; 'you dare touch the one brother chose... then die'; "
"the finger vs the Evil Fire Phoenix [a six-ring Soul Emperor]; 'I dodge'); the inner court's rescue (the white-robed elder; Li the Life Tree Soul Saint; "
"the grass un-burning); the cover-up order + compensation; **Skydream's debrief: the phoenix bloodline; the evil fire; THE FIRST SEAL partially open**\n"
"- **BUTTERFLY (structural):** the OC + fox on the near-shore work-site: the fox's warning saves the crew; the fox reads BOTH beings "
"('older than every book' / 'a wound, not a weapon') and seals it; the academy's cover-up absorbs the OC ('saw only steam'); "
"room 108's seam: 'whatever stood behind your eyes, it spent YOU to do it... the account has a keeper now'; 'I knew he was my brother.'\n"
"- **Ranks at end:** Yuhao 12 peak; the first seal hairline-open (canon); no changes\n\n"
"**Chapter 15: (NEXT - the month's rhythm; the first assessment approaching; canon ch 14-3/4 + ch 15 三個月 [book/15437-15447]: the three-month montage; research-first)**\n\n"
)
if a>0 and b>a:
    s=s[:a]+rec+s[b:]
s=s.replace("### FOUNDATION CHANGELOG\n",
"### FOUNDATION CHANGELOG\n- **v6.5 (2026-08-26): CHAPTER 14 WRITTEN - 'The Lake.'** Skydream's possession held canon-exact; the OC's witness-structure butterfly (the fox reads both beings and seals it); the cover-up absorbs the OC; the account-has-a-keeper seam. All files updated; integrity clean.\n",1)
open(p,'w',encoding='utf-8').write(s)
print("codex -> v6.5")
subprocess.run(['cp','CODEX/06_PROJECT_SOUL_LAND_2.md','Soul_Land_2_Project/THE_CODEX.md'])
p2='CODEX/00_INDEX.md'
s2=open(p2,encoding='utf-8').read()
s2=s2.replace('v6.4 CHAPTERS 1-13 (The Fifth: the stairwell word; the sect = five)','v6.5 CHAPTERS 1-14 (The Lake: Skydream\\'s finger witnessed; the account has a keeper)',1)
open(p2,'w',encoding='utf-8').write(s2)
print("index -> v6.5")
