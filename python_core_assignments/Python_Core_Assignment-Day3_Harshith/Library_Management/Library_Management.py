import csv
import os

BOOKS_FILE = "books.csv"
MEMBERS_FILE = "members.csv"


class BookNotFoundError(Exception):
    pass

class BookAlreadyBorrowedError(Exception):
    pass

class MemberNotFoundError(Exception):
    pass

class BookNotBorrowedError(Exception):
    pass


class Book:
    def __init__(self, book_id, title, author, category, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.status = status

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "category": self.category,
            "status": self.status
        }


class Member:
    def __init__(self, member_id, name, email, borrowed_books=""):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = borrowed_books

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "borrowed_books": self.borrowed_books
        }


def init_files():
    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["book_id", "title", "author", "category", "status"])
            writer.writeheader()
            writer.writerows([
                {"book_id": "101", "title": "Python Programming", "author": "John Smith", "category": "Programming", "status": "Available"},
                {"book_id": "102", "title": "Data Science Handbook", "author": "Jane Miller", "category": "Data Science", "status": "Available"},
                {"book_id": "103", "title": "Machine Learning", "author": "Andrew Ng", "category": "AI", "status": "Available"}
            ])

    if not os.path.exists(MEMBERS_FILE):
        with open(MEMBERS_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["member_id", "name", "email", "borrowed_books"])
            writer.writeheader()


def load_books():
    try:
        with open(BOOKS_FILE, "r") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        raise FileNotFoundError("Error: Data file not found.")


def save_books(books):
    with open(BOOKS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["book_id", "title", "author", "category", "status"])
        writer.writeheader()
        writer.writerows(books)


def load_members():
    try:
        with open(MEMBERS_FILE, "r") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        raise FileNotFoundError("Error: Data file not found.")


def save_members(members):
    with open(MEMBERS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["member_id", "name", "email", "borrowed_books"])
        writer.writeheader()
        writer.writerows(members)


def view_books():
    books = load_books()
    if not books:
        print("No books found.")
        return
    print(f"\n{'ID':<8} {'Title':<30} {'Author':<20} {'Category':<15} {'Status'}")
    print("-" * 85)
    for b in books:
        print(f"{b['book_id']:<8} {b['title']:<30} {b['author']:<20} {b['category']:<15} {b['status']}")


def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    category = input("Enter Category: ")
    book = Book(book_id, title, author, category)
    books = load_books()
    books.append(book.to_dict())
    save_books(books)
    print("Book added successfully.")


def register_member():
    member_id = input("Enter Member ID: ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    member = Member(member_id, name, email)
    members = load_members()
    members.append(member.to_dict())
    save_members(members)
    print("Member registered successfully.")


def borrow_book():
    member_id = input("Enter Member ID: ")
    book_id = input("Enter Book ID: ")

    books = load_books()
    members = load_members()

    book = next((b for b in books if b["book_id"] == book_id), None)
    member = next((m for m in members if m["member_id"] == member_id), None)

    if not book:
        raise BookNotFoundError("Error: Book not found.")
    if not member:
        raise MemberNotFoundError("Error: Member not found.")
    if book["status"] == "Borrowed":
        raise BookAlreadyBorrowedError("Error: Book is already borrowed.")

    book["status"] = "Borrowed"
    borrowed = member["borrowed_books"]
    member["borrowed_books"] = f"{borrowed},{book_id}".strip(",") if borrowed else book_id

    save_books(books)
    save_members(members)
    print("Book borrowed successfully.")


def return_book():
    member_id = input("Enter Member ID: ")
    book_id = input("Enter Book ID: ")

    books = load_books()
    members = load_members()

    book = next((b for b in books if b["book_id"] == book_id), None)
    member = next((m for m in members if m["member_id"] == member_id), None)

    if not book:
        raise BookNotFoundError("Error: Book not found.")
    if not member:
        raise MemberNotFoundError("Error: Member not found.")

    borrowed_list = member["borrowed_books"].split(",") if member["borrowed_books"] else []
    if book_id not in borrowed_list:
        raise BookNotBorrowedError("Error: Book not borrowed by this member.")

    book["status"] = "Available"
    borrowed_list.remove(book_id)
    member["borrowed_books"] = ",".join(borrowed_list)

    save_books(books)
    save_members(members)
    print("Book returned successfully.")


def view_members():
    members = load_members()
    if not members:
        print("No members found.")
        return
    print(f"\n{'Member ID':<12} {'Name':<20} {'Email':<25} {'Borrowed Books'}")
    print("-" * 75)
    for m in members:
        print(f"{m['member_id']:<12} {m['name']:<20} {m['email']:<25} {m['borrowed_books']}")


init_files()

while True:
    print("\n===== Library Management System =====")
    print("1. View Books")
    print("2. Add Book")
    print("3. Register Member")
    print("4. View Members")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")

    try:
        if choice == '1':
            view_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            register_member()
        elif choice == '4':
            view_members()
        elif choice == '5':
            borrow_book()
        elif choice == '6':
            return_book()
        elif choice == '7':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
    except (BookNotFoundError, BookAlreadyBorrowedError, MemberNotFoundError, BookNotBorrowedError, FileNotFoundError) as e:
        print(e)
