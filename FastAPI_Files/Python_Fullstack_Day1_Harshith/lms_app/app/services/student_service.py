from app.repositories.student_repository import StudentRepository
from app.schemas.student_schema import StudentCreate, StudentResponse


class StudentService:
    def __init__(self, student_repository: StudentRepository) -> None:
        self.student_repository = student_repository

    def register_student(self, payload: StudentCreate) -> StudentResponse:
        existing = self.student_repository.find_by_email(payload.email)
        if existing is not None:
            raise ValueError("Email already registered")

        created = self.student_repository.add_student(payload.model_dump())
        return StudentResponse(**created)

    def get_student(self, student_id: int) -> StudentResponse:
        student = self.student_repository.get_student_by_id(student_id)
        if student is None:
            raise ValueError("Student not found")

        return StudentResponse(**student)
