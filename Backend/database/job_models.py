from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from Backend.database.database import Base


class Job(Base):

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    job_title = Column(String)

    required_skills = Column(String)

    experience = Column(String)

    education = Column(String)

    uploaded_at = Column(DateTime, default=datetime.utcnow)