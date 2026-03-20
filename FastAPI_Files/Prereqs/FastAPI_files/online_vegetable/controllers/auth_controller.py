from fastapi import APIRouter, Depends, HTTPException,status,Form
from fastapi.security import OAuth2PasswordRequestForm
from core.auth import create_access_token, get_current_user
from schemas.user_schema import UserCreate, UserOut
from core.dependencies import get_user_service
from passlib.context import CryptContext

router = APIRouter(prefix="/auth", tags=["auth"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/token")

async def login(form_data: OAuth2PasswordRequestForm = Depends(), service = Depends(get_user_service)):
    user = await service.get_user_by_email(form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.email, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}