from dataclasses import dataclass


@dataclass(slots=True)
class Enrollment:
    id: int
    student_id: int
    course_id: int
