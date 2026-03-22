from pathlib import Path

from exceptions.custom_exceptions import (
    BookAlreadyBorrowedError,
    BookNotBorrowedByMemberError,
    BookNotFoundError,
    MemberNotFoundError,
)
from models.book import Book
from models.member import Member
from utils.file_handler import FileHandler


class LibraryService:
    def __init__(self, books_file: Path | None = None, members_file: Path | None = None):
        root = Path(__file__).resolve().parents[1]
        self.books_file = books_file or root / "data" / "books.csv"
        self.members_file = members_file or root / "data" / "members.csv"

    def _get_books(self) -> list[Book]:
        return [Book.from_dict(row) for row in FileHandler.read_csv(self.books_file)]

    def _save_books(self, books: list[Book]) -> None:
        rows = [book.to_dict() for book in books]
        FileHandler.write_csv(self.books_file, ["book_id", "title", "author", "category", "status"], rows)

    def _get_members(self) -> list[Member]:
        return [Member.from_dict(row) for row in FileHandler.read_csv(self.members_file)]

    def _save_members(self, members: list[Member]) -> None:
        rows = [member.to_dict() for member in members]
        FileHandler.write_csv(self.members_file, ["member_id", "name", "email", "borrowed_books"], rows)

    def view_books(self) -> list[Book]:
        return self._get_books()

    def add_book(self, book_id: str, title: str, author: str, category: str) -> None:
        books = self._get_books()
        books.append(Book(book_id=book_id, title=title, author=author, category=category, status="Available"))
        self._save_books(books)

    def register_member(self, member_id: str, name: str, email: str) -> None:
        members = self._get_members()
        members.append(Member(member_id=member_id, name=name, email=email))
        self._save_members(members)

    def borrow_book(self, member_id: str, book_id: str) -> None:
        members = self._get_members()
        books = self._get_books()

        member = next((m for m in members if m.member_id == member_id), None)
        if not member:
            raise MemberNotFoundError("Member not found")

        book = next((b for b in books if b.book_id == book_id), None)
        if not book:
            raise BookNotFoundError("Book not found")

        if book.status != "Available":
            raise BookAlreadyBorrowedError("Book is currently not available")

        book.status = "Borrowed"
        if book.book_id not in member.borrowed_books:
            member.borrowed_books.append(book.book_id)

        self._save_books(books)
        self._save_members(members)

    def return_book(self, member_id: str, book_id: str) -> None:
        members = self._get_members()
        books = self._get_books()

        member = next((m for m in members if m.member_id == member_id), None)
        if not member:
            raise MemberNotFoundError("Member not found")

        book = next((b for b in books if b.book_id == book_id), None)
        if not book:
            raise BookNotFoundError("Book not found")

        if book.book_id not in member.borrowed_books:
            raise BookNotBorrowedByMemberError("Book not borrowed by this member")

        member.borrowed_books.remove(book.book_id)
        book.status = "Available"

        self._save_books(books)
        self._save_members(members)
