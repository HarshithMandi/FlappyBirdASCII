from exceptions.custom_exceptions import (
	CourseAlreadyEnrolledError,
	CourseFullError,
	CourseNotEnrolledError,
	CourseNotFoundError,
	StudentNotFoundError,
)
from services.registration_service import RegistrationService


def print_courses(courses: list[dict]) -> None:
	if not courses:
		print("No courses available")
		return

	print(f"\n{'Course ID':<10} {'Course Name':<28} {'Instructor':<15} {'Seats'}")
	print("-" * 70)
	for course in courses:
		print(
			f"{course['course_id']:<10} {course['course_name']:<28} "
			f"{course['instructor']:<15} {course['seats_available']}"
		)


def print_students(students: list[dict]) -> None:
	if not students:
		print("No students found")
		return

	print(f"\n{'Student ID':<10} {'Name':<20} {'Email':<25} {'Enrolled Courses'}")
	print("-" * 80)
	for student in students:
		print(
			f"{student['student_id']:<10} {student['name']:<20} "
			f"{student['email']:<25} {student['enrolled_courses']}"
		)


def main() -> None:
	service = RegistrationService()

	while True:
		print("\n===== Student Course Registration System =====")
		print("1 View Courses")
		print("2 Add Course")
		print("3 Register Student")
		print("4 Enroll Course")
		print("5 Drop Course")
		print("6 View Students")
		print("7 Exit")

		choice = input("Enter your choice: ").strip()

		try:
			if choice == "1":
				print_courses(service.view_courses())

			elif choice == "2":
				course_id = input("Enter Course ID: ").strip()
				course_name = input("Enter Course Name: ").strip()
				instructor = input("Enter Instructor Name: ").strip()
				seats_available = int(input("Enter Available Seats: ").strip())
				print(service.add_course(course_id, course_name, instructor, seats_available))

			elif choice == "3":
				student_id = input("Enter Student ID: ").strip()
				name = input("Enter Student Name: ").strip()
				email = input("Enter Student Email: ").strip()
				print(service.register_student(student_id, name, email))

			elif choice == "4":
				student_id = input("Enter Student ID: ").strip()
				course_id = input("Enter Course ID: ").strip()
				print(service.enroll_course(student_id, course_id))

			elif choice == "5":
				student_id = input("Enter Student ID: ").strip()
				course_id = input("Enter Course ID: ").strip()
				print(service.drop_course(student_id, course_id))

			elif choice == "6":
				print_students(service.view_students())

			elif choice == "7":
				print("Exiting... Goodbye!")
				break

			else:
				print("Invalid choice. Please enter a valid option")

		except (
			FileNotFoundError,
			ValueError,
			CourseNotFoundError,
			StudentNotFoundError,
			CourseFullError,
			CourseAlreadyEnrolledError,
			CourseNotEnrolledError,
		) as error:
			print(error)


if __name__ == "__main__":
	main()
