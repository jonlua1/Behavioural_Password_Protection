
class Account():
    def __init__(self, account_name="", user_name="", password=""):
        self._account_id = 0
        self._account_name = account_name
        self._user_name = user_name
        self._password = password

    @property
    def account_id(self):
        return self._account_id
    @property
    def account_name(self):
        return self._account_name

    @property
    def user_name(self):
        return self._user_name

    @property
    def password(self):
        return self._password
