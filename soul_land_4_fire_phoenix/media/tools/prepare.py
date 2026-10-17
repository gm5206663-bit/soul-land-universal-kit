#!/usr/bin/env python3
"""Build a source-pinned chapter storyboard, not new canon or accepted prose."""
from pathlib import Path
import hashlib,json,re,subprocess,argparse

BEATS = [
"A northern research expedition finds a mystery beneath the ice while Yan's protected family beginning unfolds elsewhere.",
"Family safeguards and institute housing bring Yan and Lan Xuanyu together through an ordinary, quietly extraordinary childhood.",
"Awakening reveals Yan's juvenile Fire Phoenix, before any soul ring or bonded soul spirit has been acquired.",
"School registration creates the first public records while friendship must survive different classes and hidden family truths.",
"School rivalry and physical tests teach restraint as Yan reaches the first bottleneck without acquiring a ring yet.",
"Yan bonds legally with the flawed Dawnflame Kite, gaining the first yellow ring and an unmastered first skill.",
"The return journey brings Nana into Lan's home while Yan's first living bond continues to settle.",
"School resumes around public tests and private danger, with Lan's abnormality drawing attention that adults must carefully manage.",
"Quiet months of training deepen foundations while distant performances and family absences change the children's emotional world.",
"The Horizon Building crisis makes danger immediate; rescue and its aftermath give Lan new reasons to train.",
"Nana's departure and the Elite Junior Class pathway turn loss into preparation for a much harder school life.",
"A simulated forest assessment exposes the cost of survival, and Lan's mental injury leaves his friends waiting.",
"Lan wakes, a concert changes his world, and the academy transition creates new dormitory teams and obligations.",
"Yan refuses to turn every conflict into a personal intervention while classmates learn what teamwork will demand.",
"Dorm333's first Soul World challenge exposes broken formation, unreliable summoning and the real cost of earning a coin.",
"The summoning gate answers with an ice-wielding girl, revealing possibilities that depend on coordination rather than certainty.",
"A cafeteria question and another gate test show how dangerous secrets can hide inside ordinary school conversation.",
"Repeated summoning tests reveal limits and connections, while Yan learns to keep fire and light under control.",
"Teacher Ji's lessons bring special colors and dangerous questions into focus without granting anyone knowledge they have not earned.",
"Lan seeks a private answer through Nana's message route as the next physical examination begins to close in.",
"Midterm results and protected plus signs lead into the Maze, where a team's judgment matters as much as strength.",
"The Maze rewards concealment, patience and careful positioning before the next confrontation reaches its decisive exchange.",
"Ten decisive seconds test the teams, as Yan's controlled fire follows a different path from Lan's hidden answer.",
"A private teacher's demanding simulation leaves Lan exhausted while Yan measures the recovery cost of the Maze.",
"Yan's second soul-spirit process adds a new structural foundation without turning a private truth into a public reveal.",
"The next test changes the pressure on the teams, and the summoning gate prepares an answer not yet understood.",
"A Crocodile Dragon answers one call; the next door brings the unexpected and dangerous Emerald Demon Bird.",
"A frighteningly quick match changes what opponents know, forcing every later team to prepare against a visible tactic.",
"Lan chooses concession rather than gambling blindly, showing that a deliberate defeat need not mean a broken team.",
"Pressure produces Lan's colorful self-fusion-like answer, but another team's earned place cannot simply disappear from the board.",
"Dorm336 finally receives the match the board owed, preserving a real rival route before time is allowed to move.",
"Training accumulates across the time bridge, and the Purple Flame path becomes a named possibility rather than an instant reward.",
"Careful preparation begins the protected cocoon process; the door closes around a transformation nobody is allowed to hurry.",
"The twenty-first pulse brings developing wing structure, but the shell remains closed and the month is not yet over.",
"Earned emergence completes the full Fire Phoenix awakening: red-gold wings open while Yan's public identity stays intact.",
"New wings demand new teamwork and disciplined training while Lan's separate path reaches the danger of real space.",
"The pirate crisis proves that real space has no reset, while Yan continues training far away on another planet.",
"Reunions, borrowed names and guarded conversations preserve childhood connections without collapsing the walls around private knowledge.",
"Nana protects Lan's breakthrough to the second threshold while Yan's already earned strength remains its own distinct foundation.",
"Shrek's preliminary scan and qualifier briefing place the children under institutional scrutiny before the volcanic test begins.",
"Ground Fire Lizards and a much greater dragon threat turn the qualifier into a test of coordination and survival.",
"False magma creates a narrow opportunity while Dorm336 survives through its own earned team route rather than forced failure.",
"Dorm333's dangerous opening and Dorm336's controlled Fire Phoenix route remain different answers to the same qualifier pressure.",
"An offer tests what advancement is worth when personal opportunity threatens the bond and future of a team.",
"Back outside the simulation, thanks and guarded conversations arrive before anyone has seen the final public score.",
"Lan remains in deep meditation as Dorm333 takes first place and Dorm336's own route earns second.",
"Lan wakes at five hundred and five Spiritual Power, while adults seek answers his teammates will not casually surrender.",
"Yin Tianfan's account puts ambition and consequence in perspective as the Lucky Wheel doorway approaches.",
"The Lucky Wheel gives Dorm333 distinct rewards, each carrying its own practical limits and next responsibilities.",
"Six teams enter the next simulated forest round under separate scoring, random transfer and rules that punish careless assumptions.",
"Training ambitions meet the pain and practical costs of improvement as the trio changes how it moves through the forest.",
"A wounded golden ape and palm-type bear guard a rooted immortal herb; the children withdraw without resolving the stalemate."
]
ART = {1:'06-extreme-north.jpg',3:'08-first-awakening.jpg',6:'07-first-bond.jpg',33:'03-protected-cocoon.jpg',34:'03-protected-cocoon.jpg',35:'01-first-flight.jpg',36:'02-team336.jpg',46:'04-ranking-corridor.jpg',47:'04-ranking-corridor.jpg',52:'05-amiable-beasts.jpg'}
TRAILER = """Beneath the same dawn, two beginnings take shape. One mystery waits beneath northern ice. Another grows inside an ordinary family, protected by a name the world is allowed to know. Yan Shuo. Behind that public identity is Yan Shuo'er, a girl whose beauty and unusual gifts make protection necessary. The disguise must never become a cage around her strength. A flawed first soul spirit becomes a living bond. Friendship becomes trust, rivalry becomes training, and no earned gain arrives without consequence. Beside Lan Xuanyu's unfolding story, Dorm Three Three Six must keep its own place: Yan, Song Yichen, and Luo Haoran, learning to move as a team. Through a protected cocoon and an earned awakening, red-gold wings finally open. But strength does not solve every problem. At the edge of the published story, two wounded beasts guard an immortal herb, and the children still have to decide what they can honestly afford. Fire Phoenix. Strength has a memory. So does the world."""


