import re


class UserSecurity:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate_password(self):

        if len(self.password) < 6:
            return False

        if not re.search(r"[A-Z]", self.password):
            return False

        if not re.search(r"\d", self.password):
            return False

        return True

    def authenticate(self, entered_password):
        return self.password == entered_password