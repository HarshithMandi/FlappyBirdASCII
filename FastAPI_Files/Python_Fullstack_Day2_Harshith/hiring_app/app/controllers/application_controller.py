from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.application_repository import ApplicationRepository
from app.repositories.job_repository import JobRepository
from app.repositories.user_repository import UserRepository
from app.schemas.application_schema import ApplicationCreate, ApplicationResponse, ApplicationStatusUpdate
from app.services.application_service import ApplicationService

router = APIRouter()


def get_service() -> ApplicationService:
    return ApplicationService(ApplicationRepository(), UserRepository(), JobRepository())


@router.post("", response_model=ApplicationResponse)
def apply_for_job(
    payload: ApplicationCreate,
    db: Session = Depends(get_db),
    x_actor_user_id: int = Header(..., alias="X-Actor-User-Id"),
):
    return get_service().apply(db, payload, actor_id=x_actor_user_id)


@router.get("/{application_id}", response_model=ApplicationResponse)
def get_application(application_id: int, db: Session = Depends(get_db)):
    return get_service().get_application(db, application_id)


@router.get("", response_model=list[ApplicationResponse])
def list_applications(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_service().list_applications(db, skip, limit)


@router.put("/{application_id}/status", response_model=ApplicationResponse)
def update_application_status(
    application_id: int,
    payload: ApplicationStatusUpdate,
    db: Session = Depends(get_db),
):
    return get_service().update_status(db, application_id, payload)


@router.get("/users/{user_id}/applications", response_model=list[ApplicationResponse])
def list_user_applications(
    user_id: int,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    x_actor_user_id: int = Header(..., alias="X-Actor-User-Id"),
):
    return get_service().list_user_applications(db, user_id, skip, limit, actor_id=x_actor_user_id)
