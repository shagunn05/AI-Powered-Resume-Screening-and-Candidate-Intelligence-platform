from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Backend.database.database import get_db
from Backend.database.crud import get_all_candidates
from Backend.database.job_crud import get_all_jobs

from Backend.services.analytics_service import (
    calculate_dashboard_metrics,
    calculate_skill_frequency
)

router = APIRouter(
    prefix="/analytics",
    tags=["Recruiter Analytics"]
)


@router.get("/")
def analytics(db: Session = Depends(get_db)):

    candidates = get_all_candidates(db)

    jobs = get_all_jobs(db)

    metrics = calculate_dashboard_metrics(
        candidates,
        jobs
    )

    skills = calculate_skill_frequency(
        candidates
    )

    return {

        "metrics": metrics,

        "top_skills": skills

    }