def stage_guard(n):
    if n <= 2:return 'Unawakened childhood. No ring, spirit bond or physical wings.'
    if n <= 5:return 'Juvenile martial soul only. No acquired ring or spirit, no physical wings.'
    if n <= 24:return 'First-ring era: Dawnflame Kite and yellow first ring; no full wings or true flight.'
    if n <= 32:return 'Consult this chapter for second-spirit/ring specifics; no full earned wings yet. No public identity reveal.'
    if n <= 34:return 'Closed opaque cocoon; no emergence, no visible unclothed body, no completed flight.'
    return 'Earned full Fire Phoenix: red-gold/violet/iron-dark wings where released; no fourth ring, deity powers or identity reveal.'


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,required=True);a=ap.parse_args()
    out=Path(__file__).resolve().parents[1];root=a.source
    head=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
    project=root/'soul_land_4_fire_phoenix'
    manifest=json.loads((project/'foundation/CURRENT_STATE_MANIFEST.json').read_text())
    if manifest['latest_fic_chapter'] != 52:raise SystemExit('Source edge changed: re-review storyboard before regenerating.')
    chapters=[]
    for n,beat in enumerate(BEATS,1):
        rel=f'chapters/Chapter_{n:02d}.md';p=project/rel;raw=p.read_bytes();text=raw.decode()
        title=re.sub(r'^# Chapter \d+\s*[:—-]\s*','',text.splitlines()[0])
        chapters.append(dict(number=n,title=title,beat=beat,source=rel,sha256=hashlib.sha256(raw).hexdigest(),art=ART.get(n),visual_status='illustrated arc keyframe' if n in ART else 'designed storyboard card; dedicated scene art not yet made',guard=stage_guard(n),shot=f'Open on the setting and participants supported by Chapter {n}; frame this beat without adding an outcome: {beat} End within the published chapter boundary. {stage_guard(n)}',source_url=f'https://github.com/gm5206663-bit/soul-land-universal-kit/blob/{head}/soul_land_4_fire_phoenix/{rel}'))
    data=dict(schema_version=1,source_revision=head,published_edge=52,scope='Illustrated media overview and chapter storyboard, not 52 animated episodes.',approved_reference='assets/00-approved-reference.png',reference_approval='User said Ok to the beauty-preserved test, then Continue. Working visual direction only; not approval of all new scenes or canonical costume.',chapters=chapters)
    (out/'metadata/chapters.json').write_text(json.dumps(data,indent=2)+'\n')
    scripts=[TRAILER]
    for start in range(0,52,6):
        group=chapters[start:start+6]
        scripts.append(' '.join(f"Chapter {x['number']}. {x['title']}. {x['beat']}" for x in group).replace('Dorm333', 'Dorm Three Three Three').replace('Dorm336', 'Dorm Three Three Six'))
    assert len(scripts)==10
    for i,t in enumerate(scripts):
        assert len(t)<=1500,(i,len(t))
        (out/'audio'/f'{i:02d}-script.txt').write_text(t+'\n')
        print(i,len(t))
    lines=['# Fire Phoenix — chapter visual production board','',f'Source revision: `{head}`. Published line only; no candidate promotion.','', 'This is a 52-chapter storyboard. Only rows explicitly mapped to art have generated scene keyframes. Other rows are designed chapter cards and shot plans, not finished scene illustrations.','']
    for x in chapters:
        lines += [f"## {x['number']:02d} · {x['title']}",'',x['beat'],'',f"- Source: [{x['source']}]({x['source_url']})",f"- Visual: {x['visual_status']}.",f"- Guard: {x['guard']}",f"- Shot plan: {x['shot']}",'']
    (out/'CHAPTER-BOARD.md').write_text('\n'.join(lines))

if __name__=='__main__':main()
