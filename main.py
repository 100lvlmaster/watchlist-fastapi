from fastapi import FastAPI, Request
from fastapi.param_functions import Depends
from models.settings import Settings
from routes import user, bookmark, auth
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

app = FastAPI()
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(bookmark.router)


@AuthJWT.load_config
def get_config():
    return Settings()


@app.get("/", tags="root")
async def hello_world(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return {"Hello world"}


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )
