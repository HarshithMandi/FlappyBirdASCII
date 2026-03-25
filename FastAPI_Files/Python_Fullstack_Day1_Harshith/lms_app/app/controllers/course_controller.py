from fastapi import APIRouter, Depends, HTTPException

from app.dependencies.dependencies import get_course_service
from app.schemas.course_schema import CourseCreate, CourseResponse
from app.services.course_service import CourseService

router = APIRouter(prefix="/courses", tags=["courses"])


@router.post("", response_model=CourseResponse, status_code=201)
def create_course(
    payload: CourseCreate,
    service: CourseService = Depends(get_course_service),
) -> CourseResponse:
    try:
        return service.create_course(payload)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.get("", response_model=list[CourseResponse])
def list_courses(
    service: CourseService = Depends(get_course_service),
) -> list[CourseResponse]:
    return service.list_courses()


@router.get("/{course_id}", response_model=CourseResponse)
def get_course(
    course_id: int,
    service: CourseService = Depends(get_course_service),
) -> CourseResponse:
    try:
        return service.get_course(course_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
