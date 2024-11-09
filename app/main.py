import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

from .routers import api_router
from .middlewares import set_app_cors_middleware
from .utils import safe_get_env_var

def init_app() -> FastAPI:
    ### load .env ###
    load_dotenv()

    ### Create FastAPI Instance ###
    app = FastAPI(
        title=os.environ.get('APP_NAME'),
        version=os.environ.get('APP_VERSION')
    )

    set_app_cors_middleware(app)

    ### Include API Router to app ###
    app.include_router(api_router)


if __name__ == "__main__":
    load_dotenv()
    reload = safe_get_env_var("APP_ENVIRONMENT") == "development" # allows automatic reloading with changes

    app = init_app()
    uvicorn.run(app, host="0.0.0.0", port=int(safe_get_env_var("PORT")), reload=reload, debug=reload)