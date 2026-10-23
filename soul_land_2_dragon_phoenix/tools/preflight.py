"""Semantic checks and a generated view for the delegated opening design.

These prove consistency, not that fiction numbers are uniquely deducible from canon.
"""
import json


def opening_build_text(root):
    s = json.loads((root/'state/CURRENT_STATE.json').read_text())
    o = s['opening_state']
    lines = ['# Yan Jingheng — opening character dossier', '',
             'Generated from [the current record](state/CURRENT_STATE.json). This is',
             'revisable original-fiction design under delegation, not a canon OC stat sheet.', '',
             '## At a glance', '',
             '| Identity | Opening position |', '|---|---|',
             f"| Name | {s['identity']['working_name']} / {s['identity']['hanzi']} |",
             f"| Age | {o['exact_age']} |",
             f"| Cultivation | Rank {o['cultivation_rank']} — Soul King |",
             f"| Innate reading | {o['innate_soulforce']} |",
             '| Martial souls | Bright Phoenix; Evil-Dispelling Dragon Soul Spear |',
             '| Talent | Adaptation Talent, present from conception |',
             '| Family | Son of Yan Shaozhe and Cai Mei’er; native-born |', '',
             'Personality and story: [Core](story/CORE.md). Family map: [Cast](story/CAST.md).', '',
             '## Appearance', '']
    appearance=s['identity'].get('appearance',{})
    for key in ('hair','eyes','build','clothing'):
        if key in appearance:
            lines.append('- **'+key.title()+':** '+appearance[key])
    lines += ['', '## Body, soul and energy', '']
    labels={'reserves':'Reserves and control','physique':'Body','soul_capacity':'Soul and attention'}
    for key,label in labels.items():
        value=o[key]
        lines += ['### '+label,'']
        if isinstance(value,dict):
            lines += [value['description'],'','**Established in the authored history:** '+value['demonstrated'].replace('P1–P5','the five acquired rings').replace('P4/P5 black rings','fourth and fifth black rings'),'']
        else:
            lines += ['Not yet determined.','']
    blood=o['bloodline_expression']
    if isinstance(blood,dict):
        lines += ['### Inherited expression','',blood['phoenix'],'',blood['dragon'],'',blood['integration'],'']
    lines += ['## Rings and gifts', '',
              'The donors and gifts below are original fanfiction designs. Ages are nominal',
              'cultivation-age estimates; no passive calendar-aging mechanism is claimed.', '',
              '| Ring | Donor | Acquired/current age | Color | Gift |', '|---|---|---|---|---|']
    for ring in o['phoenix_rings'] or []:
        lines.append(f"| {ring['slot']} | {ring['donor']} | {ring['donor_cultivation_age']:,} / {ring['current_age']:,} | {ring['color']} | {ring['skill']['name']} |")
    lines += ['', '**Spear:** no rings at opening; genuinely practiced, not dormant.', '']
    for ring in o['phoenix_rings'] or []:
        skill=ring['skill'];lines += ['### '+skill['name'],'',skill['effect'],'', '**Scope:** '+skill['scope'],'']
    lines += ['Route and compatibility: [Development](power/DEVELOPMENT.md).',
              'Tactical application: [Rings and combat](power/RINGS_AND_COMBAT.md).','',
              '## Learned fighting style','']
    combat=o['combat_capabilities']
    if isinstance(combat,dict):
        lines += ['- '+x for x in combat['learned']]
        dual=combat['dual_expression']
        lines += ['','### '+dual['name'],'',dual['route'],'',dual['reliable'],'',dual['developing'],'',
                  '### Established training feats','']
        lines += ['- '+x for x in combat['feats']]
    eng=o['engineering_proficiency']
    lines += ['','## Engineering','']
    if isinstance(eng,dict):
        lines += [eng['instruction'],'']+['- '+x for x in eng['reliable']]
        lines += ['',eng['advanced_work'],'',
                  '**Certification:** actual workshop assessment; no external numbered certificate asserted.','']
    lines += ['## Owned and authorized equipment','','| Item | Function | Source |','|---|---|---|']
    for item in o['equipment'] or []:
        lines.append('| '+item['name']+' | '+item.get('function','Storage for recorded ordinary provisions/tools')+' | '+item['source']+' |')
    lines.append('')
    for item in o['equipment'] or []:
        lines.append('- **'+item['name']+':** '+item['limits'])
        if 'capacity' in item:lines.append('  Capacity: '+item['capacity']+'.')
        if 'contents' in item:lines.append('  Contents: '+'; '.join(item['contents'])+'.')
        if 'power' in item:lines.append('  Power: '+item['power']+'.')
    lines += ['','## Disclosures and trip','',
              '**Named twin-soul witnesses:** '+', '.join(s['relationships']['exact_witnesses'] or [])+'.','']
    trip=s['opening']['trip_history']
    if isinstance(trip,dict):
        friendly={'purpose':'Purpose','companions':'Companions','permission':'Permission','bounds':'Route boundary',
                  'huo_contact':'First meeting','knowledge':'Companions’ knowledge','institutional_position':'Academy position'}
        lines += ['- **'+label+':** '+trip[key] for key,label in friendly.items() if key in trip]
    lines += ['','## Limits of the record','',
              'Training feats are original off-page history, not published scenes or universal',
              'matchup guarantees. No infinite reserves, third soul, inherited learned memory,',
              'automatic mental immunity, universal purification or external cure aura is claimed.',
              'Ma’s future and later personal evolution remain open. No deleted image asset is used.','',
              '**Chapter readiness is separate:** see [Status](STATUS.md) and [Open work](operations/OPEN_WORK.md).',
              'Regenerate this view with `python3 tools/manage.py build`; do not edit live values here.','']
    return '\n'.join(lines)


