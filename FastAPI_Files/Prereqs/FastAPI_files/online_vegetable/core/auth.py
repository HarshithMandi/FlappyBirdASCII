from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from core.config import settings
from models.user import User
from repositories.user_repository import UserRepository
from core.dependencies import get_user_repository

roles_permissions = {
    "admin":["admin","user"],
    "user":["user"]
}

def create_access_token(data: dict):
    to_encode = data.copy()
    token = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


async def get_current_user(token: str = Depends(oauth2_scheme), repo: UserRepository = Depends(get_user_repository)):
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
    user = await repo.get_by_email(email)
    if user is None:
        raise credentials_exception
    return user

def require_role(role: str):
    def role_checker(current_user: User = Depends(get_current_user)):
        if role not in roles_permissions.get(current_user.role, []):
            raise HTTPException(status_code=403, detail="Not enough permissions")
    return role_checker