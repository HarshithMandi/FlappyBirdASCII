from fastapi import APIRouter, Depends, HTTPException
from schemas.user_schema import UserCreate, UserOut
from services.user_service import UserService
from core.dependencies import get_user_service
from core.auth import get_current_user, require_role

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserOut)
def register(user:UserCreate, service: UserService = Depends(get_user_service)):
    user_id = service.create_user(user)
    return {"id": user_id, **user.dict(), "role": "user"}

@router.get("/me", response_model=UserOut)
def get_me(current_user: UserOut = Depends(get_current_user)):
    return current_user

@router.get("/admin", dependencies=[Depends(require_role("admin"))])
def admin_only():
    return {"message": "Welcome, admin!"}