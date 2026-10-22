#!/usr/bin/env python3
"""Offline foundation integrity and honest pre-draft readiness, stdlib only.

No network calls; no source download; no prose generation. An integrity PASS is
not author approval or external canon verification. Exit 2 means not ready.
"""
from pathlib import Path
from urllib.parse import unquote, urlparse
import argparse
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'__pycache__', '.git', '.pytest_cache'}
BINARY_MEDIA = {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.mp4', '.mp3', '.wav', '.zip', '.pdf', '.pptx'}
GENERATED = {'STATUS.md', 'CODEX.md', 'FOUNDATION_INDEX.md', 'state/FILE_MANIFEST.json'}
COVERAGE_IDS = {'premise', 'character', 'family', 'relationships', 'timeline', 'places',
                'factions', 'economy', 'power', 'talent', 'souls', 'rings', 'skills',
                'combat', 'engineering', 'knowledge', 'canon', 'inventory', 'continuity',
                'routes', 'voice', 'foreshadowing', 'workflow', 'governance'}


def read(root, relative):
    return json.loads((root / relative).read_text(encoding='utf-8'))


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def files(root):
    return sorted(p.relative_to(root).as_posix() for p in root.rglob('*')
                  if p.is_file() and not set(p.relative_to(root).parts).intersection(EXCLUDED)
                  and p.suffix != '.pyc')


def blockers(root):
    s = read(root, 'state/CURRENT_STATE.json')
    result = [f"{w['id']}: {w['description']}" for w in s['work'] if w['status'] != 'resolved']
    unknown = [k for k, v in s['opening_state'].items() if v is None]
    if unknown:
        result.append('Undetermined opening fields: ' + ', '.join(unknown))
    if not s['relationships']['exact_witnesses']:
        result.append('Exact trusted-circle witness history unassigned')
    if not s['opening']['trip_history']:
        result.append('Trip purpose and prior companion history unassigned')
    for key in ['manhua_scenes_verified', 'donghua_scenes_verified', 'maternal_spear_scene_verified']:
        if not s['coverage'][key]:
            result.append('Source gate pending: ' + key)
    return result


def status_text(root):
    s = read(root, 'state/CURRENT_STATE.json')
    lines = ['# Foundation status — generated, not a second state owner', '',
             f"Updated: {s['updated']} · stage: **{s['project']['stage']}** · chapters: **{s['project']['chapters_written']}**", '',
             'Source of truth: [CURRENT_STATE.json](state/CURRENT_STATE.json).',
             'Regenerate with `python3 tools/manage.py build`; do not hand-edit.', '',
             '## Current checkpoint', '',
             f"Working name: **{s['identity']['working_name']} ({s['identity']['hanzi']})**.",
             'The name and title are delegated design, not verbatim author wording.',
             'The approved parental/twin-soul/ancestry/upbringing premises are recorded in the current state.',
             'No opening numerical power panel has been accepted. Null means undetermined, not zero.', '',
             '## Chapter readiness', '']
    b = blockers(root)
    lines.append('**BLOCKED — do not draft or publish Chapter 1.**' if b else '**All recorded readiness prerequisites resolved; run the full gate before drafting.**')
    lines += [''] + ['- ' + x for x in b]
    lines += ['', '## Evidence boundary', '',
              'Novel 1.1–1.4 narrative bodies read; manhua catalog and donghua EP1 metadata located.',
              'No manhua panel or donghua timestamp map is claimed complete.',
              'See [receipts](research/SOURCE_RECEIPTS.json), [crosswalk](foundation/SOURCE_CROSSWALK.md)',
              'and [open work](foundation/OPEN_WORK.md).', '',
              'Structural PASS is separate from this readiness result and from creative acceptance.', '']
    return '\n'.join(lines)


def codex_text(names):
    lines = ['# File map — generated', '', 'One project home; no prose or media has been published.', '',
             'Regenerate with `python3 tools/manage.py build`.', '']
    for name in names:
        if name.endswith('.gitkeep'):
            lines.append('- `'+name+'` — empty chapter-directory marker, not a chapter')
        else:
            lines.append(f'- [{name}]({name})')
    return '\n'.join(lines) + '\n'


def foundation_index_text(root):
    coverage = read(root, 'foundation/FILE_REQUIREMENTS.json')
    lines = ['# Complete foundation index — generated', '',
             'Practical file architecture is present. This is not a declaration that all',
             'opening numbers, source mappings or future decisions are resolved.', '',
             'Working story: **The Dragon and the Phoenix**, with **Yan Jingheng**.',
             'Read [status](STATUS.md) for actual readiness and [all files](CODEX.md) for the inventory.', '',
             '## Foundation functions', '']
    for category in coverage['categories']:
        lines += ['### '+category['title'], '']
        lines += ['- ['+p.split('/')[-1]+']('+p+')' for p in category['documents']]
        lines += ['']
    lines += ['## Structured owners', '',
              '- [Current state](state/CURRENT_STATE.json): accepted premise and unresolved numerical fields.',
              '- [Timeline graph](state/TIMELINE.json): relative source/planning order, not written scenes.',
              '- [Continuity events](state/continuity_events.json): written scene changes; currently empty.',
              '- [Author rulings](foundation/AUTHOR_RULINGS.json): exact available wording and provenance limits.',
              '- [Source receipts](research/SOURCE_RECEIPTS.json): read, located, partial and unreviewed scopes.',
              '- [Coverage requirements](foundation/FILE_REQUIREMENTS.json): file-presence/content contract.',
              '- [GitHub review](research/GITHUB_FOUNDATION_REVIEW.md): structural references, no holder transfer.',
              '', '## What remains', '',
              'The file set is expanded, but [open research work](foundation/OPEN_WORK.md) remains.',
              'No chapter, artwork or research-image pack has been published.', '']
    return '\n'.join(lines)


def validate_expansion(root, require):
    coverage = read(root, 'foundation/FILE_REQUIREMENTS.json')
    ids = [c['id'] for c in coverage['categories']]
    require(set(ids) == COVERAGE_IDS and len(ids) == len(COVERAGE_IDS), 'foundation coverage categories cannot disappear or duplicate')
    threshold = coverage['minimum_words_per_document']
    require(isinstance(threshold, int) and threshold >= 40, 'foundation content minimum cannot be weakened')
    for category in coverage['categories']:
        require(bool(category['documents']), 'foundation coverage category is empty')
        for name in category['documents']:
            path = root/name
            require(path.is_file(), 'foundation coverage missing document: '+name)
            if path.is_file():
                require(len(path.read_text(encoding='utf-8').split()) >= threshold, 'foundation document is empty/thin: '+name)
    timeline = read(root, 'state/TIMELINE.json')
    nodes = {e['id']:e for e in timeline['events']}
    require(len(nodes) == len(timeline['events']), 'duplicate timeline event ID')
    require(timeline['anchor_id'] == 'T_FIRST_MEETING' and timeline['anchor_id'] in nodes, 'opening timeline anchor missing or moved')
    for event in timeline['events']:
        require(event['written_in_fic'] is False, 'planning timeline is not a written scene ledger')
        for earlier in event['after']:
            require(earlier in nodes, 'timeline dependency does not exist: '+earlier)
    required_edges = [('T_JOURNEY','T_DEPARTURE'), ('T_STREAM_PREP','T_JOURNEY'),
                      ('T_FIRST_MEETING','T_STREAM_PREP'), ('T_FIRST_MEETING','T_PRETRIP'),
                      ('T_MEAL','T_FIRST_MEETING'), ('T_FOREST_APPROACH','T_FOLLOW_DECISION')]
    for later, earlier in required_edges:
        require(later in nodes and earlier in nodes and earlier in nodes[later]['after'], 'opening chronology constraint missing: '+later+' after '+earlier)
    visiting, complete = set(), set()
    def walk(name):
        if name in visiting:
            require(False, 'timeline dependency cycle')
            return
        if name in complete:
            return
        visiting.add(name)
        for previous in nodes[name]['after']:
            if previous in nodes:
                walk(previous)
        visiting.remove(name)
        complete.add(name)
    for name in nodes:
        walk(name)
    require(read(root, 'state/continuity_events.json')['events'] == [], 'foundation-only release has no written continuity events')


def validate(root, check_generated=True):
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    try:
        s = read(root, 'state/CURRENT_STATE.json')
        rulings = read(root, 'foundation/AUTHOR_RULINGS.json')['rulings']
        sources = read(root, 'research/SOURCE_RECEIPTS.json')['sources']
        proposal = read(root, 'state/design_proposals.json')
        plan = read(root, 'canon_coverage/CHAPTER_001.json')
        rs = {r['id']: r for r in rulings}
        ss = {x['id']: x for x in sources}
        require(len(rs) == len(rulings), 'duplicate ruling ID')
        require(len(ss) == len(sources), 'duplicate source ID')
        for r in rulings:
            require(r['classification'] == 'author-lock', 'ruling classification missing')
            if r['verbatim'] is None:
                require(bool(r.get('verbatim_limit')), 'unquoted ruling must expose provenance limit')
                require(r['provenance_kind'] != 'verbatim-author-message', 'reconstructed quote mislabeled verbatim')
            else:
                require(r['provenance_kind'] == 'verbatim-author-message', 'quote provenance inconsistent')
        require(s['project']['id'] == 'sl2-dragon-phoenix', 'cross-project state contamination')
        require(s['identity']['native'] is True, 'native identity lock')
        require(s['identity']['sex'] == 'male', 'male identity lock')
        require(s['identity']['parents'] == ['Yan Shaozhe', 'Cai Mei’er'], 'parentage lock')
        require(s['talent']['onset'] == 'conception', 'Talent must begin at conception')
        require(s['talent']['whole_existence'] is True, 'Talent cannot be narrowed to learning')
        require(s['talent']['sentient'] is False, 'no sentient Talent assistant')
        require(s['talent']['occupies_martial_soul_slot'] is False, 'Talent is not a martial soul')
        require(s['martial_souls']['number'] == 2, 'two-soul lock')
        require(s['martial_souls']['foundations'] == ['Bright Phoenix', 'Evil-Dispelling Dragon Soul Spear'], 'approved soul foundations')
        require(s['martial_souls']['maternal_design_authority'] == 'author-adopted-donghua', 'maternal adaptation adoption must be explicit')
        require(s['martial_souls']['maternal_novel_name_verified'] is False, 'do not promote maternal spear to verified novel claim')
        require(s['inheritance']['ancestor_contact'] is False, 'no ancestor contact')
        require(s['inheritance']['ancestor_learned_memory'] is False, 'no inherited learned memories')
        require(s['inheritance']['author_branch_great_grandparents'] == ['Long Xiaoyao', 'Ye Xishui'], 'author genealogy branch lock')
        require(s['relationships']['ma_future'] == 'open', 'Ma future remains open')
        require(s['relationships']['twins_disclosure'] == 'trusted-circle', 'disclosure scope lock')
        require(s['relationships']['mu_en_role'] == 'grandmaster', 'Mu En relationship lock')
        require(s['opening']['earlier_huo_contact'] is False, 'no earlier Huo contact')
        require(s['opening']['first_meeting_companions'] == ['Tang Ya', 'Bei Bei'], 'first-meeting companions')
        require(s['opening']['childhood_chronicle'] is False, 'no exhaustive childhood prologue')
        for value in s['upbringing'].values():
            if isinstance(value, bool):
                require(value is True, 'do not erase locked upbringing advantage')
        require(proposal['status'] == 'proposals-not-current-state', 'proposal/current-state boundary')
        require(plan['status'] == 'plan-only' and plan['prose_exists'] is False, 'foundation must not impersonate written Chapter 1')
        require(s['project']['stage'] == 'foundation' and s['project']['chapters_written'] == 0, 'this foundation release has zero chapters')
        require(s['coverage']['chapter_001_consumed_units'] == [], 'a plan has not consumed source units in prose')
        chapters = [x for x in files(root) if x.startswith('chapters/') and not x.endswith('.gitkeep')]
        require(not chapters, 'prose exists in a foundation-only release')
        for source in sources:
            parsed = urlparse(source['url'])
            require(parsed.scheme == 'https' and bool(parsed.netloc), 'source URL must be explicit HTTPS')
            if source.get('scene_reviewed'):
                require(source['status'] in {'primary-read', 'visual-reviewed'}, 'metadata/empty/secondary source cannot prove a scene')
                if source['medium'] in {'manhua', 'donghua'}:
                    require(bool(source.get('scene_location')), 'visual review needs exact panels/timestamps')
        require(ss['M01']['catalog'][0]['cid'] == '2' and ss['M01']['catalog'][1]['cid'] == '3', 'Tencent row/printed chapter/content ID distinction')
        require('prologue' in ss['M01']['catalog'][0]['display_label'], 'cid 2 is the prologue')
        require(ss['AT01']['commit'] == '1b43ad6cda12e97fefeaedc83ee3e415068428a6', 'Talent authority pin changed without review')
        require(ss['AT01']['sha256'] == 'eaced0a52af1ca30c54a4352487a08dc38fc8e39cac274b4ff336b713e723b85', 'Talent source hash mismatch')
        for medium in ['manhua', 'donghua']:
            if s['coverage'][medium+'_scenes_verified']:
                require(any(x['medium'] == medium and x.get('scene_reviewed') and x['status'] == 'visual-reviewed' for x in sources), 'coverage flag lacks visual evidence: '+medium)
        if s['coverage']['maternal_spear_scene_verified']:
            require(any(x['medium'] == 'donghua' and x.get('scene_reviewed') and x['status'] == 'visual-reviewed' and 'maternal-spear' in x.get('claim_tags', []) for x in sources), 'maternal spear flag lacks its exact visual receipt')
        work_ids = [w['id'] for w in s['work']]
        require(work_ids == ['W01', 'W02', 'W03', 'W04', 'W05', 'W06'], 'readiness work inventory cannot shrink')
        for w in s['work']:
            require(w['status'] in {'pending', 'in-progress', 'resolved'}, 'invalid work status')
            require(isinstance(w['closure_evidence'], list), 'closure evidence must be a list')
            if w['status'] == 'resolved':
                require(bool(w['closure_evidence']), 'resolved work requires closure evidence')
                for evidence in w['closure_evidence']:
                    require(evidence in ss or (root/evidence.split('#')[0]).is_file(), 'closure evidence not found')
        events = read(root, 'state/development_events.json')['events']
        event_ids = [e['id'] for e in events]
        require(len(event_ids) == len(set(event_ids)), 'duplicate development event ID')
        for key, value in s['opening_state'].items():
            if value is not None:
                evidence = s['derivation_evidence'].get(key, {})
                require(bool(evidence.get('source_refs')), 'accepted state lacks sources: '+key)
                require(any(e.get('status') == 'accepted' and e.get('state_outputs', {}).get(key) == value and e['id'] in evidence.get('event_ids', []) for e in events), 'accepted state lacks causal development output: '+key)
        def references(node):
            if isinstance(node, dict):
                for k, value in node.items():
                    if k in {'ruling_refs', 'source_refs', 'source_anchor', 'novel_opening_read', 'candidate_units'}:
                        allowed = rs if k == 'ruling_refs' else ss
                        require(isinstance(value, list), 'reference field must be a list')
                        for ref in value:
                            require(ref in allowed, 'unknown reference ID: '+str(ref))
                    else:
                        references(value)
            elif isinstance(node, list):
                for item in node:
                    references(item)
        for p in root.rglob('*.json'):
            if not set(p.relative_to(root).parts).intersection(EXCLUDED):
                references(json.loads(p.read_text(encoding='utf-8')))
        for name in ['development_events', 'adaptation_events', 'resource_events', 'ring_candidates']:
            log = read(root, 'state/'+name+'.json')
            require(len({e['id'] for e in log['events']}) == len(log['events']), 'duplicate event IDs in '+name)
            for event in log['events']:
                require(all(k in event for k in log['required_event_fields']), 'incomplete event in '+name)
        validate_expansion(root, require)
        all_files = files(root)
        for name in all_files:
            p = root/name
            require(p.suffix.lower() not in BINARY_MEDIA, 'no media in this text-only foundation: '+name)
            if p.suffix in {'.md', '.json', '.py', '.sh', '.yml'}:
                text = p.read_text(encoding='utf-8')
                require(not re.search(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,}', text), 'possible secret in '+name)
                if p.suffix == '.md':
                    for link in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
                        if urlparse(link).scheme or link.startswith('#'):
                            continue
                        target = (p.parent/unquote(link.split('#', 1)[0])).resolve()
                        require(target.exists(), 'broken local link in '+name+': '+link)
        if check_generated:
            require((root/'STATUS.md').read_text() == status_text(root), 'generated status drift')
            require((root/'CODEX.md').read_text() == codex_text(all_files), 'generated file map drift')
            require((root/'FOUNDATION_INDEX.md').read_text() == foundation_index_text(root), 'generated foundation index drift')
            require(read(root, 'state/FILE_MANIFEST.json')['files'] == all_files, 'file manifest drift')
    except (KeyError, ValueError, TypeError, OSError) as exc:
        errors.append('invalid or incomplete foundation data: '+str(exc))
    return errors


def build(root):
    (root/'STATUS.md').write_text(status_text(root), encoding='utf-8')
    (root/'FOUNDATION_INDEX.md').write_text(foundation_index_text(root), encoding='utf-8')
    if not (root/'audits/verification.json').exists():
        write_json(root/'audits/verification.json', {'status':'not-yet-run'})
    names = sorted(set(files(root)) | GENERATED)
    (root/'CODEX.md').write_text(codex_text(names), encoding='utf-8')
    write_json(root/'state/FILE_MANIFEST.json', {'schema_version':1,'scope':'All project files, including this manifest; caches excluded. Inventory, not a circular content hash.','files':names})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['build', 'verify', 'ready', 'report'])
    args = parser.parse_args()
    if args.command == 'build':
        build(ROOT)
        print('Generated status, file map and manifest. This does not certify readiness.')
        return 0
    errors = validate(ROOT)
    if errors:
        for error in errors:
            print('FAIL:', error)
        return 1
    b = blockers(ROOT)
    if args.command == 'ready':
        if b:
            print('NOT READY — no prose authorized by this gate:')
            for item in b:
                print('-', item)
            return 2
        print('READY — recorded pre-draft prerequisites resolved; human review still required.')
        return 0
    if args.command == 'report':
        command = [sys.executable, '-m', 'unittest', 'discover', '-s', 'tools', '-p', 'test_*.py']
        run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=60)
        found = re.search(r'Ran (\d+) tests?', run.stderr)
        if run.returncode or not found:
            print('FAIL: selftest report could not be certified')
            print(run.stdout + run.stderr)
            return 1
        write_json(ROOT/'audits/verification.json', {
            'date':read(ROOT, 'state/CURRENT_STATE.json')['updated'], 'structural_integrity':'PASS',
            'selftests':{'command':'python3 -m unittest discover -s tools -p test_*.py', 'cases':int(found.group(1)), 'result':'PASS'},
            'chapter_readiness':'BLOCKED' if b else 'READY',
            'readiness_blockers':b, 'file_count':len(files(ROOT)),
            'limits':'Offline technical checks and actually executed regression tests; not external-source revalidation, author approval or prose-quality review.'})
    print('PASS — foundation integrity; Chapter 1 '+('BLOCKED' if b else 'prerequisites resolved'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
