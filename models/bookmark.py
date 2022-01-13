from pydantic import BaseModel, Field
from utils.timestamp import Timestamp
from bson_models import PyObjectId
from bson import ObjectId


class Bookmark(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    url: str
    title: str
    imgUrl: str
    description: str
    site_name: str
    createdAt: int = Timestamp()
    updatedAt: int = Timestamp()

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id": "somteth",
                "url": "https://youtube.com",
                "title": "yo",
                "description": "this description",
                "imgUrl": "https://www.youtube.com/favicon.ico",
                "site_name": "Youtube"
            }
        }
