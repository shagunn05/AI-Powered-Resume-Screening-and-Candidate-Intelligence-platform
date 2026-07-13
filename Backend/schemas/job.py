from pydantic import BaseModel
from datetime import datetime
from typing import List


class JobCreate(BaseModel):
    job_title: str
    required_skills: List[str]
    experience: str
    education: str


class JobResponse(BaseModel):
    id: int
    job_title: str
    required_skills: str
    experience: str
    education: str
    uploaded_at: datetime

    class Config:
        from_attributes = True