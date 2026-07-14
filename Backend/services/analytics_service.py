from collections import Counter


def calculate_skill_frequency(candidates):

    skills = []

    for candidate in candidates:

        if candidate.skills:

            candidate_skills = [
                skill.strip()
                for skill in candidate.skills.split(",")
                if skill.strip()
            ]

            skills.extend(candidate_skills)

    return dict(Counter(skills))


def calculate_dashboard_metrics(candidates, jobs):

    total_candidates = len(candidates)

    total_jobs = len(jobs)

    return {
        "total_candidates": total_candidates,
        "total_jobs": total_jobs
    }