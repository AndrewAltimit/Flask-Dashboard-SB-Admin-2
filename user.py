from flask_login import UserMixin

class UserNotFoundError(Exception):
    pass

class User(UserMixin):

    USERS = {
        # username: password
        'john': 'doe',
        'mary': 'jane'
    }

    id = "john"
    password = "doe"

    def __init__(self, id):
        if not id in self.USERS:
            raise UserNotFoundError()
        self.id = id
        self.password = self.USERS[id]

    @classmethod
    def get(self_class, id):
        try:
            return self_class(id)
        except UserNotFoundError:
            return None