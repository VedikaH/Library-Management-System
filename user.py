
class User:
    def __init__(self, name, user_id):
        """
        Initialize a User object.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.
        """
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f"User(name={self.name}, user_id={self.user_id})"
