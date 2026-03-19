from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services import user_service
from app.schemas.user_schema import UserCreate,UserResponse

router=APIRouter(prefix="/users",tags=["Users"])

@router.post("/",response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user_service(db, user)

@router.get("/",response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return user_service.get_users_service(db)



