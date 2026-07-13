from sqlalchemy.orm import Session
from Backend.database.job_models import Job

def get_job_by_id(db: Session, job_id: int):

    return (
        db.query(Job)
        .filter(Job.id == job_id)
        .first()
    )

def get_all_jobs(db: Session):

    return db.query(Job).all()



def create_job(db: Session, job_data: dict):

    job = Job(

        job_title=job_data.get("job_title"),

        required_skills=", ".join(
            job_data.get("required_skills", [])
        ),

        experience=job_data.get("experience"),

        education=job_data.get("education")

    )

    db.add(job)

    db.commit()

    db.refresh(job)

    return job