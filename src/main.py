from google_sheets import write_jobs
from search_jobs import search_jobs


def main():
    jobs = search_jobs()

    if jobs.empty:
        print("No jobs found.")
        return

    write_jobs(jobs)


if __name__ == "__main__":
    main()