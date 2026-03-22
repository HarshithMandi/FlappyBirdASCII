from dataclasses import dataclass


@dataclass
class Course:
	course_id: str
	course_name: str
	instructor: str
	seats_available: int

	def to_dict(self) -> dict:
		return {
			"course_id": self.course_id,
			"course_name": self.course_name,
			"instructor": self.instructor,
			"seats_available": str(self.seats_available),
		}
