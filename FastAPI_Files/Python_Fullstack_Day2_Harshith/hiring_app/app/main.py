from fastapi import FastAPI

from app.controllers.application_controller import router as application_router
from app.controllers.job_controller import router as job_router
from app.controllers.user_controller import router as user_router
from app.core.database import create_db_and_tables
from app.core.logger import configure_logging
from app.exceptions.exception_handlers import register_exception_handlers
from app.middleware.cors import add_cors_middleware
from app.middleware.logging import LoggingMiddleware


def create_app() -> FastAPI:
    configure_logging()
    app = FastAPI(title="Hiring Application")

    add_cors_middleware(app, ["*"])
    app.add_middleware(LoggingMiddleware)

    app.include_router(user_router, prefix="/users", tags=["users"])
    app.include_router(job_router, prefix="/jobs", tags=["jobs"])
    app.include_router(application_router, prefix="/applications", tags=["applications"])

    register_exception_handlers(app)

    @app.on_event("startup")
    def _startup() -> None:
        create_db_and_tables()

    return app


app = create_app()
