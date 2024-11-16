import PyPDF2
import docx

SKILL_SET = {
    "Python", "Java", "C++", "JavaScript", "SQL", "HTML", "CSS", "Flask",
    "Django", "Machine Learning", "Data Analysis", "Git", "Docker",
    "Kubernetes", "AWS", "Azure"
}

def extract_skills(file):
    """Extract skills from the uploaded resume."""
    file_extension = file.filename.split('.')[-1].lower()
    text_content = ""

    if file_extension == 'txt':
        text_content = file.read().decode('utf-8')

    elif file_extension == 'pdf':
        pdf_reader = PyPDF2.PdfReader(file.stream)
        for page in pdf_reader.pages:
            text_content += page.extract_text()

    elif file_extension == 'docx':
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text_content += para.text

    # Find matching skills
    extracted_skills = [skill for skill in SKILL_SET if skill.lower() in text_content.lower()]
    return extracted_skills
