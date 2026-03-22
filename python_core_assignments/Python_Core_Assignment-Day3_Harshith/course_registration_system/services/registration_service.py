from exceptions.custom_exceptions import (
    CourseAlreadyEnrolledError,
    CourseFullError,
    CourseNotEnrolledError,
    CourseNotFoundError,
    StudentNotFoundError,
)
from models.course import Course
from models.student import Student
from utils.file_handler import (
    ensure_data_files,
    read_courses,
    read_students,
    write_courses,
    write_students,
)


class RegistrationService:
    def __init__(self) -> None:
        ensure_data_files()

    def view_courses(self) -> list[dict]:
        return read_courses()

    def add_course(
        self,
        course_id: str,
        course_name: str,
        instructor: str,
        seats_available: int,
    ) -> str:
        courses = read_courses()
        if any(course["course_id"] == course_id for course in courses):
            raise ValueError("Error: Course ID already exists")

        course = Course(course_id, course_name, instructor, seats_available)
        courses.append(course.to_dict())
        write_courses(courses)
        return "Course added successfully"

    def register_student(self, student_id: str, name: str, email: str) -> str:
        students = read_students()
        if any(student["student_id"] == student_id for student in students):
            raise ValueError("Error: Student ID already exists")

        student = Student(student_id, name, email)
        students.append(student.to_dict())
        write_students(students)
        return "Student registered successfully"

    def view_students(self) -> list[dict]:
        return read_students()

    def enroll_course(self, student_id: str, course_id: str) -> str:
        courses = read_courses()
        students = read_students()

        course = next((c for c in courses if c["course_id"] == course_id), None)
        if not course:
            raise CourseNotFoundError("Error: Course not found")

        student = next((s for s in students if s["student_id"] == student_id), None)
        if not student:
            raise StudentNotFoundError("Error: Student not found")

        enrolled_courses = (
            student["enrolled_courses"].split(",") if student["enrolled_courses"] else []
        )
        if course_id in enrolled_courses:
            raise CourseAlreadyEnrolledError("Error: Student already enrolled in this course")

        seats_available = int(course["seats_available"])
        if seats_available <= 0:
            raise CourseFullError("Error: No seats available for this course")

        enrolled_courses.append(course_id)
        student["enrolled_courses"] = ",".join(enrolled_courses)
        course["seats_available"] = str(seats_available - 1)

        write_students(students)
        write_courses(courses)
        return "Course enrollment successful"

    def drop_course(self, student_id: str, course_id: str) -> str:
        courses = read_courses()
        students = read_students()

        course = next((c for c in courses if c["course_id"] == course_id), None)
        if not course:
            raise CourseNotFoundError("Error: Course not found")

        student = next((s for s in students if s["student_id"] == student_id), None)
        if not student:
            raise StudentNotFoundError("Error: Student not found")

        enrolled_courses = (
            student["enrolled_courses"].split(",") if student["enrolled_courses"] else []
        )
        if course_id not in enrolled_courses:
            raise CourseNotEnrolledError("Error: Student is not enrolled in this course")

        enrolled_courses.remove(course_id)
        student["enrolled_courses"] = ",".join(enrolled_courses)
        course["seats_available"] = str(int(course["seats_available"]) + 1)

        write_students(students)
        write_courses(courses)
        return "Course dropped successfully"
