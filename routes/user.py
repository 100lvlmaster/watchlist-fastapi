from typing import Optional
from fastapi import APIRouter
router = APIRouter()


@router.get("/me", tags="users")
async def read_root():
    return {"Hello world"}
