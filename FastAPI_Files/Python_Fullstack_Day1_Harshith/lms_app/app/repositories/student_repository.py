from app.core.db import db


class StudentRepository:
    def add_student(self, student_data: dict) -> dict:
        student = student_data.copy()
        student["id"] = db.student_id_counter
        db.student_id_counter += 1
        db.students.append(student)
        return student

    def get_student_by_id(self, student_id: int) -> dict | None:
        for student in db.students:
            if student["id"] == student_id:
                return student
        return None

    def find_by_email(self, email: str) -> dict | None:
        for student in db.students:
            if student["email"].lower() == email.lower():
                return student
        return None

    def list_students(self) -> list[dict]:
        return list(db.students)
