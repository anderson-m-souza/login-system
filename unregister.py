"""Unregister User

Module used to remove an user from the database.
"""

import db_connection
from login import Login


class Unregister(Login):

    def delete_account(self):
        db_connection.delete_user(self._username)
