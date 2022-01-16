from pydantic import BaseModel, Field, AnyHttpUrl
from models.base import BaseMeta
from utils.timestamp import Timestamp
import ormar


class Bookmark(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'users'
    id: int = ormar.UUID(primary_key=True)
    url: str = ormar.String()
    img: str = ormar.String()
    title: str = ormar.String()
    description: str = ormar.String()
    site_name: str = ormar.String()
    createdAt: int = ormar.Time()
    updatedAt: int = ormar.Time()


class BookmarkIn(BaseModel):
    url: AnyHttpUrl = Field(...)
