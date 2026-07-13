from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from Backend.database.database import get_db
from Backend.database.crud import (
    get_all_candidates,
    get_candidate_by_id,
    delete_candidate
)

router = APIRouter(prefix="/candidate", tags=["Candidates"])

# get all candidates
@router.get("/")
def fetch_all_candidates(db: Session = Depends(get_db)):
    candidates = get_all_candidates(db)

    return {
        "total_candidates": len(candidates),
        "data": candidates
    }

#get candidates by id
@router.get("/{candidate_id}")
def fetch_candidate(candidate_id: int,
                    db: Session = Depends(get_db)):

    candidate = get_candidate_by_id(db, candidate_id)

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    return candidate

#delete candidate

@router.delete("/{candidate_id}")
def remove_candidate(candidate_id: int,
                     db: Session = Depends(get_db)):

    candidate = delete_candidate(db, candidate_id)

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    return {
        "message": "Candidate deleted successfully"
    }

