"""Adversarial offline fixtures. Synthetic values are not fiction decisions."""
from pathlib import Path
import json
import shutil
import tempfile
import unittest
import manage


class FoundationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        base = Path(self.tmp.name)
        self.root = base/'project'
        shutil.copytree(manage.ROOT, self.root, ignore=shutil.ignore_patterns('__pycache__'))
        workflow = base/'.github/workflows/dragon-phoenix-foundation.yml'
        workflow.parent.mkdir(parents=True)
        workflow.write_text('# fixture target for parent-repository navigation link\n')

    def change(self, relative, change):
        path = self.root/relative
        data = json.loads(path.read_text())
        change(data)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

    def assert_caught(self, expected):
        errors = manage.validate(self.root, check_generated=False)
        self.assertTrue(any(expected in error for error in errors), (expected, errors))

    def test_clean_foundation_passes_integrity(self):
        self.assertEqual(manage.validate(self.root), [])

    def test_integrity_is_not_readiness(self):
        self.assertEqual(manage.validate(self.root), [])
        self.assertTrue(manage.blockers(self.root))
        self.assertTrue(any('W01' in b for b in manage.blockers(self.root)))

    def test_unquoted_ruling_has_explicit_limit(self):
        self.change('foundation/AUTHOR_RULINGS.json', lambda x: x['rulings'][0].update(verbatim_limit=None))
        self.assert_caught('provenance limit')

    def test_reconstructed_quote_cannot_claim_verbatim(self):
        self.change('foundation/AUTHOR_RULINGS.json', lambda x: x['rulings'][0].update(provenance_kind='verbatim-author-message'))
        self.assert_caught('mislabeled verbatim')

    def test_duplicate_ruling(self):
        self.change('foundation/AUTHOR_RULINGS.json', lambda x: x['rulings'].append(x['rulings'][0].copy()))
        self.assert_caught('duplicate ruling')

    def test_duplicate_source(self):
        self.change('research/SOURCE_RECEIPTS.json', lambda x: x['sources'].append(x['sources'][0].copy()))
        self.assert_caught('duplicate source')

    def test_metadata_is_not_visual_review(self):
        self.change('research/SOURCE_RECEIPTS.json', lambda x: next(s for s in x['sources'] if s['id']=='D01').update(scene_reviewed=True))
        self.assert_caught('cannot prove a scene')

    def test_content_id_is_not_printed_chapter(self):
        self.change('research/SOURCE_RECEIPTS.json', lambda x: next(s for s in x['sources'] if s['id']=='M01')['catalog'][1].update(cid='2'))
        self.assert_caught('content ID distinction')

    def test_source_pin_hash(self):
        self.change('research/SOURCE_RECEIPTS.json', lambda x: next(s for s in x['sources'] if s['id']=='AT01').update(sha256='wrong'))
        self.assert_caught('source hash mismatch')

    def test_visual_flag_needs_visual_receipt(self):
        self.change('state/CURRENT_STATE.json', lambda x: x['coverage'].update(donghua_scenes_verified=True))
        self.assert_caught('coverage flag lacks visual evidence')

    def test_maternal_flag_needs_specific_scene(self):
        self.change('state/CURRENT_STATE.json', lambda x: x['coverage'].update(maternal_spear_scene_verified=True))
        self.assert_caught('maternal spear flag lacks')

    def test_visual_review_needs_exact_location(self):
        self.change('research/SOURCE_RECEIPTS.json', lambda x: next(s for s in x['sources'] if s['id']=='D01').update(scene_reviewed=True, status='visual-reviewed'))
        self.assert_caught('exact panels/timestamps')

    def test_unknown_reference(self):
        self.change('state/CURRENT_STATE.json', lambda x: x['talent'].update(source_refs=['NONEXISTENT']))
        self.assert_caught('unknown reference ID')

    def test_work_inventory_cannot_shrink(self):
        self.change('state/CURRENT_STATE.json', lambda x: x['work'].pop())
        self.assert_caught('work inventory cannot shrink')

    def test_work_needs_closure(self):
        self.change('state/CURRENT_STATE.json', lambda x: x['work'][0].update(status='resolved'))
        self.assert_caught('closure evidence')

    def test_closure_must_exist(self):
        self.change('state/CURRENT_STATE.json', lambda x: x['work'][0].update(status='resolved', closure_evidence=['missing.md']))
        self.assert_caught('closure evidence not found')

    def test_exact_rank_without_derivation(self):
        self.change('state/CURRENT_STATE.json', lambda x: x['opening_state'].update(cultivation_rank=43))
        self.assert_caught('lacks causal development output')

    def test_zero_is_not_a_solution_to_unknown_rank(self):
        self.change('state/CURRENT_STATE.json', lambda x: x['opening_state'].update(cultivation_rank=0))
        self.assert_caught('accepted state lacks sources')

    def test_causal_fixture_can_supply_one_field_not_full_readiness(self):
        # Entirely synthetic regression fixture, not accepted project history.
        log = manage.read(self.root, 'state/development_events.json')
        event = {k:'synthetic test fixture' for k in log['required_event_fields']}
        event.update(id='TEST_EVENT', status='accepted', source_refs=['AT01'], state_outputs={'cultivation_rank':45})
        self.change('state/development_events.json', lambda x: x['events'].append(event))
        self.change('state/CURRENT_STATE.json', lambda x: (x['opening_state'].update(cultivation_rank=45), x['derivation_evidence'].update(cultivation_rank={'event_ids':['TEST_EVENT'],'source_refs':['AT01']})))
        self.assertEqual(manage.validate(self.root, check_generated=False), [])
        self.assertTrue(manage.blockers(self.root))

    def test_prose_file_cannot_hide_in_empty_chapter_directory(self):
        (self.root/'chapters/Chapter_001.md').write_text('Synthetic fixture, not story prose.')
        self.assert_caught('prose exists')

    def test_plan_does_not_consume_source_units(self):
        self.change('state/CURRENT_STATE.json', lambda x: x['coverage'].update(chapter_001_consumed_units=['N01']))
        self.assert_caught('has not consumed')

    def test_plan_cannot_call_itself_prose(self):
        self.change('canon_coverage/CHAPTER_001.json', lambda x: x.update(prose_exists=True))
        self.assert_caught('must not impersonate')

    def test_incomplete_event(self):
        self.change('state/adaptation_events.json', lambda x: x['events'].append({'id':'TEST','source_refs':['AT01']}))
        self.assert_caught('incomplete event')

    def test_duplicate_event(self):
        self.change('state/adaptation_events.json', lambda x: x['events'].extend([{'id':'TEST'},{'id':'TEST'}]))
        self.assert_caught('duplicate event IDs')

    def test_broken_local_link(self):
        with (self.root/'README.md').open('a') as f:
            f.write('\n[fixture](missing-foundation.md)\n')
        self.assert_caught('broken local link')

    def test_media_stays_removed(self):
        (self.root/'image.png').write_bytes(b'fixture')
        self.assert_caught('no media')

    def test_possible_secret_is_rejected_without_printing_secret(self):
        (self.root/'fixture.md').write_text('ghp_'+'a'*32)
        self.assert_caught('possible secret in fixture.md')

    def test_generated_status_drift(self):
        (self.root/'STATUS.md').write_text('pretend ready')
        self.assertIn('generated status drift', manage.validate(self.root))

    def test_generated_manifest_drift(self):
        self.change('state/FILE_MANIFEST.json', lambda x: x['files'].pop())
        self.assertIn('file manifest drift', manage.validate(self.root))

    def test_generated_map_drift(self):
        (self.root/'CODEX.md').write_text('incomplete map')
        self.assertIn('generated file map drift', manage.validate(self.root))


