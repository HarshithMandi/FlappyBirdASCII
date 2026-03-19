from fastapi import HTTPException, status
from models.student import Student
from database.db import students_db

def get_student_by_id(student_id: int) -> Student:
    for student in students_db:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

