from fastapi import FastAPI

from Backend.api.routes import upload
from Backend.api.routes import candidate

from Backend.database.database import Base, engine
from Backend.api.routes import job
from Backend.api.routes import matching


# Create Database Tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="TalentPilot AI API",
    version="1.0.0"
)

app.include_router(job.router)
app.include_router(matching.router)


# Upload API
app.include_router(
    upload.router,
    prefix="/upload",
    tags=["Upload"]
)

# Candidate API
app.include_router(
    candidate.router,
    tags=["Candidate Management"]
)


@app.get("/")
def root():
    return {
        "message": "Welcome to TalentPilot AI Backend 🚀"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "TalentPilot AI Backend"
    }

