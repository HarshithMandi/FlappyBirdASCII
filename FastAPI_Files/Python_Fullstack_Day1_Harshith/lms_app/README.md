# LMS API

Clean Architecture FastAPI project using in-memory storage.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

## Endpoints

- POST /courses
- GET /courses
- GET /courses/{course_id}
- POST /students
- GET /students/{student_id}
- POST /enrollments
- GET /enrollments
- GET /enrollments/students/{student_id}
- GET /enrollments/courses/{course_id}
- GET /students/{student_id}/enrollments (alias)
