from pathlib import Path
import sys

import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from exceptions.custom_exceptions import BookAlreadyBorrowedError, BookNotFoundError
from services.library_service import LibraryService


@pytest.fixture
def service(tmp_path: Path) -> LibraryService:
    books = tmp_path / "books.csv"
    members = tmp_path / "members.csv"

    books.write_text(
        "book_id,title,author,category,status\n"
        "101,Python Programming,John Smith,Programming,Available\n",
        encoding="utf-8",
    )
    members.write_text(
        "member_id,name,email,borrowed_books\n"
        "M001,Ravi,ravi@gmail.com,\n",
        encoding="utf-8",
    )

    return LibraryService(books_file=books, members_file=members)


def test_borrow_book_success(service: LibraryService):
    service.borrow_book("M001", "101")
    books = service.view_books()
    assert books[0].status == "Borrowed"


def test_borrow_unavailable_book(service: LibraryService):
    service.borrow_book("M001", "101")
    with pytest.raises(BookAlreadyBorrowedError):
        service.borrow_book("M001", "101")


def test_borrow_invalid_book(service: LibraryService):
    with pytest.raises(BookNotFoundError):
        service.borrow_book("M001", "999")


def test_return_book_success(service: LibraryService):
    service.borrow_book("M001", "101")
    service.return_book("M001", "101")
    books = service.view_books()
    assert books[0].status == "Available"
