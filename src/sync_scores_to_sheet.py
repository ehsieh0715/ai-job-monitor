import json
from pathlib import Path

import subprocess
import pandas as pd

from google_sheets import (
    get_existing_job_ids,
    get_worksheet,
)
from schema import (
    PENDING_COLUMNS,
    SCORED_COLUMNS,
)


SCORED_JOBS_PATH = Path(
    "data/scored_jobs.csv"
)

PENDING_JOBS_PATH = Path(
    "data/pending_jobs.csv"
)

PROCESSED_IDS_PATH = Path(
    "data/processed_job_ids.json"
)


def clean_value(value):
    if value is None:
        return ""

    try:
        if pd.isna(value):
            return ""
    except (TypeError, ValueError):
        pass

    return value


def load_processed_ids():
    if not PROCESSED_IDS_PATH.exists():
        return set()

    with open(
        PROCESSED_IDS_PATH,
        "r",
        encoding="utf-8",
    ) as file:
        return set(json.load(file))


def save_processed_ids(processed_ids):
    with open(
        PROCESSED_IDS_PATH,
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            sorted(processed_ids),
            file,
            indent=2,
        )


def ensure_header(worksheet):
    current_header = worksheet.row_values(1)

    if current_header == SCORED_COLUMNS:
        return

    worksheet.update(
        range_name="A1:K1",
        values=[SCORED_COLUMNS],
    )


def remove_processed_from_pending(
    processed_job_ids,
):
    if not PENDING_JOBS_PATH.exists():
        return

    pending = pd.read_csv(
        PENDING_JOBS_PATH
    )

    if pending.empty:
        return

    pending = pending[
        ~pending["job_id"].astype(str).isin(
            processed_job_ids
        )
    ]

    pending = pending[
        [
            column
            for column in PENDING_COLUMNS
            if column in pending.columns
        ]
    ]

    pending.to_csv(
        PENDING_JOBS_PATH,
        index=False,
    )


def sync_scores():
    if not SCORED_JOBS_PATH.exists():
        print(
            "data/scored_jobs.csv "
            "does not exist."
        )
        return

    scored_jobs = pd.read_csv(
        SCORED_JOBS_PATH
    )

    if scored_jobs.empty:
        print("No scored jobs to sync.")
        return

    missing_columns = [
        column
        for column in SCORED_COLUMNS
        if column not in scored_jobs.columns
    ]

    if missing_columns:
        raise ValueError(
            "Missing columns in scored_jobs.csv: "
            + ", ".join(missing_columns)
        )

    worksheet = get_worksheet()

    ensure_header(worksheet)

    existing_sheet_ids = (
        get_existing_job_ids(worksheet)
    )

    processed_ids = load_processed_ids()

    jobs_to_upload = scored_jobs[
        ~scored_jobs["job_id"]
        .astype(str)
        .isin(existing_sheet_ids)
    ].copy()

    if jobs_to_upload.empty:
        print(
            "All scored jobs already exist "
            "in Google Sheet."
        )

        processed_ids.update(
            scored_jobs["job_id"]
            .astype(str)
            .tolist()
        )

        save_processed_ids(
            processed_ids
        )

        remove_processed_from_pending(
            set(
                scored_jobs["job_id"]
                .astype(str)
                .tolist()
            )
        )

        return

    rows = []

    for _, job in jobs_to_upload.iterrows():
        row = [
            clean_value(
                job.get(column)
            )
            for column in SCORED_COLUMNS
        ]

        rows.append(row)

    worksheet.append_rows(
        rows,
        value_input_option="USER_ENTERED",
    )

    uploaded_ids = set(
        jobs_to_upload["job_id"]
        .astype(str)
        .tolist()
    )

    processed_ids.update(
        uploaded_ids
    )

    save_processed_ids(
        processed_ids
    )

    remove_processed_from_pending(
        uploaded_ids
    )

    print(
        f"Uploaded {len(rows)} scored jobs "
        "to Google Sheet."
    )


def send_mac_notification(job):
    recommendation = str(
        job.get("recommendation", "")
    )

    if recommendation not in {
        "Apply",
        "Strong Apply",
    }:
        return

    title = str(job.get("title", ""))
    company = str(job.get("company", ""))
    score = str(job.get("match_score", ""))

    message = (
        f"{title} — {company}\\n"
        f"Match Score: {score}"
    )

    script = (
        f'display notification "{message}" '
        f'with title "AI Job Monitor" '
        f'subtitle "{recommendation}"'
    )

    subprocess.run(
        ["osascript", "-e", script],
        check=False,
    )


if __name__ == "__main__":
    sync_scores()
