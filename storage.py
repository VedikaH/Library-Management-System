import json
from book import Book
from user import User

class Storage:
    def __init__(self, book_file='books.json', user_file='users.json'):
        """
        Initialize the Storage object.

        Args:
            book_file (str): Path to the file storing book data. Default is 'books.json'.
            user_file (str): Path to the file storing user data. Default is 'users.json'.
        """
        self.book_file = book_file
        self.user_file = user_file

    def load_books(self):
        """
        Load book data from the JSON file.

        Returns:
            list: List of Book objects loaded from the file.
        """
        try:
            with open(self.book_file, 'r') as file:
                data = json.load(file)
                return [Book(**item) for item in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as e:
            print(f"Error loading books: {e}")
            return []

    def save_books(self, books):
        """
        Save book data to the JSON file.

        Args:
            books (list): List of Book objects to be saved.
        """
        try:
            with open(self.book_file, 'w') as file:
                json.dump([book.__dict__ for book in books], file, indent=4)
        except Exception as e:
            print(f"Error saving books: {e}")

    def load_users(self):
        """
        Load user data from the JSON file.

        Returns:
            list: List of User objects loaded from the file.
        """
        try:
            with open(self.user_file, 'r') as file:
                data = json.load(file)
                return [User(**item) for item in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as e:
            print(f"Error loading users: {e}")
            return []

    def save_users(self, users):
        """
        Save user data to the JSON file.

        Args:
            users (list): List of User objects to be saved.
        """
        try:
            with open(self.user_file, 'w') as file:
                json.dump([user.__dict__ for user in users], file, indent=4)
        except Exception as e:
            print(f"Error saving users: {e}")
