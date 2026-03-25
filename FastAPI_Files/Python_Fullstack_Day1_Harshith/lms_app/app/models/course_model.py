from dataclasses import dataclass


@dataclass(slots=True)
class Course:
    id: int
    title: str
    duration: int
