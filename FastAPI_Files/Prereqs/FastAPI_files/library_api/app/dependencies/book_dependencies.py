from repository.book_repository import BookRepository
from services.book_service import BookService

repository = BookRepository()

def get_book_service():
    return BookService(repository)

#This is the dependency function.