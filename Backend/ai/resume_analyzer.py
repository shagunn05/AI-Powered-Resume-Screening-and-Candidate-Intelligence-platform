from Backend.ai.llm import llm

def analyze_resume(candidate, job):

    prompt = f"""
You are an expert HR Recruiter.

Candidate Resume

Name:
{candidate.name}

Skills:
{candidate.skills}

Job Title:
{job.job_title}

Required Skills:
{job.required_skills}

Provide:

1. Resume Summary

2. Strengths

3. Weaknesses

4. Missing Skills

5. Improvement Suggestions

6. Hiring Recommendation

Return response in clean markdown.
"""

    response = llm.invoke(prompt)

    return response.content