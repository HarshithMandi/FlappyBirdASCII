from app.repositories.course_repository import CourseRepository
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.student_repository import StudentRepository
from app.services.course_service import CourseService
from app.services.enrollment_service import EnrollmentService
from app.services.student_service import StudentService

_student_repository = StudentRepository()
_course_repository = CourseRepository()
_enrollment_repository = EnrollmentRepository()

_student_service = StudentService(_student_repository)
_course_service = CourseService(_course_repository)
_enrollment_service = EnrollmentService(
    _enrollment_repository, _student_repository, _course_repository
)


def get_student_service() -> StudentService:
    return _student_service


def get_course_service() -> CourseService:
    return _course_service


def get_enrollment_service() -> EnrollmentService:
    return _enrollment_service
