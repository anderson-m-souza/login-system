import os

import db_connection


def create_db():
    users = [
        # Pa$$w0rd
        ('user1', '97c94ebe5d767a353b77f3c0ce2d429741f2e8c99473c3c150e2faa3d14c9da6', '15e501a12ad0c83c3bddd9625e463ce5f9264e9e52d78bcc20d1bf2897ea323d'),
        # Qwer1234%
        ('user2', 'd680cb7b13e71d24791855edea4983f8a6c97e0cd666bff10908c1a309ba4e21', 'da2b2ed7b74a8bb4d849458471811411128b1e79655e8affdf47bcc496543275'),
        # asdF!234
        ('user3', '0fe88cec2272917529ad607668a9029a17aeb95ad68cfa059375d7db6d00e33a', '5bbb0302f02bf72943b4530b19fc6500ff274eea181406ecbfec93c104e05165')
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

