from dataclasses import dataclass, field


@dataclass
class Member:
    member_id: str
    name: str
    email: str
    borrowed_books: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, row: dict) -> "Member":
        borrowed = row.get("borrowed_books", "").strip()
        borrowed_books = [book_id for book_id in borrowed.split(";") if book_id]
        return cls(
            member_id=row["member_id"],
            name=row["name"],
            email=row["email"],
            borrowed_books=borrowed_books,
        )

    def to_dict(self) -> dict:
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "borrowed_books": ";".join(self.borrowed_books),
        }
