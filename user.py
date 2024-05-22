""" users = []

def add_user(name, user_id):
    users.append({"name": name, "user_id": user_id}) """

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f"User(name={self.name}, user_id={self.user_id})"

