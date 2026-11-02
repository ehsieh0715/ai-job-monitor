"""Read private search settings independently of the current directory."""
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / 'config' / 'config.local.yaml'


def load_search_config(path=None):
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
