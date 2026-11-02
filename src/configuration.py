"""Read private search settings independently of the current directory."""
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / 'config' / 'config.local.yaml'


def load_config(path=None):
    path = Path(path) if path is not None else CONFIG_PATH
    if not path.is_file():
        raise FileNotFoundError(
            f'Missing configuration: {path}. Copy config/config.example.yaml '
            'to config/config.local.yaml and edit your settings.'
        )
    try:
        config = yaml.safe_load(path.read_text(encoding='utf-8'))
    except yaml.YAMLError as exc:
        raise ValueError(f'Invalid YAML in {path}: {exc}') from exc
    if not isinstance(config, dict):
        raise ValueError(f"{path}: configuration must be a mapping")
    return config


def load_career_paths(path=None, *, config=None):
    """Resolve the repository-owned layout; legacy path overrides are ignored.

    Resolving paths never creates folders or approved candidate content.
    """
    config = load_config(path) if config is None else config
    career = config.get('career')
    value = career.get('root') if isinstance(career, dict) else None
    if not isinstance(value, str) or not value.strip():
        raise ValueError('Set career.root to an absolute Career folder path')
    root = Path(value).expanduser()
    if not root.is_absolute():
        raise ValueError('career.root must be absolute')
    return {
        'root': root,
        'profile': root / 'Candidate Profile.md',
        'source_documents': root / 'Source Documents',
        'projects': root / 'Source Documents' / 'Projects.md',
        'applications': root / 'applications',
        'application_tracker': root / 'applications.md',
    }


def load_search_config(path=None):
    config = load_config(path)
    if not isinstance(config, dict) or not isinstance(config.get('search'), dict):
        raise ValueError(f'{path}: search must be a mapping')
    search = config['search']
    required = ('keywords', 'location', 'sites', 'hours_old', 'results_wanted',
                'country_indeed', 'linkedin_fetch_description')
    for key in required:
        if key not in search:
            raise ValueError(f'{path}: missing search.{key}')
    for key in ('keywords', 'sites'):
        value = search[key]
        if not isinstance(value, list) or not value or any(
            not isinstance(item, str) or not item.strip() for item in value
        ):
            raise ValueError(f'{path}: search.{key} must be a non-empty list of strings')
    for key in ('location', 'country_indeed'):
        if not isinstance(search[key], str) or not search[key].strip():
            raise ValueError(f'{path}: search.{key} must be a non-empty string')
    for key in ('hours_old', 'results_wanted'):
        if type(search[key]) is not int or search[key] <= 0:
            raise ValueError(f'{path}: search.{key} must be a positive integer')
    if type(search['linkedin_fetch_description']) is not bool:
        raise ValueError(f'{path}: search.linkedin_fetch_description must be boolean')
    return {key: search[key] for key in required}


def load_sheets_config(path=None):
    config = load_config(path)
    sheets = config.get('google_sheets')
    if not isinstance(sheets, dict):
        raise ValueError('Configure google_sheets in config/config.local.yaml')
    for key in ('worksheet', 'credentials_path'):
        if not isinstance(sheets.get(key), str) or not sheets[key].strip():
            raise ValueError(f'Missing google_sheets.{key}')
    target = sheets.get('spreadsheet', '')
    name = sheets.get('spreadsheet_name', '')
    if not isinstance(target, str) or not isinstance(name, str) or not (target.strip() or name.strip()):
        raise ValueError('Set google_sheets.spreadsheet to a Sheet URL or ID')
    credentials = Path(sheets['credentials_path']).expanduser()
    if not credentials.is_absolute():
        credentials = REPO_ROOT / credentials
    if not credentials.is_file():
        raise FileNotFoundError(f'Missing Google credential file: {credentials}')
    return {**sheets, 'spreadsheet': target.strip(), 'credentials_path': str(credentials)}
