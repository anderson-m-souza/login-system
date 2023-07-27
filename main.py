from getpass import getpass

from users_helper_functions import sha256_hash
import db_connection


def is_valid_credentials(username, input_password):
    res = db_connection.get_password_hash(username)

    hashed_db_password = ''
    if res != None:
        hashed_db_password = res[0]
    else:
        return False

    hashed_input_password = sha256_hash(input_password)
    if hashed_db_password == hashed_input_password:
        return True
    else:
        return False


def main():
    username = input("Username: ")
    password = getpass("Password: ")

    if is_valid_credentials(username, password):
        print("Authenticated")
    else:
        print("Not authenticated")


main()

