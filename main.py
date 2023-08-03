from getpass import getpass

from login import Login
from signup import Signup


def print_header():
    print("Authentication Program")


def print_menu():
    print("""Chose an option:
(1) Sign in
(2) Sign up
(q) Quit""")


def ask_to_signin():
    while True:
        signin = input("Would you like to sign in now? [yes/no]: ")
        if signin in "yes":
            login()
            break
        elif signin in "no":
            break


def login():
    username = input("Username: ")
    password = getpass("Password: ")

    authentication = Login()
    authentication.set_username(username)
    authentication.set_password(password)

    if authentication.is_valid_credentials():
        print("Authenticated")
    else:
        print("Not authenticated")


def signup():
    registration = Signup()

    while True:
        username = input("Username: ")
        user_exists = registration.user_exists(username)
        if user_exists:
            print("This username is taken. Try another one.")
        else:
            registration.set_username(username)
            break

    while True:
        password = getpass("Password: ")
        password_confirmation = getpass("Confirm the password: ")

        if password == password_confirmation:
            break
        else:
            print("Passwords don't match, please try again.")

    registration.set_password(password)
    registration.add_user()


def main():
    print_header()

    while True:
        print_menu()
        choice = input("Your choice: ")

        if choice in "12q":
            if choice == '1':
                login()
            elif choice == '2':
                signup()
                ask_to_signin()

            print("Exiting authentication...")
            break


if __name__ == "__main__":
    main()

