
from sqlalchemy.orm import Session
from Backend.database.models import Candidate


# Create Candidate
def create_candidate(db: Session, candidate_data: dict):

    # Check duplicate email
    existing_candidate = (
        db.query(Candidate)
        .filter(Candidate.email == candidate_data.get("email"))
        .first()
    )

    if existing_candidate:
        return existing_candidate

    candidate = Candidate(
        name=candidate_data.get("name"),
        email=candidate_data.get("email"),
        phone=candidate_data.get("phone"),
        skills=", ".join(candidate_data.get("skills", []))
    )

    db.add(candidate)
    db.commit()
    db.refresh(candidate)

    return candidate


# Get all candidates
def get_all_candidates(db: Session):
    return db.query(Candidate).all()


# Get candidate by ID
def get_candidate_by_id(db: Session, candidate_id: int):
    return (
        db.query(Candidate)
        .filter(Candidate.id == candidate_id)
        .first()
    )


# Delete candidate
def delete_candidate(db: Session, candidate_id: int):
    candidate = (
        db.query(Candidate)
        .filter(Candidate.id == candidate_id)
        .first()
    )

    if candidate:
        db.delete(candidate)
        db.commit()

    return candidate