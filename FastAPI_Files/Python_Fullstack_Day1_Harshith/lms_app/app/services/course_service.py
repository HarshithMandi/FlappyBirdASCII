from app.repositories.course_repository import CourseRepository
from app.schemas.course_schema import CourseCreate, CourseResponse


class CourseService:
    def __init__(self, course_repository: CourseRepository) -> None:
        self.course_repository = course_repository

    def create_course(self, payload: CourseCreate) -> CourseResponse:
        existing = self.course_repository.find_by_title(payload.title)
        if existing is not None:
            raise ValueError("Course title already exists")

        created = self.course_repository.add_course(payload.model_dump())
        return CourseResponse(**created)

    def list_courses(self) -> list[CourseResponse]:
        courses = self.course_repository.list_courses()
        return [CourseResponse(**course) for course in courses]

    def get_course(self, course_id: int) -> CourseResponse:
        course = self.course_repository.get_course_by_id(course_id)
        if course is None:
            raise ValueError("Course not found")

        return CourseResponse(**course)
