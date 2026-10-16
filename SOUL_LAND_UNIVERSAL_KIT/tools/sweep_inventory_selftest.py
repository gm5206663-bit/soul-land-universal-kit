#!/usr/bin/env python3
"""Offline regression tests: public discovery must never shrink silently."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import Mock
import sweep_inventory as inventory


def repo(name='alpha', **extra):
    return dict(name=name, owner={'login': 'owner'}, private=False, archived=False, **extra)


class InventoryTests(unittest.TestCase):
    def test_pagination(self):
        fetch = Mock(side_effect=[[repo(f'r{i}') for i in range(100)], [repo('last')]])
        self.assertEqual(len(inventory.discover('owner', fetch)), 101)
        self.assertIn('page=2', fetch.call_args.args[0])

    def test_empty_refused(self):
        with self.assertRaises(ValueError):
            inventory.discover('owner', lambda url: [])

    def test_error_object_refused(self):
        with self.assertRaises(ValueError):
            inventory.discover('owner', lambda url: {'message': 'rate limited'})

    def test_wrong_owner_refused(self):
        with self.assertRaises(ValueError):
            inventory.discover('other', lambda url: [repo()])

    def test_private_refused(self):
        item = repo(); item['private'] = True
        with self.assertRaises(ValueError):
            inventory.discover('owner', lambda url: [item])

    def test_unsafe_name_refused(self):
        with self.assertRaises(ValueError):
            inventory.discover('owner', lambda url: [repo('../outside')])

    def test_duplicate_refused(self):
        with self.assertRaises(ValueError):
            inventory.discover('owner', lambda url: [repo(), repo()])

    def test_invalid_owner_refused(self):
        with self.assertRaises(ValueError):
            inventory.discover('../owner', Mock())

    def test_archived_retained(self):
        item = repo(); item['archived'] = True
        self.assertTrue(inventory.discover('owner', lambda url: [item])[0]['archived'])

    def test_clone_receipt(self):
        with tempfile.TemporaryDirectory() as temp:
            receipt = Path(temp) / 'receipt.json'
            run = Mock(return_value=subprocess.CompletedProcess([], 0, stdout='a' * 40 + '\n'))
            inventory.clone_all('owner', [repo()], Path(temp) / 'clones', receipt, run)
            data = json.loads(receipt.read_text())
            self.assertEqual(data[0]['head'], 'a' * 40)
            self.assertEqual(data[0]['status'], 'cloned')

    def test_clone_failure_is_fatal_and_recorded(self):
        with tempfile.TemporaryDirectory() as temp:
            receipt = Path(temp) / 'receipt.json'
            run = Mock(side_effect=subprocess.CalledProcessError(128, ['git']))
            with self.assertRaises(RuntimeError):
                inventory.clone_all('owner', [repo()], Path(temp) / 'clones', receipt, run)
            self.assertEqual(json.loads(receipt.read_text())[0]['status'], 'failed')

    def test_existing_destination_refused(self):
        with tempfile.TemporaryDirectory() as temp:
            (Path(temp) / 'alpha').mkdir()
            run = Mock()
            with self.assertRaises(RuntimeError):
                inventory.clone_all('owner', [repo()], temp, Path(temp) / 'receipt.json', run)
            run.assert_not_called()

    def test_invalid_head_refused(self):
        with tempfile.TemporaryDirectory() as temp:
            run = Mock(return_value=subprocess.CompletedProcess([], 0, stdout=''))
            with self.assertRaises(RuntimeError):
                inventory.clone_all('owner', [repo()], Path(temp) / 'clones', Path(temp) / 'receipt.json', run)

    def test_later_repos_attempted_after_failure(self):
        with tempfile.TemporaryDirectory() as temp:
            run = Mock(side_effect=[subprocess.CalledProcessError(128, ['git']),
                                   subprocess.CompletedProcess([], 0),
                                   subprocess.CompletedProcess([], 0, stdout='b' * 40)])
            receipt = Path(temp) / 'receipt.json'
            with self.assertRaises(RuntimeError):
                inventory.clone_all('owner', [repo('alpha'), repo('beta')], Path(temp) / 'clones', receipt, run)
            self.assertEqual([r['status'] for r in json.loads(receipt.read_text())], ['failed', 'cloned'])


if __name__ == '__main__':
    unittest.main()
