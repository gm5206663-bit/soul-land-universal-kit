#!/usr/bin/env python3
"""Offline tests for the distinction between findings and incomplete execution."""
import json
from pathlib import Path
import tempfile
import unittest
import sweep_evidence as evidence


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.prefix = str(Path(self.temp.name) / 'sweep')

    def gate(self, text, code):
        path = self.prefix + '-gate.txt'
        Path(path).write_text(text)
        evidence.validate_gate(path, code)

    def report(self, hard=1):
        report = {'tool': 'account-control-centre', 'books': [{}], 'facts': [{}],
                  'coverage': [{'detector': d} for d in ('gate', 'dupes', 'two-homes',
                      'receipts', 'publication', 'housekeeping', 'links', 'generated',
                      'enforcement', 'stale-claims', 'sightings')],
                  'summary': {'hard': hard},
                  'findings': [{'severity': 'hard'}] * hard}
        self.save(report)
        return report

    def save(self, report):
        Path(self.prefix + '.json').write_text(json.dumps(report))
        for ext in ('.md', '.html'):
            Path(self.prefix + ext).write_text('report')

    def test_gate_clean(self):
        self.gate('COVERAGE: 1 book\nPASS\n', 0)

    def test_gate_findings(self):
        self.gate('COVERAGE: 1 book\nFAIL\n', 1)

    def test_gate_traceback_not_findings(self):
        with self.assertRaises(ValueError):
            self.gate('Traceback: checker crashed\n', 1)

    def test_gate_code_mismatch(self):
        with self.assertRaises(ValueError):
            self.gate('COVERAGE: 1 book\nFAIL\n', 0)

    def test_gate_missing_coverage(self):
        with self.assertRaises(ValueError):
            self.gate('PASS\n', 0)

    def test_report_findings(self):
        self.report()
        evidence.validate_report(self.prefix, 1)

    def test_report_clean(self):
        self.report(0)
        evidence.validate_report(self.prefix, 0)

    def test_report_crash_code(self):
        self.report()
        with self.assertRaises(ValueError):
            evidence.validate_report(self.prefix, 2)

    def test_missing_artifact(self):
        self.report()
        Path(self.prefix + '.html').unlink()
        with self.assertRaises(ValueError):
            evidence.validate_report(self.prefix, 1)

    def test_partial_coverage(self):
        report = self.report(); report['coverage'].pop(); self.save(report)
        with self.assertRaises(ValueError):
            evidence.validate_report(self.prefix, 1)

    def test_empty_scope(self):
        report = self.report(); report['facts'] = []; self.save(report)
        with self.assertRaises(ValueError):
            evidence.validate_report(self.prefix, 1)

    def test_inconsistent_summary(self):
        report = self.report(); report['summary']['hard'] = 0; self.save(report)
        with self.assertRaises(ValueError):
            evidence.validate_report(self.prefix, 1)


if __name__ == '__main__':
    unittest.main()
