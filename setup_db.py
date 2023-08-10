#!/usr/bin/env python3

import os

import db_connection


def create_db():
    users = [
        # Pa$$w0rd
        ('user1', '79887b2bdb4914a8668cda60e753aee6e0e34cc9c58bfdec0e2f0f5aca185d53', '15e501a12ad0c83c3bddd9625e463ce5f9264e9e52d78bcc20d1bf2897ea323d'),
        # Qwer1234%
        ('user2', 'd443fe7fa318e75369201b0d6590404afba851005cfa5cd50cd0a2b5b9dd967a', 'da2b2ed7b74a8bb4d849458471811411128b1e79655e8affdf47bcc496543275'),
        # asdF!234
        ('user3', '83e81e10d01f33f3a737bb2df147b191e8dee2663942c78570670ed292da33fb', '5bbb0302f02bf72943b4530b19fc6500ff274eea181406ecbfec93c104e05165')
    ]
    db_connection.create_db()
    db_connection.insert_users(users)


def main():
    db_filename = db_connection.get_db_filename()

    if os.path.exists(db_filename):
        print("The database already exists.")
        db_connection.show_tables()
        overwrite = input("Would you like to overwrite it with a new one? ")
        
        if overwrite in 'yes':
            os.remove(db_filename) 
            create_db()
            print("Database overwritten.")
            db_connection.show_tables()
        elif overwrite in 'no':
            print("Aborting database creation.")

    else:
        create_db()
        print("Database created.")
        db_connection.show_tables()


main()

