def calculate_match_score(candidate_skills, job_skills):

    candidate = {
        skill.strip().lower()
        for skill in candidate_skills.split(",")
        if skill.strip()
    }

    required = {
        skill.strip().lower()
        for skill in job_skills.split(",")
        if skill.strip()
    }

    matched = candidate.intersection(required)

    if len(required) == 0:
        return 0, []

    score = round((len(matched) / len(required)) * 100)

    return score, list(matched)

def recommendation(score):

    if score >= 85:
        return "Hire"

    elif score >= 65:
        return "Hold"

    else:
        return "Reject"
    
def candidate_level(score):

    if score >= 85:
        return "Excellent"

    elif score >= 70:
        return "Good"

    elif score >= 50:
        return "Average"

    return "Poor"

def rank_candidate(candidate, job):

    score, matched = calculate_match_score(
        candidate.skills,
        job.required_skills
    )

    return {

        "id": candidate.id,

        "name": candidate.name,

        "email": candidate.email,

        "score": score,

        "matched_skills": matched,

        "recommendation": recommendation(score),

        "level": candidate_level(score)

    }

 