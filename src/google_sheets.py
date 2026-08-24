from pathlib import Path

import gspread


CREDENTIALS_PATH = Path(
    "google-service-account.json"
)

SPREADSHEET_NAME = "AI Job Monitor"
WORKSHEET_NAME = "Jobs"


def get_worksheet():
    client = gspread.service_account(
        filename=str(CREDENTIALS_PATH)
    )

    spreadsheet = client.open(
        SPREADSHEET_NAME
    )

    return spreadsheet.worksheet(
        WORKSHEET_NAME
    )


def get_existing_job_ids(worksheet):
    records = worksheet.get_all_records()

    return {
        str(record["job_id"])
        for record in records
        if record.get("job_id")
    }