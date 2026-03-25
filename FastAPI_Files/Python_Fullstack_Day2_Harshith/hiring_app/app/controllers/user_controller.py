from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from app.services.user_service import UserService

router = APIRouter()


def get_service() -> UserService:
    return UserService(UserRepository())


@router.post("", response_model=UserResponse)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    return get_service().create_user(db, payload)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_service().get_user(db, user_id)


@router.get("", response_model=list[UserResponse])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_service().list_users(db, skip, limit)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    payload: UserUpdate,
    db: Session = Depends(get_db),
    x_actor_user_id: int = Header(..., alias="X-Actor-User-Id"),
):
    return get_service().update_user(db, user_id, payload, actor_id=x_actor_user_id)


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    x_actor_user_id: int = Header(..., alias="X-Actor-User-Id"),
):
    get_service().delete_user(db, user_id, actor_id=x_actor_user_id)
    return {"message": "User deleted"}
