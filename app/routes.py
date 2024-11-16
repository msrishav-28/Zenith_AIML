from flask import Blueprint, render_template, request
from .skill_extractor import extract_skills
from .job_matcher import match_jobs

main = Blueprint('main', __name__)

@main.route('/')
def home():
    """Home page."""
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads."""
    if 'cv' not in request.files:
        return 'No file part in the request', 400

    file = request.files['cv']
    if file.filename == '':
        return 'No file selected', 400

    user_name = request.form.get('user_name', 'Guest')
    extracted_skills = extract_skills(file)
    job_listings = match_jobs(extracted_skills)

    return render_template(
        'results.html',
        user_name=user_name,
        skills=extracted_skills,
        jobs=job_listings
    )
