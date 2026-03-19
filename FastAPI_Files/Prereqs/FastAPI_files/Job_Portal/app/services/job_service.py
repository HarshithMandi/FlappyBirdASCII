from app.repositories import job_repository
from app.schemas.job_schema import JobCreate

def create_job_service(db, job: JobCreate):
    return job_repository.create_job(db, job)

def get_jobs_service(db):
    return job_repository.get_jobs(db)