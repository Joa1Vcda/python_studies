'''setter'''

class Connection:
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        # setter
        self.user = user

    def set_passwords(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = Connection()
        connection.user = user
        connection.password = password
        return connection


# c1 = Connection()
# c1.user = "João"
# c1.password = "1234"
# print(c1.__dict__)
c2 = Connection.create_with_auth("João Vitor", 1234)
print(c2.__dict__)
