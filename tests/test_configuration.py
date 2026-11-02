"""Configuration boundaries for Career data, search and Google Sheets."""
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import configuration
import google_sheets
import prepare_evaluation
import search_jobs
from configuration import load_search_config, load_sheets_config


def scoring_files(root):
    directory = root / 'policies'
    directory.mkdir(exist_ok=True)
    for name in ['candidate-evidence-standards.md', 'job-fit-evaluation.md']:
        (directory / name).write_text('Initial scoring rule')


class CareerLayoutTests(unittest.TestCase):

    def test_root_alone_resolves_fixed_layout_without_creating_files(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / 'career'
            with patch.object(configuration, 'load_config', return_value={'career': {'root': str(root)}}):
                paths = configuration.load_career_paths()
            self.assertEqual(paths, {'root': root, 'profile': root / 'Candidate Profile.md', 'source_documents': root / 'Source Documents', 'projects': root / 'Source Documents' / 'Projects.md', 'applications': root / 'applications', 'application_tracker': root / 'applications.md'})
            self.assertFalse(root.exists())

    def test_invalid_root_rejected(self):
        for career in [None, {}, {'root': ''}, {'root': 'relative'}, {'root': 42}]:
            with self.subTest(career=career), patch.object(configuration, 'load_config', return_value={'career': career}):
                with self.assertRaisesRegex(ValueError, 'career.root'):
                    configuration.load_career_paths()

    def test_old_path_overrides_cannot_redirect_reads(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            scoring_files(root)
            config = {'career': {'root': str(root), 'profile': '/unrelated/profile.md', 'project_evidence': '/unrelated/evidence'}}
            (root / 'Candidate Profile.md').write_text('verified SQL')
            with patch.object(prepare_evaluation, 'load_config', return_value=config):
                first = prepare_evaluation.fingerprint()
                evidence = root / 'Project Evidence'
                evidence.mkdir()
                (evidence / 'legacy.md').write_text('unapproved legacy claims')
                self.assertEqual(prepare_evaluation.fingerprint(), first)
                (root / 'Candidate Profile.md').write_text('verified Python')
                self.assertNotEqual(prepare_evaluation.fingerprint(), first)

    def test_presentation_preferences_do_not_affect_scoring_freshness(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            scoring_files(root)
            (root / 'Candidate Profile.md').write_text('verified SQL')
            policies = root / 'policies'
            policies.mkdir(exist_ok=True)
            config = {'career': {'root': str(root)}}
            with patch.object(prepare_evaluation, 'REPO_ROOT', root), patch.object(prepare_evaluation, 'load_config', return_value=config):
                no_preferences = prepare_evaluation.fingerprint()
                note = policies / 'preferences.md'
                note.write_text('Analysis language: Traditional Chinese')
                first = prepare_evaluation.fingerprint()
                self.assertEqual(first, no_preferences)
                note.write_text('Analysis language: English')
                self.assertEqual(prepare_evaluation.fingerprint(), first)
                note.unlink()
                self.assertEqual(prepare_evaluation.fingerprint(), no_preferences)


class GoogleConfigurationTests(unittest.TestCase):

    def test_url_id_and_legacy_name_route(self):
        for target, name, method in [('https://docs.google.com/spreadsheets/d/example/edit', '', 'open_by_url'), ('example', '', 'open_by_key'), ('', 'Old Sheet', 'open')]:
            with self.subTest(target=target):
                client = MagicMock()
                cfg = dict(spreadsheet=target, spreadsheet_name=name, worksheet='My Jobs', credentials_path='/private/example.json')
                with patch.object(google_sheets, 'load_sheets_config', return_value=cfg), patch.object(google_sheets.gspread, 'service_account', return_value=client):
                    google_sheets.get_worksheet()
                getattr(client, method).assert_called_once_with(target or name)
                getattr(client, method).return_value.worksheet.assert_called_once_with('My Jobs')

    def test_load_and_missing_credentials(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            credentials = root / 'google-service-account.json'
            credentials.write_text('{}')
            path = root / 'settings.yaml'
            cfg = {'google_sheets': {'spreadsheet': 'example', 'worksheet': 'Jobs'}}
            path.write_text(yaml.safe_dump(cfg))
            with patch('configuration.REPO_ROOT', root):
                self.assertEqual(load_sheets_config(path)['credentials_path'], str(credentials))
                cfg['google_sheets']['credentials_path'] = '/unrelated/secret.json'
                path.write_text(yaml.safe_dump(cfg))
                self.assertEqual(load_sheets_config(path)['credentials_path'], str(credentials))
                credentials.unlink()
                with self.assertRaisesRegex(FileNotFoundError, 'google-service-account.json'):
                    load_sheets_config(path)


class SearchConfigurationTests(unittest.TestCase):

    def write(self, text):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        path = Path(folder.name) / 'settings.yaml'
        path.write_text(text)
        return path

    def test_loads_user_parameters_without_career_access(self):
        path = self.write('search:\n  keywords: [engineer]\n  location: Cork, Ireland\n  sites: [indeed]\n  hours_old: 12\n  results_wanted: 20\n  country_indeed: Ireland\n  linkedin_fetch_description: false\n')
        settings = load_search_config(path)
        with patch.object(search_jobs, 'scrape_jobs') as scrape:
            search_jobs.search_keyword('engineer', settings)
        self.assertEqual(scrape.call_args.kwargs, dict(site_name=['indeed'], search_term='engineer', location='Cork, Ireland', hours_old=12, results_wanted=20, country_indeed='Ireland', linkedin_fetch_description=False, verbose=0))

    def test_invalid_parameters_fail_before_search(self):
        for entry in ['keywords: []', 'keywords: engineer', 'hours_old: -1', 'results_wanted: true', 'sites: linkedin', 'location: 42', 'linkedin_fetch_description: yesplease']:
            with self.subTest(entry=entry):
                settings = dict(keywords=['engineer'], location='Cork, Ireland', sites=['indeed'], hours_old=12, results_wanted=20, country_indeed='Ireland', linkedin_fetch_description=False)
                settings.update(yaml.safe_load(entry))
                path = self.write(yaml.safe_dump({'search': settings}))
                with self.assertRaises(ValueError):
                    load_search_config(path)

    def test_missing_config_explains_setup(self):
        with self.assertRaisesRegex(FileNotFoundError, 'config.example.yaml'):
            load_search_config(Path('/nonexistent/job-monitor-settings.yaml'))

    def test_default_config_path_does_not_depend_on_working_directory(self):
        path = self.write('search: {}')
        previous = Path.cwd()
        self.addCleanup(os.chdir, previous)
        os.chdir(path.parent)
        import configuration
        self.assertEqual(configuration.CONFIG_PATH, Path(__file__).resolve().parents[1] / 'config/config.local.yaml')
        with patch.object(configuration, 'CONFIG_PATH', path):
            with self.assertRaisesRegex(ValueError, 'missing search.keywords'):
                load_search_config()

    def test_empty_or_wrong_shape_is_rejected(self):
        for text in ['', '[]', 'search: []', 'career: {}']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                load_search_config(self.write(text))
