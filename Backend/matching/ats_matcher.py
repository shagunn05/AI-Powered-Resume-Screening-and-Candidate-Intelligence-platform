from Backend.matching.similarity import calculate_match_score


def ats_match(candidate, job):

    candidate_skills = candidate.skills.split(",")

    job_skills = job.required_skills.split(",")

    result = calculate_match_score(

        candidate_skills,

        job_skills

    )

    score = result["score"]

    if score >= 85:

        recommendation = "Highly Recommended"

    elif score >= 70:

        recommendation = "Recommended"

    elif score >= 50:

        recommendation = "Average Match"

    else:

        recommendation = "Not Recommended"

    return {

        "candidate_name": candidate.name,

        "job_title": job.job_title,

        "match_score": score,

        "matched_skills": result["matched_skills"],

        "missing_skills": result["missing_skills"],

        "recommendation": recommendation

    }