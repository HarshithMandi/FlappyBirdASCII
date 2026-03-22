import unittest
from pathlib import Path

from exceptions.custom_exceptions import (
    CourseFullError,
    CourseNotEnrolledError,
    CourseNotFoundError,
    StudentNotFoundError,
)
from services.registration_service import RegistrationService
from utils import file_handler


class TestRegistrationService(unittest.TestCase):
    def setUp(self):
        file_handler.ensure_data_files()

        file_handler.write_courses(
            [
                {
                    "course_id": "C101",
                    "course_name": "Python Programming",
                    "instructor": "Dr.Kumar",
                    "seats_available": "2",
                },
                {
                    "course_id": "C102",
                    "course_name": "Data Science Fundamentals",
                    "instructor": "Dr.Smith",
                    "seats_available": "0",
                },
            ]
        )

        file_handler.write_students(
            [
                {
                    "student_id": "S001",
                    "name": "Ravi Kumar",
                    "email": "ravi@gmail.com",
                    "enrolled_courses": "",
                }
            ]
        )

        self.service = RegistrationService()

    def test_view_courses(self):
        courses = self.service.view_courses()
        self.assertEqual(len(courses), 2)

    def test_register_student_success(self):
        message = self.service.register_student("S002", "Meena Priya", "meena@gmail.com")
        self.assertEqual(message, "Student registered successfully")

    def test_enroll_course_success(self):
        message = self.service.enroll_course("S001", "C101")
        self.assertEqual(message, "Course enrollment successful")

    def test_enroll_full_course(self):
        with self.assertRaises(CourseFullError):
            self.service.enroll_course("S001", "C102")

    def test_course_not_found(self):
        with self.assertRaises(CourseNotFoundError):
            self.service.enroll_course("S001", "C999")

    def test_student_not_found(self):
        with self.assertRaises(StudentNotFoundError):
            self.service.enroll_course("S999", "C101")

    def test_drop_course_success(self):
        self.service.enroll_course("S001", "C101")
        message = self.service.drop_course("S001", "C101")
        self.assertEqual(message, "Course dropped successfully")

    def test_drop_course_not_enrolled(self):
        with self.assertRaises(CourseNotEnrolledError):
            self.service.drop_course("S001", "C101")


if __name__ == "__main__":
    unittest.main()
