class CourseNotFoundError(Exception):
    pass


class StudentNotFoundError(Exception):
    pass


class CourseFullError(Exception):
    pass


class CourseAlreadyEnrolledError(Exception):
    pass


class CourseNotEnrolledError(Exception):
    pass
