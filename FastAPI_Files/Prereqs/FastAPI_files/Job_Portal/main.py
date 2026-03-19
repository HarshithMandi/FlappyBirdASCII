from app.middleware.cors import add_cors_middleware
from app.middleware.exception_middleware import custom_exception_handler
from fastapi import FastAPI
from app.core.database import Base, engine
from app.controllers import job_controller, user_controller, application_controller
from app .middleware.logging_middleware import log_requests


app= FastAPI()

Base.metadata.create_all(bind=engine)

app.middleware("http")(log_requests)
add_cors_middleware(app)
app.add_exception_handler(Exception, custom_exception_handler)

app.include_router(job_controller.router)
app.include_router(user_controller.router)
app.include_router(application_controller.router)

app.get("/")
def root():
    return {"message": "Welcome to the Job Portal API!"}
