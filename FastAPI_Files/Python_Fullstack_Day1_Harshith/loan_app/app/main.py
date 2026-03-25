from fastapi import FastAPI

from app.controllers.loan_controller import router as loan_router
from app.middleware.cors import add_cors_middleware

app = FastAPI(title="Loan Management API", version="1.0")

add_cors_middleware(app)

app.include_router(loan_router)


@app.get("/")
def health_check() -> dict:
    return {"status": "ok"}
