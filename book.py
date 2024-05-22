class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, isbn={self.isbn}, available={self.available})"
