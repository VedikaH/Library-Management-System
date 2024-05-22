class BookManager:
    def __init__(self, storage):
        self.storage = storage
        self.books = self.storage.load_books()

    def add_book(self, book):
        self.books.append(book)
        self.storage.save_books(self.books)

    def update_book(self, isbn, **kwargs):
        book = self.search_book_by_isbn(isbn)
        if book:
            for key, value in kwargs.items():
                setattr(book, key, value)
            self.storage.save_books(self.books)

    def delete_book(self, isbn):
        book = self.search_book_by_isbn(isbn)
        if book:
            self.books.remove(book)
            self.storage.save_books(self.books)

    def list_books(self):
        return self.books

    def search_book_by_isbn(self, isbn):
        return next((book for book in self.books if book.isbn == isbn), None)

    def search_books_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

class UserManager:
    def __init__(self, storage):
        self.storage = storage
        self.users = self.storage.load_users()

    def add_user(self, user):
        self.users.append(user)
        self.storage.save_users(self.users)

    def update_user(self, user_id, **kwargs):
        user = self.search_user_by_id(user_id)
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            self.storage.save_users(self.users)

    def delete_user(self, user_id):
        user = self.search_user_by_id(user_id)
        if user:
            self.users.remove(user)
            self.storage.save_users(self.users)

    def list_users(self):
        return self.users

    def search_user_by_id(self, user_id):
        return next((user for user in self.users if user.user_id == user_id), None)

    def search_users_by_name(self, name):
        return [user for user in self.users if name.lower() in user.name.lower()]
