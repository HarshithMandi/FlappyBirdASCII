from app.repositories import application_repository
from app.schemas.application_schema import ApplicationCreate

def apply_for_job_service(db, application: ApplicationCreate):
    return application_repository.apply_for_job(db, application)