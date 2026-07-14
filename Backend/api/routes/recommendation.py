from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Backend.database.database import get_db
from Backend.database.crud import get_candidate_by_id
from Backend.database.job_crud import get_job_by_id

from Backend.ai.hiring_recommendation import generate_hiring_recommendation

router = APIRouter(
    prefix="/recommendation",
    tags=["AI Hiring Recommendation"]
)


@router.get("/{candidate_id}/{job_id}")
def hiring_recommendation(
    candidate_id: int,
    job_id: int,
    db: Session = Depends(get_db)
):

    candidate = get_candidate_by_id(db, candidate_id)

    if candidate is None:
        return {
            "error": "Candidate not found"
        }

    job = get_job_by_id(db, job_id)

    if job is None:
        return {
            "error": "Job not found"
        }

    recommendation = generate_hiring_recommendation(
        candidate,
        job
    )

    return {

        "candidate": candidate.name,

        "job": job.job_title,

        "recommendation": recommendation

    }