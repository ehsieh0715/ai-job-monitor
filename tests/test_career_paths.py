"""The repository, rather than user settings, owns the Career layout."""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import configuration
import prepare_evaluation


class CareerLayoutTests(unittest.TestCase):
    def test_root_alone_resolves_fixed_layout_without_creating_files(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / 'career'
            with patch.object(configuration, 'load_config', return_value={'career': {'root': str(root)}}):
                paths = configuration.load_career_paths()
            self.assertEqual(paths, {
                'root': root, 'profile': root / 'Candidate Profile.md',
                'source_documents': root / 'Source Documents',
                'projects': root / 'Source Documents' / 'Projects.md',
                'applications': root / 'applications',
                'application_tracker': root / 'applications.md',
            })
            self.assertFalse(root.exists())

    def test_invalid_root_rejected(self):
        for career in [None, {}, {'root': ''}, {'root': 'relative'}, {'root': 42}]:
            with self.subTest(career=career), patch.object(configuration, 'load_config', return_value={'career': career}):
                with self.assertRaisesRegex(ValueError, 'career.root'):
                    configuration.load_career_paths()

    def test_old_path_overrides_cannot_redirect_reads(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            config = {'career': {'root': str(root), 'profile': '/unrelated/profile.md',
                                'project_evidence': '/unrelated/evidence'}}
            (root / 'Candidate Profile.md').write_text('verified SQL')
            with patch.object(prepare_evaluation, 'load_config', return_value=config):
                first = prepare_evaluation.fingerprint()
                evidence = root / 'Project Evidence'; evidence.mkdir()
                (evidence / 'legacy.md').write_text('unapproved legacy claims')
                self.assertEqual(prepare_evaluation.fingerprint(), first)
                (root / 'Candidate Profile.md').write_text('verified Python')
                self.assertNotEqual(prepare_evaluation.fingerprint(), first)

    def test_retired_preference_setting_does_not_read_external_file(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'Candidate Profile.md').write_text('verified SQL')
            note = root / 'old-preferences.md'
            config = {'career': {'root': str(root)}, 'preferences_path': str(note)}
            with patch.object(prepare_evaluation, 'load_config', return_value=config):
                baseline = prepare_evaluation.fingerprint()
                note.write_text('English')
                self.assertEqual(prepare_evaluation.fingerprint(), baseline)

    def test_optional_fixed_preferences_participate_in_freshness(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'Candidate Profile.md').write_text('verified SQL')
            policies = root / 'policies'; policies.mkdir()
            config = {'career': {'root': str(root)}}
            with patch.object(prepare_evaluation, 'REPO_ROOT', root), patch.object(prepare_evaluation, 'load_config', return_value=config):
                no_preferences = prepare_evaluation.fingerprint()
                note = policies / 'preferences.md'
                note.write_text('Analysis language: Traditional Chinese')
                first = prepare_evaluation.fingerprint()
                self.assertNotEqual(first, no_preferences)
                note.write_text('Analysis language: English')
                self.assertNotEqual(prepare_evaluation.fingerprint(), first)
                note.unlink()
                self.assertEqual(prepare_evaluation.fingerprint(), no_preferences)
