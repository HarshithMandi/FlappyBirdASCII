from app.repository.book_repository import BookRepository
from app.services.book_service import BookService

repository=BookRepository()

def get_book_service():
    return BookService(repository)