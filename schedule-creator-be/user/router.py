from fastapi import APIRouter, Response, Depends, Body, HTTPException
from pydantic import EmailStr
import logging
from models import User, UserIn, UserRegister
from config import CONFIG

from operations import UserOperations

router = APIRouter(
    prefix="/api/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

userOps = UserOperations()

@router.post("/register", response_model=User)
async def register(user: UserRegister):
    user.password = UserOperations.hash_password(user.password)
    user = await userOps.create_user(user)
    return user


@router.post("/login")
async def login_user(user_: UserIn):
    user = await userOps.get_user_by_email(user.email)
    if user:
        if UserOperations.verify_password(password=user_.password, hashed_password=user.password):
            return Response(status_code=200, content={'Message': 'Login Successful', 'User': user})
        else:
            raise HTTPException(status_code=401, detail="Incorrect password")
    else:
        raise HTTPException(status_code=404, detail="User not found")


