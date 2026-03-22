import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
COURSES_FILE = DATA_DIR / "courses.csv"
STUDENTS_FILE = DATA_DIR / "students.csv"

COURSE_FIELDS = ["course_id", "course_name", "instructor", "seats_available"]
STUDENT_FIELDS = ["student_id", "name", "email", "enrolled_courses"]


def ensure_data_files() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not COURSES_FILE.exists():
        with COURSES_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=COURSE_FIELDS)
            writer.writeheader()

    if not STUDENTS_FILE.exists():
        with STUDENTS_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=STUDENT_FIELDS)
            writer.writeheader()


def read_courses() -> list[dict]:
    if not COURSES_FILE.exists():
        raise FileNotFoundError("Error: Course data file not found")

    with COURSES_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def write_courses(courses: list[dict]) -> None:
    with COURSES_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=COURSE_FIELDS)
        writer.writeheader()
        writer.writerows(courses)


def read_students() -> list[dict]:
    if not STUDENTS_FILE.exists():
        raise FileNotFoundError("Error: Student data file not found")

    with STUDENTS_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def write_students(students: list[dict]) -> None:
    with STUDENTS_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=STUDENT_FIELDS)
        writer.writeheader()
        writer.writerows(students)
