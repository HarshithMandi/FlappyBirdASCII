from fastapi import APIRouter, Depends, HTTPException

from app.dependencies.dependencies import get_enrollment_service
from app.schemas.enrollment_schema import EnrollmentCreate, EnrollmentResponse, StudentEnrollmentResponse
from app.services.enrollment_service import EnrollmentService

router = APIRouter(prefix="/enrollments", tags=["enrollments"])


@router.post("", response_model=EnrollmentResponse, status_code=201)
def enroll_student(
    payload: EnrollmentCreate,
    service: EnrollmentService = Depends(get_enrollment_service),
) -> EnrollmentResponse:
    try:
        return service.enroll_student(payload)
    except ValueError as exc:
        detail = str(exc)
        status_code = 404 if detail in {"Student not found", "Course not found"} else 400
        raise HTTPException(status_code=status_code, detail=detail)


@router.get("", response_model=list[EnrollmentResponse])
def list_enrollments(
    service: EnrollmentService = Depends(get_enrollment_service),
) -> list[EnrollmentResponse]:
    return service.list_enrollments()


@router.get("/students/{student_id}", response_model=list[StudentEnrollmentResponse])
def list_enrollments_by_student(
    student_id: int,
    service: EnrollmentService = Depends(get_enrollment_service),
) -> list[StudentEnrollmentResponse]:
    try:
        return service.list_enrollments_by_student(student_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@router.get("/courses/{course_id}", response_model=list[EnrollmentResponse])
def list_enrollments_by_course(
    course_id: int,
    service: EnrollmentService = Depends(get_enrollment_service),
) -> list[EnrollmentResponse]:
    try:
        return service.list_enrollments_by_course(course_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
