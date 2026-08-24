from datetime import date, datetime
from pathlib import Path

import gspread
import pandas as pd

from schema import SHEET_COLUMNS


CREDENTIALS_PATH = Path("google-service-account.json")
RAW_JOBS_PATH = Path("data/raw_jobs.csv")

SPREADSHEET_NAME = "AI Job Monitor"
WORKSHEET_NAME = "Jobs"


def get_worksheet():
    client = gspread.service_account(
        filename=str(CREDENTIALS_PATH)
    )

    spreadsheet = client.open(SPREADSHEET_NAME)

    return spreadsheet.worksheet(WORKSHEET_NAME)


def clean_value(value):
    if value is None:
        return ""

    try:
        if pd.isna(value):
            return ""
    except (TypeError, ValueError):
        pass

    if isinstance(value, (date, datetime)):
        return value.isoformat()

    return value


def make_job_id(job):
    site = clean_value(job.get("site"))
    job_id = clean_value(job.get("id"))

    return f"{site}:{job_id}"


def ensure_header(worksheet):
    first_row = worksheet.row_values(1)

    if first_row != SHEET_COLUMNS:
        end_column = chr(64 + len(SHEET_COLUMNS))

        worksheet.update(
            range_name=f"A1:{end_column}1",
            values=[SHEET_COLUMNS],
        )


def get_existing_job_ids(worksheet):
    records = worksheet.get_all_records()

    return {
        str(record["job_id"])
        for record in records
        if record.get("job_id")
    }


def get_new_jobs(jobs, existing_job_ids):
    new_jobs = []

    for _, job in jobs.iterrows():
        job_id = make_job_id(job)

        if job_id in existing_job_ids:
            continue

        new_jobs.append(job)

    return new_jobs


def write_jobs(jobs):
    worksheet = get_worksheet()

    ensure_header(worksheet)

    existing_job_ids = get_existing_job_ids(
        worksheet
    )

    new_jobs = get_new_jobs(
        jobs,
        existing_job_ids,
    )

    if not new_jobs:
        print("No new jobs to add.")
        return

    found_at = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    rows = []

    for job in new_jobs:
        row = [
            make_job_id(job),
            found_at,
            job.get("site"),
            job.get("title"),
            job.get("company"),
            job.get("location"),
            job.get("search_term"),
            job.get("job_url"),
            "",
            "",
            "",
        ]

        rows.append([
            clean_value(value)
            for value in row
        ])

    worksheet.append_rows(
        rows,
        value_input_option="USER_ENTERED",
    )

    print(
        f"Added {len(rows)} new jobs "
        "to Google Sheet."
    )


def load_raw_jobs():
    if not RAW_JOBS_PATH.exists():
        raise FileNotFoundError(
            f"{RAW_JOBS_PATH} does not exist. "
            "Run search_jobs.py first."
        )

    return pd.read_csv(RAW_JOBS_PATH)


if __name__ == "__main__":
    jobs = load_raw_jobs()

    print(f"Loaded {len(jobs)} jobs from {RAW_JOBS_PATH}")

    write_jobs(jobs)