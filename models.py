
class Session:
    our_user = None


class Account:
    def __init__(self, name=None, password=None, email=None):
        self.name = name
        self.password = password
        self.email = email

        self.tasks = {
                      "daily": [],
                      "important": [],
                      "planned": []
                     }