from fastapi import APIRouter
from fastapi.params import Depends
from fastapi_jwt_auth.auth_jwt import AuthJWT
from models.user import CreateUser
router = APIRouter(prefix="/auth")


@router.post("/login")
def login(user: CreateUser, Authorize: AuthJWT = Depends()):

    refresh_token = Authorize.create_refresh_token(subject=user.email)
    access_token = Authorize.create_access_token(subject=user.email)
    return {"user": user, "access_token": access_token, "refresh_token": refresh_token}
