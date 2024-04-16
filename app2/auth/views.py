import secrets
from fastapi import APIRouter,HTTPException,Depends,status
from fastapi.security import HTTPBasic,HTTPBasicCredentials
from typing import Annotated,Any


router = APIRouter(prefix="/auth", tags=["Auth"])

security = HTTPBasic()

username_to_passwords = {
    "admin":"admin",
}

def auth_get_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
)-> str:
    unauthed_ex = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail="Invalid login or password",
    )        
    correct_password = username_to_passwords.get(credentials.username)
    if correct_password is None:
        raise unauthed_ex
    
    if not secrets.compare_digest(
        credentials.password.encode("utf-8"),
        correct_password.encode("utf-8")
    ):
        raise unauthed_ex
    
    return credentials.username

@router.get("/")
def auth_with_username(
    auth_username: str = Depends(auth_get_username)
):
    return {
        "message" : f"Hi,{auth_username}",
        "username" : auth_username,
    }