import sys
import os
import yaml
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from configuration import load_search_config
import search_jobs


class SearchConfigurationTests(unittest.TestCase):
    def write(self, text):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        path = Path(folder.name) / 'settings.yaml'
        path.write_text(text)
        return path

    def test_loads_user_parameters_without_career_access(self):
        path = self.write('''search:
  keywords: [engineer]
  location: Cork, Ireland
  sites: [indeed]
  hours_old: 12
  results_wanted: 20
  country_indeed: Ireland
  linkedin_fetch_description: false
''')
        settings = load_search_config(path)
        with patch.object(search_jobs, 'scrape_jobs') as scrape:
            search_jobs.search_keyword('engineer', settings)
        self.assertEqual(scrape.call_args.kwargs, dict(
            site_name=['indeed'], search_term='engineer', location='Cork, Ireland',
            hours_old=12, results_wanted=20, country_indeed='Ireland',
            linkedin_fetch_description=False, verbose=0))

    def test_invalid_parameters_fail_before_search(self):
        for entry in ['keywords: []', 'keywords: engineer', 'hours_old: -1',
                      'results_wanted: true', 'sites: linkedin', 'location: 42',
                      'linkedin_fetch_description: yesplease']:
            with self.subTest(entry=entry):
                settings = dict(keywords=['engineer'], location='Cork, Ireland',
                                sites=['indeed'], hours_old=12, results_wanted=20,
                                country_indeed='Ireland', linkedin_fetch_description=False)
                settings.update(yaml.safe_load(entry))
                path = self.write(yaml.safe_dump({'search': settings}))
                with self.assertRaises(ValueError):
                    load_search_config(path)

    def test_missing_config_explains_setup(self):
        with self.assertRaisesRegex(FileNotFoundError, 'config.example.yaml'):
            load_search_config(Path('/nonexistent/job-monitor-settings.yaml'))

    def test_default_config_path_does_not_depend_on_working_directory(self):
        path = self.write("search: {}")
        previous = Path.cwd()
        self.addCleanup(os.chdir, previous)
        os.chdir(path.parent)
        import configuration
        self.assertEqual(configuration.CONFIG_PATH,
                         Path(__file__).resolve().parents[1] / 'config/config.local.yaml')
        with patch.object(configuration, 'CONFIG_PATH', path):
            with self.assertRaisesRegex(ValueError, 'missing search.keywords'):
                load_search_config()

    def test_empty_or_wrong_shape_is_rejected(self):
        for text in ['', '[]', 'search: []', 'career: {}']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                load_search_config(self.write(text))


if __name__ == '__main__':
    unittest.main()
