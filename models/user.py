from enum import unique
from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from models.base import BaseMeta
from utils.timestamp import Timestamp
import ormar


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'users'
    id: int = ormar.UUID(primary_key=True)
    email: str = ormar.String(max_length=500, unique=True)
    username: str = ormar.String(max_length=200)
    photoUrl: str = ormar.String(max_length=400)


class UserIn(BaseModel):
    username: str
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    photoUrl: Optional[str]
