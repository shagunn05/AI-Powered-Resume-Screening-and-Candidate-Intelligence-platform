KNOWN_SKILLS = [

    "Python",
    "Java",
    "C",
    "C++",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "Keras",
    "PyTorch",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "Power BI",
    "Excel",
    "FastAPI",
    "Streamlit",
    "LangChain",
    "LangGraph",
    "OpenAI",
    "Mistral AI",
    "Docker",
    "Git",
    "GitHub",
    "Linux",
    "AWS",
    "Azure",
    "REST API",
    "HTML",
    "CSS",
    "JavaScript"

]


def extract_skills(text: str):
    """
    Extract skills from resume.
    """

    found_skills = []

    lower_text = text.lower()

    for skill in KNOWN_SKILLS:

        if skill.lower() in lower_text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))