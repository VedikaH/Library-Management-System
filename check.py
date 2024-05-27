checkouts = []

def checkout_book(user_id, isbn):
    """
    Add a book checkout record to the list of checkouts.

    Args:
        user_id (str): The ID of the user checking out the book.
        isbn (str): The ISBN (International Standard Book Number) of the book being checked out.
    """
    # Input validation: Ensure user_id and isbn are provided and not empty
    if not user_id:
        raise ValueError("User ID cannot be empty")
    if not isbn:
        raise ValueError("ISBN cannot be empty")

    checkouts.append({"user_id": user_id, "isbn": isbn})



