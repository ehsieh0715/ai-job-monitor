import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock
import yaml
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from configuration import load_sheets_config
import google_sheets


class GoogleConfigurationTests(unittest.TestCase):
    def test_url_id_and_legacy_name_route(self):
        for target, name, method in [('https://docs.google.com/spreadsheets/d/example/edit','','open_by_url'),('example','','open_by_key'),('','Old Sheet','open')]:
            with self.subTest(target=target):
                client = MagicMock()
                cfg = dict(spreadsheet=target,spreadsheet_name=name,worksheet='My Jobs',credentials_path='/private/example.json')
                with patch.object(google_sheets,'load_sheets_config',return_value=cfg), patch.object(google_sheets.gspread,'service_account',return_value=client):
                    google_sheets.get_worksheet()
                getattr(client,method).assert_called_once_with(target or name)
                getattr(client,method).return_value.worksheet.assert_called_once_with('My Jobs')

    def test_load_and_missing_credentials(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); credentials = root/'private.json'; credentials.write_text('{}')
            path = root/'settings.yaml'
            cfg = {'google_sheets': {'spreadsheet':'example', 'worksheet':'Jobs', 'credentials_path':str(credentials)}}
            path.write_text(yaml.safe_dump(cfg))
            self.assertEqual(load_sheets_config(path)['credentials_path'], str(credentials))
            credentials.unlink()
            with self.assertRaises(FileNotFoundError): load_sheets_config(path)
