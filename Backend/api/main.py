from fastapi import FastAPI

from Backend.api.routes.upload import router as upload_router

app = FastAPI(
    title="TalentPilot AI API",
    version="1.0.0"
)

app.include_router(
    upload_router,
    prefix="/upload",
    tags=["Upload"]
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