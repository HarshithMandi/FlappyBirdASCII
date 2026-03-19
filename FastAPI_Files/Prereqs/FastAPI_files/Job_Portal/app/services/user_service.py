from app.repositories import user_repository
from app.schemas.user_schema import UserCreate
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

def create_user_service(db, user: UserCreate):
    existing = user_repository.get_user_by_email(db, user.email)
    if existing is not None:
        raise HTTPException(status_code=409, detail="Email already exists")
    try:
        return user_repository.create_user(db, user)
    except IntegrityError:
        # In case of a race condition where another request inserted the same email.
        raise HTTPException(status_code=409, detail="Email already exists")
def get_users_service(db, skip: int = 0, limit: int = 100):
    return user_repository.get_users(db, skip=skip, limit=limit)


def get_user_by_id_service(db, user_id: int):
    user = user_repository.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user