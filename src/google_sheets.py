"""Connect to the user's configured spreadsheet without printing credentials."""
import gspread
from configuration import load_sheets_config


def get_worksheet():
    settings = load_sheets_config()
    client = gspread.service_account(filename=settings['credentials_path'])
    target = settings['spreadsheet']
    if target.startswith('https://docs.google.com/spreadsheets/'):
        spreadsheet = client.open_by_url(target)
    elif target:
        spreadsheet = client.open_by_key(target)
    else:
        # Explicit legacy name support; URL/ID is preferred to avoid ambiguity.
        spreadsheet = client.open(settings['spreadsheet_name'])
    return spreadsheet.worksheet(settings['worksheet'])
