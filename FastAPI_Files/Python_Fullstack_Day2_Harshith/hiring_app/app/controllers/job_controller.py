from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.job_repository import JobRepository
from app.repositories.user_repository import UserRepository
from app.schemas.job_schema import JobCreate, JobResponse, JobUpdate
from app.services.job_service import JobService

router = APIRouter()


def get_service() -> JobService:
    return JobService(JobRepository(), UserRepository())


@router.post("", response_model=JobResponse)
def create_job(
    payload: JobCreate,
    db: Session = Depends(get_db),
    x_actor_user_id: int = Header(..., alias="X-Actor-User-Id"),
):
    return get_service().create_job(db, payload, actor_id=x_actor_user_id)


@router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    return get_service().get_job(db, job_id)


@router.get("", response_model=list[JobResponse])
def list_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_service().list_jobs(db, skip, limit)


@router.put("/{job_id}", response_model=JobResponse)
def update_job(
    job_id: int,
    payload: JobUpdate,
    db: Session = Depends(get_db),
    x_actor_user_id: int = Header(..., alias="X-Actor-User-Id"),
):
    return get_service().update_job(db, job_id, payload, actor_id=x_actor_user_id)


@router.delete("/{job_id}")
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    x_actor_user_id: int = Header(..., alias="X-Actor-User-Id"),
):
    get_service().delete_job(db, job_id, actor_id=x_actor_user_id)
    return {"message": "Job deleted"}
