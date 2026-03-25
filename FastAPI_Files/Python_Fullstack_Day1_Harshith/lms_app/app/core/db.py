class InMemoryDB:
    def __init__(self) -> None:
        self.students = []
        self.courses = []
        self.enrollments = []
        self.student_id_counter = 1
        self.course_id_counter = 1
        self.enrollment_id_counter = 1


db = InMemoryDB()
