from fastapi import FastAPI

from app.controllers.course_controller import router as course_router
from app.controllers.enrollment_controller import router as enrollment_router
from app.controllers.student_controller import router as student_router
from app.middleware.cors import add_cors_middleware

app = FastAPI(title="LMS API", version="1.0")

add_cors_middleware(app)

app.include_router(course_router)
app.include_router(student_router)
app.include_router(enrollment_router)


@app.get("/")
def health_check() -> dict:
    return {"status": "ok"}
