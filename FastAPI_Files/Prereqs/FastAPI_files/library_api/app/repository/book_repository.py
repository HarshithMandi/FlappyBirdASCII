class BookRepository:
    def __init__(self):
        self._books = [
            {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "published_year": 1925},
            {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "published_year": 1960},
            {"id": 3, "title": "1984", "author": "George Orwell", "published_year": 1949},
        ]
    
    def get_all_books(self):
        return self._books