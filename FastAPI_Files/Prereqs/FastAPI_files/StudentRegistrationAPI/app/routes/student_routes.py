from fastapi import APIRouter, Depends, HTTPException, status
from models.student import Student
from typing import List, Optional
from dependencies.student_dependency import get_student_by_id

router = APIRouter()
students_db: List[Student] = []

@router.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
    students_db.append(student)
    #return {"message": "Student created successfully", "student": student}
    return student

@router.get("/students", response_model=List[Student], status_code=status.HTTP_200_OK)
def get_students():
    return {"students": students_db}

@router.get("/students/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
def get_student(student_id: Student= Depends(get_student_by_id)):
    return student_id

@router.put("/students/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students_db):
        if student.id == student_id:
            students_db[index] = updated_student
            return updated_student

@router.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    for index, student in enumerate(students_db):
        if student.id == student_id:
            del students_db[index]
            return






















































































































