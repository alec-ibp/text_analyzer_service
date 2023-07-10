# type: ignore

import logging
import importlib

import uvicorn
from starlette.types import ASGIApp

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from conf import settings


def get_asgi_application() -> ASGIApp:
    app_name: str = "text_analyzer_service"
    docs_url = redoc_url = None
    if settings.DEBUG:
        docs_url = "/docs"
        redoc_url = "/redoc"
        logging.basicConfig(level=logging.DEBUG)

    app: ASGIApp = FastAPI(
        title=app_name,
        version=settings.VERSION,
        on_startup=[_startup_event],
        docs_url=docs_url,
        redoc_url=redoc_url,
    )

    _set_urls_apps(app)
    _configure_cors(app)
    return app


async def _startup_event() -> None:
    logger = logging.getLogger("uvicorn.access")
    console_formatter = uvicorn.logging.ColourizedFormatter(**settings.LOGGING)
    for index in range(len(logger.handlers)):
        logger.handlers[index].setFormatter(console_formatter)


def _set_urls_apps(app: ASGIApp):
    for _app in settings.INSTALLED_APPS:
        app_urls = importlib.import_module(f"text_analyzer_service.{_app}.urls")
        if not hasattr(app_urls, "router"):
            raise Exception("missing router")  # MissingAPIRouterError()
        app.include_router(app_urls.router)


def _configure_cors(app: ASGIApp) -> None:
    # configure fastapi cors
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=settings.CORS_ALLOWED_METHODS,
        allow_headers=settings.CORS_ALLOWED_HEADERS,
    )
