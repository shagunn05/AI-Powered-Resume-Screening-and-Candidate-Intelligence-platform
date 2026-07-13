def calculate_match_score(candidate_skills, job_skills):

    candidate_set = set(
        skill.strip().lower()
        for skill in candidate_skills
    )

    job_set = set(
        skill.strip().lower()
        for skill in job_skills
    )

    matched = candidate_set.intersection(job_set)

    missing = job_set - candidate_set

    if len(job_set) == 0:
        score = 0
    else:
        score = round(
            (len(matched) / len(job_set)) * 100,
            2
        )

    return {

        "score": score,

        "matched_skills": list(matched),

        "missing_skills": list(missing)

    }