from app.model.job import Job

def _schema_to_dict(schema) -> dict:
    if isinstance(schema, dict):
        return schema
    if hasattr(schema, "model_dump"):
        return schema.model_dump()
    return schema.dict()


def create_job(db, job):
    """Create a Job from a Pydantic schema instance."""
    db_job = Job(**_schema_to_dict(job))
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_jobs(db):
    return db.query(Job).all()