def validate_preflight(root, s, sources, require):
    """Do not let work checkboxes or a matching output alone fake a complete route."""
    o=s['opening_state']
    work={w['id']:w for w in s['work']}
    history=json.loads((root/'state/development_events.json').read_text())['events']
    adaptations=json.loads((root/'state/adaptation_events.json').read_text())['events']
    flags=['manhua_scenes_verified','donghua_scenes_verified','maternal_spear_scene_verified']
    if work['W04']['status']=='resolved':
        require(all(s['coverage'][f] for f in flags), 'visual work closure needs all scene gates')
    if work['W01']['status']=='resolved':
        require(all(v is not None for v in o.values()), 'numerical work closure needs complete opening fields')
        authority=s.get('opening_state_authority',{})
        require(authority.get('classification')=='delegated-design', 'opening design authority must be explicit, not an invented author lock')
        require('R17' in authority.get('ruling_refs',[]), 'opening design needs current delegation')
        design=sources.get('DESIGN01',{})
        require(design.get('medium')=='project-design' and design.get('status')=='delegated-design' and not design.get('scene_reviewed'), 'original design cannot masquerade as external primary evidence')
        required_docs=['power/DEVELOPMENT.md','plot/CONTINUITY.md']
        for name in required_docs:
            p=root/name
            require(p.is_file() and len(p.read_text().split())>=150, 'missing substantive preflight support: '+name)
        events=json.loads((root/'state/development_events.json').read_text())['events']
        if s.get('opening_state_authority',{}).get('classification')=='delegated-design':
            accepted=[e for e in events if e.get('status')=='accepted']
            months=[e.get('age_months_grid') for e in accepted]
            require(all(type(n) is int and n>=0 for n in months), 'development needs nonnegative month grid')
            if all(type(n) is int for n in months):
                require(months==sorted(set(months)), 'development month grid must increase without duplicates')
            require(bool(accepted) and accepted[0].get('epoch')=='conception-to-birth', 'development must include prenatal foundation')
            checkpoints=[e for e in accepted if e.get('epoch')=='opening-checkpoint']
            require(len(checkpoints)==1 and checkpoints[0].get('state_outputs')==o, 'opening checkpoint must match the whole current build')
            if checkpoints:
                require(type(o['exact_age']) is int and checkpoints[0].get('age_months_grid')==12*o['exact_age'], 'opening age must match the authored month grid')
            for e in accepted:
                require(e.get('authority')=='delegated-design' and 'DESIGN01' in e.get('source_refs',[]), 'authored development requires explicit original-design provenance')
                for key in ('prior_state','input','teacher_or_source','resources','task','result','cost','integration','witnesses','later_proof'):
                    require(bool(e.get(key)), 'development causal field cannot be empty: '+key)
    rank=o['cultivation_rank']
    if rank is not None:
        require(type(rank) is int and 1<=rank<=99, 'opening cultivation rank must be a native mortal positive rank')
    if o['innate_soulforce'] is not None:
        require(type(o['innate_soulforce']) is int and o['innate_soulforce']>0, 'innate reading must be positive')
    if work['W02']['status']=='resolved':
        for key in ('phoenix_rings','spear_rings'):
            rings=o[key]
            require(isinstance(rings,list), 'ring progression closure needs actual ring lists')
            if not isinstance(rings,list):
                continue
            require([r.get('slot') for r in rings]==list(range(1,len(rings)+1)), 'ring slots must be contiguous')
            require(len({r.get('id') for r in rings})==len(rings), 'ring IDs must not duplicate')
            if type(rank) is int:
                require(len(rings)<=rank//10, 'ring count exceeds cultivation stage')
            for r in rings:
                require(r.get('origin_class')=='original-design' and r.get('canonical_species_claim') is False and 'DESIGN01' in r.get('source_refs',[]), 'original ring donor provenance cannot be promoted to canon')
                for field in ('donor','availability','trait','support','absorption_basis','cost'):
                    require(bool(r.get(field)), 'ring history is missing '+field)
                age=r.get('current_age');original=r.get('donor_cultivation_age')
                require(type(age) is int and age>0, 'ring age must be positive')
                if type(age) is int:
                    color='white' if age<100 else 'yellow' if age<1000 else 'purple' if age<10000 else 'black' if age<100000 else 'red'
                    require(r.get('color')==color, 'ring age and color mismatch')
                if age!=original:
                    require(bool(r.get('age_change_event_ids')), 'ring age changes require an earned aging mechanism')
                    require(any(e.get('id') in r.get('age_change_event_ids',[]) and e.get('status')=='accepted' and e.get('ring_age_outputs',{}).get(r['id'])==age for e in adaptations), 'ring aging needs an actual matching adaptation output')
                require(type(r.get('acquired_age_months')) is int and r['acquired_age_months']<=12*o['exact_age'], 'ring cannot be acquired after the opening')
                acquisitions=[e for e in history if r.get('id') in e.get('ring_acquired_ids',[])]
                require(len(acquisitions)==1 and acquisitions[0].get('age_months_grid')==r.get('acquired_age_months'), 'ring acquisition needs a matching dated development event')
                skill=r.get('skill',{})
                require(all(skill.get(k) for k in ('name','effect','scope')) and skill.get('origin_class')=='original-design', 'ring gift needs explicit original effect and scope')
        if type(rank) is int and isinstance(o['phoenix_rings'],list) and isinstance(o['spear_rings'],list):
            require(max(len(o['phoenix_rings']),len(o['spear_rings']))==rank//10, 'cultivation stage needs its completed breakthrough ring')
    if work['W03']['status']=='resolved':
        require(bool(o['engineering_proficiency']) and bool(o['engineering_certification']), 'engineering closure needs actual work and certification disposition')
        cert=o['engineering_certification']
        if isinstance(cert,dict) and cert.get('external_certificate'):
            refs=cert.get('exam_source_refs',[])
            require(any(sources.get(r,{}).get('status')=='primary-read' and sources.get(r,{}).get('scene_reviewed') for r in refs), 'external engineering certificate requires primary exam evidence')
    if work['W06']['status']=='resolved':
        require(bool(s['relationships']['exact_witnesses']) and isinstance(s['opening']['trip_history'],dict) and bool(o['equipment']), 'opening logistics closure needs witnesses, trip and equipment')
        for item in o['equipment'] or []:
            require(all(item.get(k) for k in ('id','name','owner','source','limits')), 'equipment needs identity, ownership, provenance and limits')
    if work['W05']['status']=='resolved':
        p=root/'plot/CONTINUITY.md'
        require(p.is_file() and len(p.read_text().split())>=150, 'butterfly closure needs substantive consequence assessment')
