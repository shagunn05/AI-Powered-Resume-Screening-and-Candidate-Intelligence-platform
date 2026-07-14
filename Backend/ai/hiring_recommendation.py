from Backend.ai.llm import llm


def generate_hiring_recommendation(candidate, job):

    prompt = f"""
You are an experienced Senior Technical Recruiter.

Evaluate the candidate for the given job role.

### Candidate Information
Name: {candidate.name}

Skills:
{candidate.skills}

### Job Information
Job Title:
{job.job_title}

Required Skills:
{job.required_skills}

Experience:
{job.experience}

Education:
{job.education}

Generate a professional hiring report.

Return ONLY the following sections.

# Overall Match Score
Give a score out of 100.

# Hiring Decision
Choose ONLY one:
- Hire
- Hold
- Reject

# Candidate Strengths
Maximum 3 bullet points.

# Missing Skills
Maximum 3 bullet points.

# Interview Focus Areas
Maximum 3 bullet points.

# Final Recruiter Recommendation
Maximum 2 short professional lines.

Rules:
- Keep the entire report under 200 words.
- Return clean Markdown only.
- Do not explain your reasoning.
"""

    response = llm.invoke(prompt)

    return response.content