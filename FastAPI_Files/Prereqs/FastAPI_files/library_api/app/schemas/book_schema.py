from pydantic import BaseModel

class Book:
    id: int
    title: str
    author: str
    published_year: int