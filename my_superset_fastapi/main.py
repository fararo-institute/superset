from app.api.v1 import api_router
from app.core.config import get_settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import setup_logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.middleware import SlowAPIMiddleware


def create_app() -> FastAPI:
    settings = get_settings()
    setup_logging()
    app = FastAPI(title=settings.APP_NAME)

    if settings.ALLOWED_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.ALLOWED_ORIGINS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    if settings.RATE_LIMIT:
        limiter = Limiter(
            key_func=lambda request: request.client.host,
            default_limits=[settings.RATE_LIMIT],
        )
        app.state.limiter = limiter
        app.add_middleware(SlowAPIMiddleware)

    register_exception_handlers(app)

    app.include_router(api_router, prefix="/api/v1")
    # TODO: enable authentication routes once configuration is complete

    return app


app = create_app()
