from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services import application_service
from app.schemas.application_schema import ApplicationCreate

router = APIRouter(prefix="/applications", tags=["Applications"])

@router.post("/")
def apply_for_job(application: ApplicationCreate, db: Session = Depends(get_db)):
    return application_service.apply_for_job_service(db, application)