from fastapi import APIRouter, Depends, HTTPException, status
from jose import JWTError, jwt
from datetime import datetime, timedelta
from pydantic import BaseModel
import httpx
import os


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

router = APIRouter()


class User(BaseModel):
    id: str
    email: str
    first_name: str | None
    last_name: str | None
    email_verified: bool
    created_at: str
    updated_at: str


class Token(BaseModel):
    access_token: str
    token_type: str


class HttpError(BaseModel):
    detail: str


def create_access_token(data: dict, expries_delta: timedelta = None):
    to_encode = data.copy()
    if expries_delta:
        expire = datetime.utcnow() + expries_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

asynce def authenticate_user(id: str):
    response = await httpx.get(
        f"https://api.workos.com/directory_sync/users/{id}",
        headers={"Authorization": f"Bearer {os.getenv('WORKOS_API_KEY')}"},
    )

@router.get("/token", response_model=UserToken | None)
async def get_token(
    request: Request,
    user: UserOut = Depends(authenticator.try_get_current_account_data),
) -> UserToken | None:
    if user and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "user": user,
        }
