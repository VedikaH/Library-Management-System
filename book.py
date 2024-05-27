class Book:
    def __init__(self, title, author, isbn, available=True):

        """
        Initialize a Book object with the provided title, author, ISBN, and availability.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN (International Standard Book Number) of the book.
            available (bool, optional): The availability status of the book. Default is True.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, isbn={self.isbn}, available={self.available})"
