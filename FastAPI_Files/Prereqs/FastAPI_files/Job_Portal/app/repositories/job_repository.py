from app.model.job import Job

def create_job(db, job):
    """Create a Job from a Pydantic schema instance."""
    db_job = Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_jobs(db):
    return db.query(Job).all()