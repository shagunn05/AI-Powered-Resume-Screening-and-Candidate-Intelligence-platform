from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Backend.database.database import get_db
from Backend.database.crud import get_all_candidates
from Backend.database.job_crud import get_job_by_id

from Backend.ai.ranking_engine import rank_candidate

router = APIRouter(
    prefix="/ranking",
    tags=["Candidate Ranking"]
)


@router.get("/{job_id}")
def ranking(job_id: int, db: Session = Depends(get_db)):

    job = get_job_by_id(db, job_id)

    if job is None:
        return {
            "error": "Job not found"
        }

    candidates = get_all_candidates(db)

    ranking_list = []

    for candidate in candidates:

        result = rank_candidate(candidate, job)

        ranking_list.append(result)

    ranking_list = sorted(
        ranking_list,
        key=lambda x: x["score"],
        reverse=True
    )

    for i, candidate in enumerate(ranking_list):

        candidate["rank"] = i + 1

    return {

        "job_title": job.job_title,

        "total_candidates": len(ranking_list),

        "ranking": ranking_list

    }
