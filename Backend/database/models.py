from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from Backend.database.database import Base


class Candidate(Base):

    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    email = Column(String)

    phone = Column(String)

    skills = Column(String)

    uploaded_at = Column(DateTime, default=datetime.utcnow)