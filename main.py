import databases
from fastapi import FastAPI, Request
from fastapi.param_functions import Depends
import sqlalchemy
import uvicorn
from models.settings import Settings
from routes import user, bookmark, auth
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from database.db import database

app = FastAPI()
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(bookmark.router)
#
metadata = sqlalchemy.MetaData()
database = databases.Database("sqlite:///test.db")
app.state.database = database


DATABASE_URL = "sqlite:///./test.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


def _setup_database():
    # if you do not have the database run this once
    engine = sqlalchemy.create_engine(DATABASE_URL)
    metadata.drop_all(engine)
    metadata.create_all(engine)
    return engine, database


_setup_database()


@AuthJWT.load_config
def get_config():
    return Settings()


@app.get("/", tags="root")
async def hello_world(Authorize: AuthJWT = Depends()):
    # Authorize.jwt_required()
    return {"Hello world"}


@app.exception_handler(AuthJWTException)
async def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
