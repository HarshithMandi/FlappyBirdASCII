from app.core.db import db


class CourseRepository:
    def add_course(self, course_data: dict) -> dict:
        course = course_data.copy()
        course["id"] = db.course_id_counter
        db.course_id_counter += 1
        db.courses.append(course)
        return course

    def get_course_by_id(self, course_id: int) -> dict | None:
        for course in db.courses:
            if course["id"] == course_id:
                return course
        return None

    def list_courses(self) -> list[dict]:
        return list(db.courses)

    def find_by_title(self, title: str) -> dict | None:
        for course in db.courses:
            if course["title"].lower() == title.lower():
                return course
        return None
