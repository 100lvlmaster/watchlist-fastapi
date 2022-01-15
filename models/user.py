from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from models.bson_models import PyObjectId
from utils.timestamp import Timestamp


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    photoUrl: Optional[str]
    disabled: Optional[bool] = False
    createdAt: int = Timestamp()
    updatedAt: int = Timestamp()

    class Config:
        schema_extra = {
            "example": {
                "username": "100lvlmaster",
                "fullname": "Navin Kodag",
                "email": "navinkodag@gmail.com",
                "disabled": False
            }
        }


class UserIn(BaseModel):
    username: str
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    photoUrl: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "username": "100lvlmaster",
                "fullname": "Navin Kodag",
                "email": "navinkodag@gmail.com",
            }
        }
