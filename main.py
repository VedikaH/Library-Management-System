from book import Book
from models import BookManager, UserManager
from storage import Storage
from user import User


def main():
    # Initialize storage and managers
    storage = Storage()
    book_manager = BookManager(storage)
    user_manager = UserManager(storage)

    
    while True:
        # Display main menu options
        print("Library Management System")
        print("1. Manage Books")
        print("2. Manage Users")
        print("3. Check Out Book")
        print("4. Check In Book")
        print("5. Exit")

        # Get user choice
        choice = input("Enter your choice: ")

        # Perform actions based on user choice
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
            add_book(book_manager)
        elif choice == '2':
            update_book(book_manager)
        elif choice == '3':
            delete_book(book_manager)
        elif choice == '4':
            list_books(book_manager)
        elif choice == '5':
            search_book_by_isbn(book_manager)
        elif choice == '6':
            search_book_by_title(book_manager)
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
            add_user(user_manager)
        elif choice == '2':
            update_user(user_manager)
        elif choice == '3':
            delete_user(user_manager)
        elif choice == '4':
            list_users(user_manager)
        elif choice == '5':
            search_user_by_id(user_manager)
        elif choice == '6':
            search_user_by_name(user_manager)
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

    # Update book availability and print success message
    book.available = False
    book_manager.update_book(book.isbn, available=book.available)
    print(f"Book '{book.title}' checked out to {user.name}.")


def check_in_book(book_manager, user_manager):
    # Check in a book from a user
    isbn = input("Enter book ISBN: ")
    book = book_manager.search_book_by_isbn(isbn)
    if not book:
        print("Book not found.")
        return

    # Update book availability and print success message
    book.available = True
    book_manager.update_book(book.isbn, available=book.available)
    print(f"Book '{book.title}' checked in.")



def add_book(book_manager):
    title = input("Enter title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    if not isbn.isdigit():  # ISBN should contain only digits
        print("Invalid ISBN. Please enter a valid ISBN.")
        return
    book = Book(title, author, isbn)
    book_manager.add_book(book)
    print("Book added successfully.")


def update_book(book_manager):
    isbn = input("Enter ISBN of the book to update: ")
    title = input("Enter new title: ")
    author = input("Enter new author: ")
    available = input("Is the book available (yes/no): ").lower()
    if available not in ('yes', 'no'):
        print("Invalid input for availability. Please enter 'yes' or 'no'.")
        return
    book_manager.update_book(isbn, title=title, author=author, available=available == 'yes')
    print("Book updated successfully.")


def delete_book(book_manager):
    isbn = input("Enter ISBN of the book to delete: ")
    book_manager.delete_book(isbn)
    print("Book deleted successfully.")


def list_books(book_manager):
    for book in book_manager.list_books():
        print(book)


def search_book_by_isbn(book_manager):
    isbn = input("Enter ISBN: ")
    book = book_manager.search_book_by_isbn(isbn)
    print(book if book else "Book not found.")


def search_book_by_title(book_manager):
    title = input("Enter title: ")
    books = book_manager.search_books_by_title(title)
    for book in books:
        print(book)


# Helper functions for managing users
def add_user(user_manager):
    name = input("Enter name: ")
    user_id = input("Enter user ID: ")
    if not user_id.isalnum():  # User ID should contain only alphanumeric characters
        print("Invalid user ID. Please enter a valid user ID.")
        return
    user = User(name, user_id)
    user_manager.add_user(user)
    print("User added successfully.")


def update_user(user_manager):
    user_id = input("Enter user ID to update: ")
    name = input("Enter new name: ")
    user_manager.update_user(user_id, name=name)
    print("User updated successfully.")


def delete_user(user_manager):
    user_id = input("Enter user ID to delete: ")
    user_manager.delete_user(user_id)
    print("User deleted successfully.")


def list_users(user_manager):
    for user in user_manager.list_users():
        print(user)


def search_user_by_id(user_manager):
    user_id = input("Enter user ID: ")
    user = user_manager.search_user_by_id(user_id)
    print(user if user else "User not found.")


def search_user_by_name(user_manager):
    name = input("Enter name: ")
    users = user_manager.search_users_by_name(name)
    for user in users:
        print(user)


if __name__ == '__main__':
    main()
