import re

from users_helper_functions import hash_password, generate_salt
import db_connection


class Signup():


    def user_exists(self, username):
        user_exists = db_connection.user_exists(username)
        return user_exists


    def set_username(self, username):
        self._username = username


    def _set_salt(self):
        self._salt = generate_salt()


    def set_password(self, password):
        self._set_salt()
        hashed_password = hash_password(password, self._salt)
        self._input_password = hashed_password


    def add_user(self):
        user = [(self._username, self._input_password, self._salt)]
        db_connection.insert_users(user)


    def password_is_strong(self, password):

        if len(password) < 8:
            return False
        elif not self._has_lowercase_letter(password):
            return False
        elif not self._has_uppercase_letter(password):
            return False
        elif not self._has_number(password):
            return False
        elif not self._has_special_character(password):
            return False
        else:
            return True


    def _has_lowercase_letter(self, password):
        regex_search = re.search(r'[a-z]', password)
        has_uppercase = bool(regex_search)
        if has_uppercase:
            return True
        else:
            return False


    def _has_uppercase_letter(self, password):
        regex_search = re.search(r'[A-Z]', password)
        has_uppercase = bool(regex_search)
        if has_uppercase:
            return True
        else:
            return False


    def _has_number(self, password):
        regex_search = re.search(r'[0-9]', password)
        has_number = bool(regex_search)
        if has_number:
            return True
        else:
            return False


    def _has_special_character(self, password):
        for c in password:
            if c in "!@#$%¨&*()-_=+{}[]\\\ |/?:;.>,<^~`´":
                return True

        return False

