from sqlalchemy.orm import Session

from app.exceptions.custom_exceptions import ForbiddenError, NotFoundError
from app.models.job import Job
from app.models.user import UserRole
from app.repositories.job_repository import JobRepository
from app.repositories.user_repository import UserRepository
from app.schemas.job_schema import JobCreate, JobUpdate


class JobService:
    def __init__(self, repository: JobRepository, user_repo: UserRepository):
        self.repository = repository
        self.user_repo = user_repo

    def create_job(self, db: Session, payload: JobCreate, actor_id: int) -> Job:
        actor = self.user_repo.get(db, actor_id)
        if not actor:
            raise NotFoundError("Actor user not found")
        if actor.role not in {UserRole.admin, UserRole.recruiter}:
            raise ForbiddenError("Only recruiters or admins can create jobs")
        if actor.role == UserRole.recruiter and payload.company_id != actor.id:
            raise ForbiddenError("Recruiters can only create jobs for their own company_id")

        job = Job(**payload.model_dump())
        with db.begin():
            return self.repository.create(db, job)

    def get_job(self, db: Session, job_id: int) -> Job:
        job = self.repository.get(db, job_id)
        if not job:
            raise NotFoundError("Job not found")
        return job

    def list_jobs(self, db: Session, skip: int, limit: int) -> list[Job]:
        return self.repository.list(db, skip, limit)

    def update_job(self, db: Session, job_id: int, payload: JobUpdate, actor_id: int) -> Job:
        actor = self.user_repo.get(db, actor_id)
        if not actor:
            raise NotFoundError("Actor user not found")
        if actor.role not in {UserRole.admin, UserRole.recruiter}:
            raise ForbiddenError("Only recruiters or admins can update jobs")

        job = self.get_job(db, job_id)
        if actor.role == UserRole.recruiter and job.company_id != actor.id:
            raise ForbiddenError("Recruiters can only update their own jobs")

        update_data = payload.model_dump(exclude_unset=True)
        if actor.role == UserRole.recruiter and "company_id" in update_data and update_data["company_id"] != actor.id:
            raise ForbiddenError("Recruiters cannot change company_id")

        for field, value in update_data.items():
            setattr(job, field, value)
        with db.begin():
            return self.repository.update(db, job)

    def delete_job(self, db: Session, job_id: int, actor_id: int) -> None:
        actor = self.user_repo.get(db, actor_id)
        if not actor:
            raise NotFoundError("Actor user not found")
        if actor.role not in {UserRole.admin, UserRole.recruiter}:
            raise ForbiddenError("Only recruiters or admins can delete jobs")

        job = self.get_job(db, job_id)
        if actor.role == UserRole.recruiter and job.company_id != actor.id:
            raise ForbiddenError("Recruiters can only delete their own jobs")

        with db.begin():
            self.repository.delete(db, job)
