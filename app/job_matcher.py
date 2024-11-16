import pandas as pd

def match_jobs(skills):
    """Match jobs based on extracted skills."""
    try:
        # Load job dataset
        df = pd.read_csv('linkedin_jobs.csv')

        # Filter jobs based on skills
        matching_jobs = df[df['Job Description'].str.contains('|'.join(skills), case=False, na=False)]
        job_listings = matching_jobs[['Job Title', 'Company Name', 'Location', 'Estimated Salary']].to_dict(orient='records')

        return job_listings
    except FileNotFoundError:
        return [{"Job Title": "No data", "Company Name": "N/A", "Location": "N/A", "Estimated Salary": "N/A"}]
