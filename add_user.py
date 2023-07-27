from getpass import getpass

from users_helper_functions import sha256_hash
import db_connection


def main():
    while True:
        username = input("Username: ")
        user_exists = db_connection.user_exists(username)
        if user_exists:
            print("This username is taken. Try another one.")
        else:
            break

    password = getpass("Password: ")
    password_hash = sha256_hash(password)

    user = [(username, password_hash)]
    db_connection.insert_users(user)


main()
