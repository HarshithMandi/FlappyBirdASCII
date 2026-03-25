from sqlalchemy.orm import Session

from app.models.job import Job


class JobRepository:
    def create(self, db: Session, job: Job) -> Job:
        db.add(job)
        db.flush()
        return job

    def get(self, db: Session, job_id: int) -> Job | None:
        return db.query(Job).filter(Job.id == job_id).first()

    def list(self, db: Session, skip: int, limit: int) -> list[Job]:
        return db.query(Job).offset(skip).limit(limit).all()

    def update(self, db: Session, job: Job) -> Job:
        db.add(job)
        db.flush()
        return job

    def delete(self, db: Session, job: Job) -> None:
        db.delete(job)
