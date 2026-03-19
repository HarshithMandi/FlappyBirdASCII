from app.repositories import job_repository

def create_job_service(db, job: dict):
    return job_repository.create_job(db, job)

def get_jobs_service(db):
    return job_repository.get_jobs(db)