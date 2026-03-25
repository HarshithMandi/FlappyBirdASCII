from app.core.db import db


class EnrollmentRepository:
    def add_enrollment(self, enrollment_data: dict) -> dict:
        enrollment = enrollment_data.copy()
        enrollment["id"] = db.enrollment_id_counter
        db.enrollment_id_counter += 1
        db.enrollments.append(enrollment)
        return enrollment

    def list_enrollments(self) -> list[dict]:
        return list(db.enrollments)

    def list_by_student(self, student_id: int) -> list[dict]:
        return [e for e in db.enrollments if e["student_id"] == student_id]

    def list_by_course(self, course_id: int) -> list[dict]:
        return [e for e in db.enrollments if e["course_id"] == course_id]

    def find_by_student_course(self, student_id: int, course_id: int) -> dict | None:
        for enrollment in db.enrollments:
            if enrollment["student_id"] == student_id and enrollment["course_id"] == course_id:
                return enrollment
        return None
