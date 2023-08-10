"""Login

Class used to check if a username exists in the database, and check the
credentials.

Methods:

set_username(username)
    Sets the username to login.

set_password(password)
    Sets the password of the user.

user_exists()
    Check if the username exists in the configured database.

is_valid_credentials()
    Check if the username and password match.
"""

from password_hashing import hash_password
import db_connection


class Login():

    def set_username(self, username):
        self._username = username


    def set_password(self, password):
        self._input_password = password


    def _set_password_salt(self):
        res = db_connection.get_password_salt(self._username)
        salt = res[0]
        self._salt = salt


    def user_exists(self):
        user_exists = db_connection.user_exists(self._username)
        if user_exists:
            return True
        else:
            return False


    def is_valid_credentials(self):

        if self.user_exists():
            self._set_password_salt()
            hashed_password = hash_password(self._input_password, self._salt)
            db_password = db_connection.get_password_hash(self._username)[0]
            passwords_match = db_password == hashed_password

            if passwords_match:
                return True
            else:
                return False

        else:
            return False

