from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..utils import safe_get_env_var


def set_app_cors_middleware(app: FastAPI) -> None:
    cors_origins = safe_get_env_var('CORS_ORIGINS')
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins.split(","),
        allow_methods=["GET", "POST", "DELETE", "PATCH", "PUT"],
        allow_headers=[
            'Authorization',
            'Content-Type',
            'Origin',
            'Referrer',
            'User-Agent',
            'Accept',
            # Add additional Headers here #
        ]
    )