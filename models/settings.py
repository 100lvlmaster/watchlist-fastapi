from pydantic import BaseModel
import os


class Settings(BaseModel):
    authjwt_secret_key: str = os.environ["JWT_SECRET"]
