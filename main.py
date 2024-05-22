# This is a deliberately poorly implemented main script for a Library Management System.
"""
import book_management
import user_management
import checkout_management

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. Checkout Book")
    print("5. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book_management.add_book(title, author, isbn)
            print("Book added.")
        elif choice == '2':
            book_management.list_books()
        elif choice == '3':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user_management.add_user(name, user_id)
            print("User added.")
        elif choice == '4':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            checkout_management.checkout_book(user_id, isbn)
            print("Book checked out.")
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
"""

from book import Book
from models import BookManager, UserManager
from storage import Storage
from user import User


def main():
    storage = Storage()
    book_manager = BookManager(storage)
    user_manager = UserManager(storage)

    while True:
        print("Library Management System")
        print("1. Manage Books")
        print("2. Manage Users")
        print("3. Check Out Book")
        print("4. Check In Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manage_books(book_manager)
        elif choice == '2':
            manage_users(user_manager)
        elif choice == '3':
            check_out_book(book_manager, user_manager)
        elif choice == '4':
            check_in_book(book_manager, user_manager)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_books(book_manager):
    while True:
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. List Books")
        print("5. Search Book by ISBN")
        print("6. Search Book by Title")
        print("7. Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            book_manager.add_book(book)
            print("Book added successfully.")
        elif choice == '2':
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            available = input("Is the book available (yes/no): ").lower() == 'yes'
            book_manager.update_book(isbn, title=title, author=author, available=available)
            print("Book updated successfully.")
        elif choice == '3':
            isbn = input("Enter ISBN of the book to delete: ")
            book_manager.delete_book(isbn)
            print("Book deleted successfully.")
        elif choice == '4':
            for book in book_manager.list_books():
                print(book)
        elif choice == '5':
            isbn = input("Enter ISBN: ")
            book = book_manager.search_book_by_isbn(isbn)
            print(book if book else "Book not found.")
        elif choice == '6':
            title = input("Enter title: ")
            books = book_manager.search_books_by_title(title)
            for book in books:
                print(book)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_users(user_manager):
    while True:
        print("1. Add User")
        print("2. Update User")
        print("3. Delete User")
        print("4. List Users")
        print("5. Search User by ID")
        print("6. Search User by Name")
        print("7. Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            user_id = input("Enter user ID: ")
            user = User(name, user_id)
            user_manager.add_user(user)
            print("User added successfully.")
        elif choice == '2':
            user_id = input("Enter user ID to update: ")
            name = input("Enter new name: ")
            user_manager.update_user(user_id, name=name)
            print("User updated successfully.")
        elif choice == '3':
            user_id = input("Enter user ID to delete: ")
            user_manager.delete_user(user_id)
            print("User deleted successfully.")
        elif choice == '4':
            for user in user_manager.list_users():
                print(user)
        elif choice == '5':
            user_id = input("Enter user ID: ")
            user = user_manager.search_user_by_id(user_id)
            print(user if user else "User not found.")
        elif choice == '6':
            name = input("Enter name: ")
            users = user_manager.search_users_by_name(name)
            for user in users:
                print(user)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

def check_out_book(book_manager, user_manager):
    user_id = input("Enter user ID: ")
    user = user_manager.search_user_by_id(user_id)
    if not user:
        print("User not found.")
        return

    isbn = input("Enter book ISBN: ")
    book = book_manager.search_book_by_isbn(isbn)
    if not book or not book.available:
        print("Book not available.")
        return

    book.available = False
    book_manager.update_book(book.isbn, available=book.available)
    print(f"Book {book.title} checked out to {user.name}.")

def check_in_book(book_manager, user_manager):
    isbn = input("Enter book ISBN: ")
    book = book_manager.search_book_by_isbn(isbn)
    if not book:
        print("Book not found.")
        return

    book.available = True
    book_manager.update_book(book.isbn, available=book.available)
    print(f"Book {book.title} checked in.")

if __name__ == '__main__':
    main()
