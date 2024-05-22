import json
from book import Book
from user import User

class Storage:
    def __init__(self, book_file='books.json', user_file='users.json'):
        self.book_file = book_file
        self.user_file = user_file

    def load_books(self):
        try:
            with open(self.book_file, 'r') as file:
                return [Book(**data) for data in json.load(file)]
        except FileNotFoundError:
            return []

    def save_books(self, books):
        with open(self.book_file, 'w') as file:
            json.dump([book.__dict__ for book in books], file)

    def load_users(self):
        try:
            with open(self.user_file, 'r') as file:
                return [User(**data) for data in json.load(file)]
        except FileNotFoundError:
            return []

    def save_users(self, users):
        with open(self.user_file, 'w') as file:
            json.dump([user.__dict__ for user in users], file)
