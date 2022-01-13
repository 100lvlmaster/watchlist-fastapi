from typing import Optional
from fastapi import APIRouter, Form
from fastapi.param_functions import Depends
from services.open_graph import get_open_graph
from fastapi_jwt_auth import AuthJWT

router = APIRouter(
    prefix="/bookmarks",
    tags=["bookmarks", "user-bookmarks"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{item_id}", tags='bookmarks',)
async def read_item(item_id: int, q: Optional[str] = None,  Authorize: AuthJWT = Depends(),):
    return {"item_id": item_id, "q": q}


@router.get("/user/{user_id}", tags='bookmarks')
async def read_user_bookmarks(user_id: int, q: Optional[str] = None):
    return {"item_id": user_id, "q": q}


@router.post("/", tags="bookmarks")
async def read_bookmarks(url: str = Form(...)):
    result = get_open_graph(url)
    return {"data": result}


@router.delete("/{item_id}", tags='delete-bookmark by id')
async def read_user_bookmarks(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
