from app.repositories import application_repository
def apply_for_job_service(db, application: dict):
    return application_repository.apply_for_job(db, application)