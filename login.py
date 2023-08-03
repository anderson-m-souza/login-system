from users_helper_functions import hash_password
import db_connection


class Login():

    def __init__(self):
        pass

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        hashed_password = hash_password(password)
        self._input_password = hashed_password

    def is_valid_credentials(self):
        res = db_connection.get_password_hash(self._username)

        db_password = ''
        if res != None:
            db_password = res[0]
        else:
            return False

        if db_password == self._input_password:
            return True
        else:
            return False