# One independent fixture per recorded guard. Explicit names keep CI useful.
MUTATIONS = [
 ('native_identity','identity.native',False,'native identity'),
 ('male_identity','identity.sex','female','male identity'),
 ('parentage','identity.parents',[],'parentage'),
 ('conception_onset','talent.onset','awakening','begin at conception'),
 ('whole_existence','talent.whole_existence',False,'narrowed to learning'),
 ('non_sentience','talent.sentient',True,'sentient Talent'),
 ('talent_not_soul_slot','talent.occupies_martial_soul_slot',True,'not a martial soul'),
 ('two_souls','martial_souls.number',3,'two-soul lock'),
 ('parental_soul_pair','martial_souls.foundations',['Other'],'approved soul foundations'),
 ('maternal_adoption','martial_souls.maternal_design_authority','novel','adoption must be explicit'),
 ('maternal_novel_claim','martial_souls.maternal_novel_name_verified',True,'verified novel claim'),
 ('ancestor_contact','inheritance.ancestor_contact',True,'no ancestor contact'),
 ('inherited_memory','inheritance.ancestor_learned_memory',True,'no inherited learned'),
 ('genealogy_branch','inheritance.author_branch_great_grandparents',[],'genealogy branch lock'),
 ('ma_future','relationships.ma_future','romance','Ma future remains open'),
 ('trusted_disclosure','relationships.twins_disclosure','public','disclosure scope lock'),
 ('mu_en_role','relationships.mu_en_role','father','Mu En relationship'),
 ('first_meeting','opening.earlier_huo_contact',True,'no earlier Huo contact'),
 ('companions','opening.first_meeting_companions',[],'first-meeting companions'),
 ('no_childhood_chronicle','opening.childhood_chronicle',True,'childhood prologue'),
 ('elite_resources','upbringing.top_resources',False,'erase locked upbringing'),
 ('sustained_teaching','upbringing.sustained_guidance',False,'erase locked upbringing'),
 ('growth_advantage','upbringing.much_faster_growth_required',False,'erase locked upbringing'),
 ('adapted_demand','upbringing.demand_mitigated_by_adaptation',False,'erase locked upbringing'),
 ('no_fake_chapter_count','project.chapters_written',1,'zero chapters'),
 ('correct_project_owner','project.id','sl4-fire-phoenix','cross-project state')
]

def make_mutation_test(path, value, expected):
    def test(self):
        def mutate(data):
            parts = path.split('.')
            for key in parts[:-1]:
                data = data[key]
            data[parts[-1]] = value
        self.change('state/CURRENT_STATE.json', mutate)
        self.assert_caught(expected)
    return test

for name, path, value, expected in MUTATIONS:
    setattr(FoundationTests, 'test_guard_'+name, make_mutation_test(path,value,expected))


if __name__ == '__main__':
    unittest.main()
