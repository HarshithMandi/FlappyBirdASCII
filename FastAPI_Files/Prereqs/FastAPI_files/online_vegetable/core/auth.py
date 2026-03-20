from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from core.config import settings
from models.user import User
from repositories.user_repository import UserRepository
from core.dependencies import get_user_repository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

roles_permissions = {
    "admin":["admin","user"],
    "user":["user"]
}

def create_access_token(data: dict):
    to_encode = data.copy()
    token = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token

def get_current_user(token: str = Depends(oauth2_scheme), repo: UserRepository = Depends(get_user_repository)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = repo.get_by_email(email)
    if user is None:
        raise credentials_exception
    return user