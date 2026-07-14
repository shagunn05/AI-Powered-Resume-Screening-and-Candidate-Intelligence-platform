from Backend.ai.llm import llm


def generate_questions(candidate, job):

    prompt = f"""
You are an experienced Technical Interviewer.

Candidate Skills:
{candidate.skills}

Job Title:
{job.job_title}

Required Skills:
{job.required_skills}

Generate 10 technical interview questions.

Return only numbered questions.
"""

    response = llm.invoke(prompt)

    return response.content