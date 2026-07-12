from fastapi import APIRouter, UploadFile, File

from Backend.services.file_service import save_uploaded_file

router = APIRouter()


@router.post("/resume")
async def upload_resume(file: UploadFile = File(...)):

    result = save_uploaded_file(file)

    return {
        "message": "Resume uploaded successfully",
        "data": result
    }