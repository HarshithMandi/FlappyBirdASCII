from dataclasses import dataclass


@dataclass
class Student:
    student_id: str
    name: str
    email: str
    enrolled_courses: str = ""

    def to_dict(self) -> dict:
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "enrolled_courses": self.enrolled_courses,
        }
