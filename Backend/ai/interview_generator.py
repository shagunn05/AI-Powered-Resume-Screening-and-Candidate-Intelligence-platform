from Backend.ai.llm import llm


def generate_questions(candidate, job):

    prompt = f"""
You are an experienced Technical Interviewer.

Your task is to generate interview questions based on the candidate's resume and the job description.

Candidate Details

Name:
{candidate.name}

Skills:
{candidate.skills}

Job Details

Job Title:
{job.job_title}

Required Skills:
{job.required_skills}

Instructions:

Generate EXACTLY 5 interview questions.

Question Distribution:

1. Technical Question
2. Technical Question
3. Project Based Question
4. Scenario Based Question
5. HR / Behavioral Question

Rules:

- Questions should be relevant to the candidate's skills.
- Questions should also match the required job skills.
- Keep questions professional.
- Do not provide answers.
- Return only the numbered list.

Example Format:

1. Explain the difference between Random Forest and XGBoost.

2. Describe one challenging project you have worked on.

3. Suppose an API suddenly becomes very slow. How would you debug it?

4. Explain how FastAPI handles asynchronous requests.

5. Why do you think you are suitable for this role?
"""

    response = llm.invoke(prompt)

    return response.content