#!/usr/bin/env python3
"""Login System

The main script that will prompt the user to sign in or register. This is an
interface to the classes and functions of the program.
"""

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


def get_valid_password(registration):
    while True:
        password = ''

        while True:
            password = getpass("Password: ")
            if registration.password_is_strong(password):
                break
            else:
                print("This password isn't strong enough.")
                print("Please insert a password that meet these requirements:")
                print("- At least 8 characters.")
                print("- At least one numeric digit.")
                print("- At least one uppercase letter.")
                print("- At least one lowercase letter.")
                print("- At least one special character.")

        password_confirmation = getpass("Confirm the password: ")

        if password == password_confirmation:
            return password
        else:
            print("Passwords don't match, please try again.")


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

    password = get_valid_password(registration)

    registration.set_password(password)
    registration.add_user()


def ask_to_signin():
    while True:
        signin = input("Would you like to sign in now? [yes/no]: ")
        if signin in "yes":
            login()
            break
        elif signin in "no":
            break


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

