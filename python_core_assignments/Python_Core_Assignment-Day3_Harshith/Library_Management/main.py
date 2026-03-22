from exceptions.custom_exceptions import LibraryError
from services.library_service import LibraryService


def print_books(service: LibraryService) -> None:
    books = service.view_books()
    print("\nAvailable Books")
    for book in books:
        print(f"Book ID : {book.book_id}")
        print(f"Title   : {book.title}")
        print(f"Author  : {book.author}")
        print(f"Status  : {book.status}")
        print("-")


def main() -> None:
    service = LibraryService()

    while True:
        print("\n===== Library Management System =====")
        print("1. View Books")
        print("2. Add Book")
        print("3. Register Member")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                print_books(service)
            elif choice == "2":
                book_id = input("Enter Book ID: ").strip()
                title = input("Enter Title: ").strip()
                author = input("Enter Author: ").strip()
                category = input("Enter Category: ").strip()
                service.add_book(book_id, title, author, category)
                print("Book added successfully.")
            elif choice == "3":
                member_id = input("Enter Member ID: ").strip()
                name = input("Enter Member Name: ").strip()
                email = input("Enter Email: ").strip()
                service.register_member(member_id, name, email)
                print("Member registered successfully.")
            elif choice == "4":
                member_id = input("Enter Member ID: ").strip()
                book_id = input("Enter Book ID: ").strip()
                service.borrow_book(member_id, book_id)
                print("Book borrowed successfully.")
            elif choice == "5":
                member_id = input("Enter Member ID: ").strip()
                book_id = input("Enter Book ID: ").strip()
                service.return_book(member_id, book_id)
                print("Book returned successfully.")
            elif choice == "6":
                print("Thank you for using the Library Management System.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except LibraryError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
