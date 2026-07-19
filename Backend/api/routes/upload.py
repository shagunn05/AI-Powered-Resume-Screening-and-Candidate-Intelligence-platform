from fastapi import APIRouter, UploadFile, File
from pathlib import Path

from Backend.services.file_service import save_uploaded_file
from Backend.parser.pdf_parser import extract_text_from_pdf
from Backend.parser.docx_parser import extract_text_from_docx
from Backend.parser.text_cleaner import clean_text
from Backend.parser.information_extractor import extract_information
from Backend.parser.skills_extractor import extract_skills

from fastapi import Depends
from sqlalchemy.orm import Session

from Backend.database.database import get_db
from Backend.database.crud import create_candidate
from fastapi import HTTPException


router = APIRouter()


@router.post("/resume")
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    try:
        result = save_uploaded_file(file)
        print(result)

        file_path = result["filepath"]

        extension = Path(file.filename).suffix.lower()

        if extension == ".pdf":
             raw_text = extract_text_from_pdf(file_path)
        elif extension == ".docx":
             raw_text = extract_text_from_docx(file_path)
        else:
            return {"error": "Unsupported file format"}

        # Debug
        print("RAW TEXT")
        print(raw_text[:1000])

        clean_resume = clean_text(raw_text)

        print("=" * 100)
        print(clean_resume)
        print("=" * 100)
       
        candidate = extract_information(clean_resume)

        print("=" * 60)
        print("Extracted Candidate Data:")
        print(candidate)
        print("=" * 60)

        candidate["skills"] = extract_skills(clean_resume)
        print("Skills:", candidate["skills"])

        saved_candidate = create_candidate(db, candidate)
        print("=" * 60)
        print("Saved Candidate")
        print("ID:", saved_candidate.id)
        print("Name:", saved_candidate.name)
        print("Email:", saved_candidate.email)
        print("=" * 60)
        return {
            "message": "Resume uploaded successfully",
            "candidate": {
                "id": saved_candidate.id,
                "name": saved_candidate.name,
                "email": saved_candidate.email,
                "phone": saved_candidate.phone,
                "skills": saved_candidate.skills,
                "uploaded_at": saved_candidate.uploaded_at
            }
        }

    
    
    except Exception as e:
        import traceback
        traceback.print_exc()

        raise HTTPException(
          status_code=500,
          detail=str(e)
        )