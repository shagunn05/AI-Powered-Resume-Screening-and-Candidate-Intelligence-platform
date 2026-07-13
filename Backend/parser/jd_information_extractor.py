import re

SKILLS = [
    "Python",
    "SQL",
    "FastAPI",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "Scikit-learn",
    "Pandas",
    "NumPy",
    "Docker",
    "Git",
    "GitHub",
    "PostgreSQL",
    "LangChain",
    "LangGraph"
]


def extract_job_information(text):

    skills = []

    for skill in SKILLS:

        if skill.lower() in text.lower():

            skills.append(skill)

    # Experience
    experience = "Not Found"

    exp = re.search(
        r"(\d+\+?\s*(years?|yrs?))",
        text,
        re.IGNORECASE
    )

    if exp:
        experience = exp.group()

    # Education
    education = "Not Mentioned"

    education_keywords = [
        "Bachelor",
        "B.Tech",
        "B.E",
        "Master",
        "M.Tech",
        "MCA"
    ]

    for edu in education_keywords:

        if edu.lower() in text.lower():

            education = edu

            break

    # Job Title

    job_title = "AI Engineer"

    if "Data Scientist".lower() in text.lower():
        job_title = "Data Scientist"

    elif "Machine Learning Engineer".lower() in text.lower():
        job_title = "Machine Learning Engineer"

    return {

        "job_title": job_title,

        "required_skills": skills,

        "experience": experience,

        "education": education

    }