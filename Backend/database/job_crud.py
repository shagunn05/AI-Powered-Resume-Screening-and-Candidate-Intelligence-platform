from sqlalchemy.orm import Session
from Backend.database.job_models import Job


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