class BookManager:
    def __init__(self, storage):
        """
        Initialize the BookManager with a storage instance.

        Args:
            storage: An instance of Storage class.
        """
        self.storage = storage
        self.books = self.storage.load_books()

    def add_book(self, book):
        """
        Add a book to the book collection.

        Args:
            book: An instance of the Book class to be added.

        Raises:
            TypeError: If the input parameter is not an instance of the Book class.
        """
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        self.books.append(book)
        self.storage.save_books(self.books)

    def update_book(self, isbn, **kwargs):
        """
        Update information of a book.

        Args:
            isbn: ISBN of the book to be updated.
            **kwargs: Dictionary containing attributes to be updated.

        Raises:
            AttributeError: If the specified attribute does not exist in the Book object.
        """
        book = self.search_book_by_isbn(isbn)
        if not book:
            print("Book not found.")
            return

        for key, value in kwargs.items():
            if hasattr(book, key):
                setattr(book, key, value)
            else:
                print(f"Invalid attribute '{key}' for book.")
        self.storage.save_books(self.books)

    def delete_book(self, isbn):
        """
        Delete a book from the collection.

        Args:
            isbn: ISBN of the book to be deleted.
        """
        book = self.search_book_by_isbn(isbn)
        if not book:
            print("Book not found.")
            return

        self.books.remove(book)
        self.storage.save_books(self.books)

    def list_books(self):
        """
        Get the list of all books.

        Returns:
            List: List of all books.
        """
        return self.books

    def search_book_by_isbn(self, isbn):
        """
        Search for a book by its ISBN.

        Args:
            isbn: ISBN of the book to be searched.

        Returns:
            Book: The book object if found, None otherwise.
        """
        return next((book for book in self.books if book.isbn == isbn), None)

    def search_books_by_title(self, title):
        """
        Search for books by title.

        Args:
            title: Title of the book(s) to be searched.

        Returns:
            List: List of book objects matching the title.
        """
        return [book for book in self.books if title.lower() in book.title.lower()]


class UserManager:
    def __init__(self, storage):
        """
        Initialize the UserManager with a storage instance.

        Args:
            storage: An instance of Storage class.
        """
        self.storage = storage
        self.users = self.storage.load_users()

    def add_user(self, user):
        """
        Add a user to the user collection.

        Args:
            user: An instance of the User class to be added.

        """
        if not isinstance(user, User):
            raise TypeError("user must be an instance of User")
        self.users.append(user)
        self.storage.save_users(self.users)

    def update_user(self, user_id, **kwargs):
        """
        Update information of a user.

        Args:
            user_id: ID of the user to be updated.
            **kwargs: Dictionary containing attributes to be updated.

        """
        user = self.search_user_by_id(user_id)
        if not user:
            print("User not found.")
            return

        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
            else:
                print(f"Invalid attribute '{key}' for user.")
        self.storage.save_users(self.users)

    def delete_user(self, user_id):
        """
        Delete a user from the collection.

        Args:
            user_id: ID of the user to be deleted.
        """
        user = self.search_user_by_id(user_id)
        if not user:
            print("User not found.")
            return

        self.users.remove(user)
        self.storage.save_users(self.users)

    def list_users(self):
        """
        Get the list of all users.

        Returns:
            List: List of all users.
        """
        return self.users

    def search_user_by_id(self, user_id):
        """
        Search for a user by their ID.

        Args:
            user_id: ID of the user to be searched.

        """
        return next((user for user in self.users if user.user_id == user_id), None)

    def search_users_by_name(self, name):
        """
        Search for users by name.

        Args:
            name: Name of the user(s) to be searched.

        """
        return [user for user in self.users if name.lower() in user.name.lower()]
