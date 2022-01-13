from pydantic import BaseModel
from decouple import config


class Settings(BaseModel):
    authjwt_secret_key: str = config('JWT_SECRET')
