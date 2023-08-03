from users_helper_functions import hash_password
import db_connection


class Signup():

    def user_exists(self, username):
        user_exists = db_connection.user_exists(username)
        return user_exists


    def set_username(self, username):
        self._username = username


    def set_password(self, password):
        hashed_password = hash_password(password)
        self._input_password = hashed_password


    def add_user(self):
        user = [(self._username, self._input_password)]
        db_connection.insert_users(user)

