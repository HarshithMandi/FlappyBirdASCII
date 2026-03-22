# Student Course Registration System

## Objective
A menu-driven Python system to manage courses, student registration, course enrollment, and course dropping using CSV files.

## Project Structure
- `main.py`
- `models/course.py`
- `models/student.py`
- `services/registration_service.py`
- `utils/file_handler.py`
- `exceptions/custom_exceptions.py`
- `data/courses.csv`
- `data/students.csv`
- `tests/test_registration.py`

## Features
- Add new courses
- View all available courses
- Register students
- View student details
- Enroll students in courses
- Drop courses for students
- Handles key exceptions (`Course Not Found`, `Student Not Found`, `Course Full`, `File Not Found`)

## Run Application
From `course_registration_system` folder:

```bash
python main.py
```

## Run Tests
From `course_registration_system` folder:

```bash
python -m unittest tests/test_registration.py -v
```
