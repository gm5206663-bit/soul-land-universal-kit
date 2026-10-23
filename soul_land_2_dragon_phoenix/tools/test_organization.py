"""Layout and owner regressions; not a substitute for reading the content."""
import unittest
from test_foundation import FoundationTests as Base
import manage


class OrganizationTests(unittest.TestCase):
    setUp=Base.setUp
    change=Base.change
    assert_caught=Base.assert_caught

    def test_old_flat_layout_cannot_return(self):
        (self.root/'foundation').mkdir()
        self.assert_caught('superseded flat layout must not return')

    def test_live_subject_is_not_listed_as_two_owners(self):
        def mutate(x):
            section=x['reading_sections'][0]
            section['documents'].append(section['documents'][0].copy())
        self.change('operations/FILE_REQUIREMENTS.json',mutate)
        self.assert_caught('must not duplicate live subject owners')

    def test_navigation_requires_explanation_not_only_a_filename(self):
        self.change('operations/FILE_REQUIREMENTS.json',lambda x:x['reading_sections'][0]['documents'][0].update(purpose=''))
        self.assert_caught('meaningful labels and responsibilities')

    def test_reader_guide_cannot_point_nowhere(self):
        self.change('operations/FILE_REQUIREMENTS.json',lambda x:x['reading_sections'][0]['documents'][0].update(path='story/missing.md'))
        self.assert_caught('reading guide target is missing')

    def test_every_function_needs_a_visible_owner(self):
        self.change('operations/FILE_REQUIREMENTS.json',lambda x:x['reading_sections'][0]['documents'].pop(0))
        self.assert_caught('functional coverage lacks a clear subject owner')

    def test_consolidation_is_not_a_bundle_of_pasted_documents(self):
        with (self.root/'story/CORE.md').open('a') as f:
            f.write('\n# Second unrelated document fixture\n')
        self.assert_caught('one main title, not pasted old documents')

    def test_latest_author_organization_correction_is_recorded(self):
        r=next(x for x in manage.read(self.root,'operations/AUTHOR_RULINGS.json')['rulings'] if x['id']=='R18')
        self.assertEqual(r['provenance_kind'],'verbatim-author-message')
        self.assertIn('clear and clean and systematic and organized',r['verbatim'])

    def test_historical_migration_is_not_a_power_retcon(self):
        receipt=manage.read(self.root,'records/organization/2026-10-23.json')
        self.assertTrue(receipt['story_decisions_preserved'])
        self.assertEqual(receipt['before_story_sha256'],receipt['after_story_sha256'])
        self.assertTrue(receipt['source_flags_preserved'])


del Base

if __name__=='__main__':
    unittest.main()
