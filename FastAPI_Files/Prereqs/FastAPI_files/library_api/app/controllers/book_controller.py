from fastapi import APIRouter, Depends
from dependencies.book_dependencies import get_book_service
from services.book_service import BookService

router = APIRouter()

@router.get("/books")
def get_books(book_service: BookService = Depends(get_book_service)):
    return book_service.get_all_books() 