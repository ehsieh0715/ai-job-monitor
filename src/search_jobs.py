from pathlib import Path

import pandas as pd
import yaml
from jobspy import scrape_jobs

from schema import JOB_COLUMNS


SEARCH_TERMS_PATH = Path("config/search_terms.yaml")
OUTPUT_PATH = Path("data/raw_jobs.csv")


def load_search_terms():
    with open(SEARCH_TERMS_PATH, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config["keywords"]


def search_keyword(keyword):
    print(f"Searching: {keyword}")

    return scrape_jobs(
        site_name=["linkedin", "indeed"],
        search_term=keyword,
        location="Dublin, Ireland",
        results_wanted=100,
        hours_old=24,
        country_indeed="Ireland",
        linkedin_fetch_description=False,
        verbose=0,
    )


def search_jobs():
    results = []

    for keyword in load_search_terms():
        jobs = search_keyword(keyword)

        if jobs.empty:
            continue

        jobs["search_term"] = keyword
        results.append(jobs)

    if not results:
        return pd.DataFrame(columns=JOB_COLUMNS)

    jobs = pd.concat(
        results,
        ignore_index=True,
    )

    available_columns = [
        column
        for column in JOB_COLUMNS
        if column in jobs.columns
    ]

    jobs = jobs[available_columns]

    jobs = jobs.drop_duplicates(
        subset=["site", "id"],
        keep="first",
    )

    return jobs


if __name__ == "__main__":
    jobs = search_jobs()

    print(f"\nFound {len(jobs)} unique jobs\n")

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    jobs.to_csv(
        OUTPUT_PATH,
        index=False,
    )

    print(f"Saved results to {OUTPUT_PATH}")