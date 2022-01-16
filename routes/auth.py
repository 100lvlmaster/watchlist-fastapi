from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from fastapi_jwt_auth.auth_jwt import AuthJWT
from models.user import UserIn, User
#
router = APIRouter(prefix="/auth")
#


@router.post("/login")
async def login(user: UserIn):
    # existing_user = await users.find_one({'email': user.email})
    # refresh_token = Authorize.create_refresh_token(subject=user.email)
    # access_token = Authorize.create_access_token(subject=user.email)
    # return {"user": existing_user, "access_token": access_token, "refresh_token": refresh_token}
    return {"user": user}
