import io, sys, re
p = "chapters/Chapter_02_The_House_and_the_Road.md"
s = io.open(p, encoding="utf-8").read()

subs = [
 ('His father answered him seriously, the way\u2014 no. "His father answered him seriously. That was how his father answered everything."',
  'His father answered him seriously. That was how his father answered everything.'),
 ('Zhou Hui had walked to the school office at first light, the way\u2014 no. "Zhou Hui had walked to the school office at first light, before the shutters came up, and she had settled the term standing up. It was what she had told the table she would do, and that woman did what she told the table."',
  'Zhou Hui had walked to the school office at first light, before the shutters came up, and she had settled the term standing up. It was what she had told the table she would do, and that woman did what she told the table.'),
 ('She had kept the grain house books for six years, and she read the way\u2014 (no) "She had kept the grain house books for six years, and she could read a list faster than most people could read a name."',
  'She had kept the grain house books for six years, and she could read a list faster than most people could read a name.'),
 ('and she said it the way\u2014 no. "The sums had gone through the house that week like weather through a house, and she said it anyway, to the pot and the two of them, because a house that stops saying a thing stops being able to say it."',
  'The sums had gone through the house that week like weather through a house, and she said it anyway, to the pot and to the two of them, because a house that stops saying a thing stops being able to say it.'),
 ('His mother called it *the pig*, dryly, the way\u2014no: "His mother called it *the pig*, in the flat voice she used for the weather. His father called it nothing at all, and fed it the clean trimmings from the clinic, and watched it eat, and had his own thoughts about all of it."',
  'His mother called it *the pig*, in the flat voice she used for the weather. His father called it nothing at all, and fed it the clean trimmings from the clinic, and watched it eat, and had his own thoughts about all of it.'),
 ('The boy sat with it until his feet went numb, the way\u2014no: "The boy sat with it until his feet went numb, the way a boy watches the first coal he has ever carried across a room without dropping it." \u2014 banned. Rewrite: "The boy sat with it until his feet went numb and would not take his eyes off it, the way\u2014" no. "The boy sat with it until his feet went numb, guarding it as if a draft could put it out."',
  'The boy sat with it until his feet went numb, guarding it as if a draft could put it out.'),
 ('and turned and came back, the way a river turns when the land tilts the other way \u2014 no. New: "and turned, and came back, as rivers do when the land tilts." Hmm \u2014 "as rivers do when the land tilts" is fine (no "the way").',
  'and turned, and came back, as rivers do when the land tilts.'),
 ('and the groups closed without him the way\u2014no: "and the groups closed without him, the way water closes." \u2014 rewrite: "and the groups closed over the space where he stood, as water closes over a stone."',
  'and the groups closed over the space where he stood, as water closes over a stone.'),
]
miss=[]
for old,new in subs:
    n=s.count(old)
    if n!=1:
        miss.append((n,old[:80]))
        continue
    s=s.replace(old,new,1)
if miss:
    print("MISS:",miss); sys.exit(1)

# meta-artifact sweep
for bad in ["the way\u2014", "banned", "Rewrite:", "no: \"", "(no)"]:
    if bad in s:
        print("ARTIFACT STILL PRESENT:", bad)
io.open(p,"w",encoding="utf-8").write(s)
print("fixed. 'the way' count:", len(re.findall("the way", s)))
