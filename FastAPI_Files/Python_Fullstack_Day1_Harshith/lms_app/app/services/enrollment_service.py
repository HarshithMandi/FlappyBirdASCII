from app.repositories.course_repository import CourseRepository
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.student_repository import StudentRepository
from app.schemas.enrollment_schema import (
    EnrollmentCreate,
    EnrollmentResponse,
    StudentEnrollmentResponse,
)


class EnrollmentService:
    def __init__(
        self,
        enrollment_repository: EnrollmentRepository,
        student_repository: StudentRepository,
        course_repository: CourseRepository,
    ) -> None:
        self.enrollment_repository = enrollment_repository
        self.student_repository = student_repository
        self.course_repository = course_repository

    def enroll_student(self, payload: EnrollmentCreate) -> EnrollmentResponse:
        student = self.student_repository.get_student_by_id(payload.student_id)
        if student is None:
            raise ValueError("Student not found")

        course = self.course_repository.get_course_by_id(payload.course_id)
        if course is None:
            raise ValueError("Course not found")

        existing = self.enrollment_repository.find_by_student_course(
            payload.student_id, payload.course_id
        )
        if existing is not None:
            raise ValueError("Already enrolled")

        created = self.enrollment_repository.add_enrollment(payload.model_dump())
        return EnrollmentResponse(**created)

    def list_enrollments(self) -> list[EnrollmentResponse]:
        enrollments = self.enrollment_repository.list_enrollments()
        return [EnrollmentResponse(**enrollment) for enrollment in enrollments]

    def list_enrollments_by_student(
        self, student_id: int
    ) -> list[StudentEnrollmentResponse]:
        student = self.student_repository.get_student_by_id(student_id)
        if student is None:
            raise ValueError("Student not found")

        enrollments = self.enrollment_repository.list_by_student(student_id)
        response: list[StudentEnrollmentResponse] = []
        for enrollment in enrollments:
            course = self.course_repository.get_course_by_id(enrollment["course_id"])
            if course is not None:
                response.append(
                    StudentEnrollmentResponse(
                        course_id=course["id"], course_title=course["title"]
                    )
                )
        return response

    def list_enrollments_by_course(self, course_id: int) -> list[EnrollmentResponse]:
        course = self.course_repository.get_course_by_id(course_id)
        if course is None:
            raise ValueError("Course not found")

        enrollments = self.enrollment_repository.list_by_course(course_id)
        return [EnrollmentResponse(**enrollment) for enrollment in enrollments]
