from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from pathlib import Path

from Backend.database.database import get_db
from Backend.database.job_crud import create_job

from Backend.services.file_service import save_uploaded_file

from Backend.parser.jd_parser import extract_text_from_jd
from Backend.parser.jd_cleaner import clean_jd
from Backend.parser.jd_information_extractor import extract_job_information

router = APIRouter(
    prefix="/job",
    tags=["Job Management"]
)


@router.post("/upload")
async def upload_job(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    result = save_uploaded_file(file)

    file_path = result["filepath"]

    extension = Path(file.filename).suffix.lower()

    if extension != ".pdf":
        return {
            "error": "Only PDF Job Description supported."
        }

    raw_text = extract_text_from_jd(file_path)

    clean_text = clean_jd(raw_text)

    job_data = extract_job_information(clean_text)

    saved_job = create_job(db, job_data)

    return {

        "message": "Job Uploaded Successfully",

        "job": {

            "id": saved_job.id,

            "job_title": saved_job.job_title,

            "required_skills": saved_job.required_skills,

            "experience": saved_job.experience,

            "education": saved_job.education,

            "uploaded_at": saved_job.uploaded_at

        }

    }