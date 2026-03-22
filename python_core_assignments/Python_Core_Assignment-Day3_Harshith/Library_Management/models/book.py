from dataclasses import dataclass


@dataclass
class Book:
    book_id: str
    title: str
    author: str
    category: str
    status: str = "Available"

    @classmethod
    def from_dict(cls, row: dict) -> "Book":
        return cls(
            book_id=row["book_id"],
            title=row["title"],
            author=row["author"],
            category=row["category"],
            status=row.get("status", "Available"),
        )

    def to_dict(self) -> dict:
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "category": self.category,
            "status": self.status,
        }
