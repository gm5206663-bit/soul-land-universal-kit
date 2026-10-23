"""Preflight semantics. Positive source examples below are temporary test fixtures.

Nothing generated here is a real source review or a project design revision.
"""
import subprocess
import sys
import unittest
from test_foundation import FoundationTests as Base
import manage


# Reuse setup/assertions without duplicating the original 66 tests in discovery.
class PreflightTests(unittest.TestCase):
    setUp = Base.setUp
    change = Base.change
    assert_caught = Base.assert_caught

    def change_ring(self, change):
        self.change('state/CURRENT_STATE.json', lambda x: change(x['opening_state']['phoenix_rings'][0]))

    def change_event(self, change):
        self.change('state/development_events.json', lambda x: change(x['events'][0]))

    def ready_cli(self):
        manage.build(self.root)
        return subprocess.run([sys.executable,str(self.root/'tools/manage.py'),'ready'],capture_output=True,text=True)

    def synthetic_reviewed_fixture(self):
        # Fictional exact locations, confined to TemporaryDirectory.
        def sources(x):
            for s in x['sources']:
                if s['id'] in {'M01','D01'}:
                    s.update(status='visual-reviewed', scene_reviewed=True,
                             scene_location='SYNTHETIC REGRESSION FIXTURE: page 1 / 00:00–00:01',
                             scope='Synthetic test data, NOT a real source review')
                    if s['id']=='D01':
                        s['claim_tags']=['maternal-spear']
        self.change('canon/SOURCE_RECEIPTS.json', sources)
        def state(x):
            for k in ('manhua_scenes_verified','donghua_scenes_verified','maternal_spear_scene_verified'):
                x['coverage'][k]=True
            x['work'][3].update(status='resolved',closure_evidence=['M01','D01'])
        self.change('state/CURRENT_STATE.json',state)

    def test_real_readiness_is_only_visual_work_and_three_scene_flags(self):
        b=manage.blockers(self.root)
        self.assertEqual(len(b),4)
        self.assertIn('W04',b[0])

    def test_blocked_cli_returns_two(self):
        run=self.ready_cli()
        self.assertEqual(run.returncode,2,run.stdout+run.stderr)
        self.assertIn('NOT READY',run.stdout)

    def test_synthetic_fully_resolved_cli_returns_zero(self):
        self.synthetic_reviewed_fixture()
        self.assertEqual(manage.blockers(self.root),[])
        run=self.ready_cli()
        self.assertEqual(run.returncode,0,run.stdout+run.stderr)
        self.assertIn('READY',run.stdout)

    def test_positive_fixture_does_not_change_actual_project(self):
        self.synthetic_reviewed_fixture()
        self.assertTrue(manage.blockers(manage.ROOT))
        self.assertFalse(manage.read(manage.ROOT,'state/CURRENT_STATE.json')['coverage']['donghua_scenes_verified'])

    def test_fake_visual_closure_is_invalid_not_ready(self):
        self.change('state/CURRENT_STATE.json',lambda x:x['work'][3].update(status='resolved',closure_evidence=['D01']))
        self.assert_caught('visual work closure needs all scene gates')
        self.assertEqual(self.ready_cli().returncode,1)

    def test_null_fields_cannot_hide_under_resolved_work(self):
        self.change('state/CURRENT_STATE.json',lambda x:x['opening_state'].update(reserves=None))
        self.assert_caught('closure needs complete opening fields')

    def test_delegated_build_cannot_become_invented_author_lock(self):
        self.change('state/CURRENT_STATE.json',lambda x:x['opening_state_authority'].update(classification='author-lock'))
        self.assert_caught('design authority must be explicit')

    def test_original_design_cannot_become_external_primary(self):
        self.change('canon/SOURCE_RECEIPTS.json',lambda x:next(s for s in x['sources'] if s['id']=='DESIGN01').update(status='primary-read',scene_reviewed=True))
        self.assert_caught('cannot masquerade as external primary')

    def test_missing_delegation_is_caught(self):
        self.change('state/CURRENT_STATE.json',lambda x:x['opening_state_authority'].update(ruling_refs=['R01']))
        self.assert_caught('needs current delegation')

    def test_support_file_must_have_substance(self):
        (self.root/'power/DEVELOPMENT.md').write_text('# Thin fixture')
        self.assert_caught('missing substantive preflight support')

    def test_butterfly_assessment_cannot_be_missing(self):
        (self.root/'plot/CONTINUITY.md').unlink()
        self.assert_caught('butterfly closure needs substantive')

    def test_whole_checkpoint_cannot_drift(self):
        self.change_event(lambda e:None)
        self.change('state/development_events.json',lambda x:next(e for e in x['events'] if e['id']=='D09')['state_outputs'].update(physique={'description':'different fixture'}))
        self.assert_caught('checkpoint must match the whole')

    def test_prenatal_history_cannot_disappear(self):
        self.change('state/development_events.json',lambda x:x['events'].pop(0))
        self.assert_caught('must include prenatal foundation')

    def test_months_cannot_run_backward(self):
        self.change_event(lambda e:e.update(age_months_grid=90))
        self.assert_caught('month grid must increase')

    def test_exact_age_must_match_grid(self):
        self.change('state/CURRENT_STATE.json',lambda x:x['opening_state'].update(exact_age=12))
        self.assert_caught('age must match the authored month grid')

    def test_causal_field_cannot_be_empty(self):
        self.change_event(lambda e:e.update(resources=''))
        self.assert_caught('causal field cannot be empty: resources')

    def test_development_needs_original_provenance(self):
        self.change_event(lambda e:e.update(source_refs=['AT01']))
        self.assert_caught('requires explicit original-design provenance')

    def test_ring_color_cannot_disagree_with_age(self):
        self.change_ring(lambda r:r.update(color='black'))
        self.assert_caught('ring age and color mismatch')

    def test_ring_age_is_not_calendar_aging(self):
        self.change_ring(lambda r:r.update(current_age=r['current_age']+5))
        self.assert_caught('earned aging mechanism')

    def test_original_donor_is_not_canon_species(self):
        self.change_ring(lambda r:r.update(canonical_species_claim=True))
        self.assert_caught('donor provenance cannot be promoted to canon')

    def test_original_donor_needs_real_acquisition_support(self):
        self.change_ring(lambda r:r.update(support=''))
        self.assert_caught('ring history is missing support')

    def test_ring_slots_cannot_skip(self):
        self.change_ring(lambda r:r.update(slot=2))
        self.assert_caught('ring slots must be contiguous')

    def test_ring_ids_cannot_duplicate(self):
        self.change('state/CURRENT_STATE.json',lambda x:x['opening_state']['phoenix_rings'][1].update(id='P1'))
        self.assert_caught('ring IDs must not duplicate')

    def test_soul_king_needs_completed_fifth_breakthrough(self):
        self.change('state/CURRENT_STATE.json',lambda x:x['opening_state']['phoenix_rings'].pop())
        self.assert_caught('needs its completed breakthrough ring')

    def test_ring_cannot_be_acquired_in_future(self):
        self.change_ring(lambda r:r.update(acquired_age_months=999))
        self.assert_caught('cannot be acquired after the opening')

    def test_ring_gift_scope_is_required(self):
        self.change_ring(lambda r:r['skill'].update(scope=''))
        self.assert_caught('gift needs explicit original effect and scope')

    def test_engineering_needs_actual_work(self):
        self.change('state/CURRENT_STATE.json',lambda x:x['opening_state'].update(engineering_proficiency={}))
        self.assert_caught('engineering closure needs actual work')

    def test_certificate_needs_primary_exam_not_cultivation(self):
        self.change('state/CURRENT_STATE.json',lambda x:x['opening_state']['engineering_certification'].update(external_certificate=True,exam_source_refs=['A01']))
        self.assert_caught('requires primary exam evidence')

    def test_partial_certification_lead_stays_partial(self):
        a=next(x for x in manage.read(self.root,'canon/SOURCE_RECEIPTS.json')['sources'] if x['id']=='A01')
        self.assertEqual(a['status'],'partial-primary')
        self.assertFalse(a['scene_reviewed'])

    def test_equipment_needs_actual_owner(self):
        self.change('state/CURRENT_STATE.json',lambda x:x['opening_state']['equipment'][0].update(owner=''))
        self.assert_caught('equipment needs identity, ownership')

    def test_logistics_cannot_be_closed_without_witnesses(self):
        self.change('state/CURRENT_STATE.json',lambda x:x['relationships'].update(exact_witnesses=[]))
        self.assert_caught('logistics closure needs witnesses')

    def test_aging_cannot_reference_an_invented_event(self):
        self.change_ring(lambda r:r.update(current_age=1505,age_change_event_ids=['NONEXISTENT']))
        self.assert_caught('ring aging needs an actual matching adaptation output')

    def test_acquisition_date_needs_actual_development_milestone(self):
        self.change_ring(lambda r:r.update(acquired_age_months=74))
        self.assert_caught('ring acquisition needs a matching dated development event')

    def test_generated_opening_build_is_not_second_owner(self):
        (self.root/'OPENING_BUILD.md').write_text('Different fixture numbers')
        self.assertIn('generated opening build drift',manage.validate(self.root))


# Avoid unittest discovering Base's inherited tests in this module a second time.
del Base

if __name__=='__main__':
    unittest.main()
