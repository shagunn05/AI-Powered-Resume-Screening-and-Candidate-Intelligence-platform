from pydantic import BaseModel
from typing import List
from datetime import datetime


class CandidateCreate(BaseModel):
    name: str
    email: str
    phone: str
    skills: List[str]


class CandidateResponse(CandidateCreate):
    id: int
    uploaded_at: datetime

    class Config:
        from_attributes = True