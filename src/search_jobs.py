import json
from datetime import datetime

import pandas as pd
from jobspy import scrape_jobs

from schema import PENDING_COLUMNS, RAW_JOB_COLUMNS
from configuration import load_search_config, REPO_ROOT


RAW_JOBS_PATH = REPO_ROOT / "data/raw_jobs.csv"
PENDING_JOBS_PATH = REPO_ROOT / "data/pending_jobs.csv"
PROCESSED_IDS_PATH = REPO_ROOT / "data/processed_job_ids.json"


def search_keyword(keyword, settings=None):
    settings = load_search_config() if settings is None else settings
    print(f"Searching: {keyword}")
    return scrape_jobs(
        site_name=settings["sites"],
        search_term=keyword,
        location=settings["location"],
        results_wanted=settings["results_wanted"],
        hours_old=settings["hours_old"],
        country_indeed=settings["country_indeed"],
        linkedin_fetch_description=settings["linkedin_fetch_description"],
        verbose=0,
    )


def make_job_id(row):
    return f"{row['site']}:{row['id']}"


def load_processed_ids():
    if not PROCESSED_IDS_PATH.exists():
        return set()

    with open(
        PROCESSED_IDS_PATH,
        "r",
        encoding="utf-8",
    ) as file:
        return set(json.load(file))


def load_pending_jobs():
    if not PENDING_JOBS_PATH.exists():
        return pd.DataFrame(
            columns=PENDING_COLUMNS
        )

    return pd.read_csv(PENDING_JOBS_PATH)


def search_jobs():
    results = []

    settings = load_search_config()
    for keyword in settings["keywords"]:
        jobs = search_keyword(keyword, settings)

        if jobs.empty:
            continue

        jobs["search_term"] = keyword

        results.append(jobs)

    if not results:
        return pd.DataFrame(
            columns=RAW_JOB_COLUMNS
        )

    jobs = pd.concat(
        results,
        ignore_index=True,
    )

    available_columns = [
        column
        for column in RAW_JOB_COLUMNS
        if column in jobs.columns
    ]

    jobs = jobs[available_columns]

    # Same job may appear under multiple search terms.
    jobs = jobs.drop_duplicates(
        subset=["site", "id"],
        keep="first",
    )

    return jobs


def update_pending_jobs(jobs):
    if jobs.empty:
        print("No jobs returned from search.")
        return

    jobs = jobs.copy()

    jobs["job_id"] = jobs.apply(
        make_job_id,
        axis=1,
    )

    pending_jobs = load_pending_jobs()
    processed_ids = load_processed_ids()

    pending_ids = set(
        pending_jobs["job_id"]
        .dropna()
        .astype(str)
    )

    known_ids = (
        processed_ids
        | pending_ids
    )

    new_jobs = jobs[
        ~jobs["job_id"].isin(known_ids)
    ].copy()

    if new_jobs.empty:
        print("No new jobs found.")
        return

    new_jobs["found_at"] = (
        datetime.now()
        .strftime("%Y-%m-%d %H:%M:%S")
    )

    new_jobs = new_jobs[
        PENDING_COLUMNS
    ]

    updated_pending = pd.concat(
        [
            pending_jobs,
            new_jobs,
        ],
        ignore_index=True,
    )

    updated_pending.to_csv(
        PENDING_JOBS_PATH,
        index=False,
    )

    print(
        f"Added {len(new_jobs)} new jobs "
        f"to {PENDING_JOBS_PATH}"
    )


def run_search():
    jobs = search_jobs()

    print(
        f"\nFound {len(jobs)} "
        "unique jobs."
    )

    RAW_JOBS_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    jobs.to_csv(
        RAW_JOBS_PATH,
        index=False,
    )

    print(
        f"Saved current search results "
        f"to {RAW_JOBS_PATH}"
    )

    update_pending_jobs(jobs)

    return jobs


if __name__ == "__main__":
    run_search()