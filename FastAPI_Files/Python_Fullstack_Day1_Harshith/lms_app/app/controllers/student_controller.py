from fastapi import APIRouter, Depends, HTTPException

from app.dependencies.dependencies import get_student_service
from app.schemas.student_schema import StudentCreate, StudentResponse
from app.services.student_service import StudentService

router = APIRouter(prefix="/students", tags=["students"])


@router.post("", response_model=StudentResponse, status_code=201)
def register_student(
    payload: StudentCreate,
    service: StudentService = Depends(get_student_service),
) -> StudentResponse:
    try:
        return service.register_student(payload)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: int,
    service: StudentService = Depends(get_student_service),
) -> StudentResponse:
    try:
        return service.get_student(student_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
