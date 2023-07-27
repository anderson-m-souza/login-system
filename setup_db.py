import os

import db_connection


def create_db():
    users = [
        ('user1', '9b8769a4a742959a2d0298c36fb70623f2dfacda8436237df08d8dfd5b37374c'),
        ('user2', '2a0ed4a87b24786ecfaf39712985c9054b36dab2df714e5f1cd45ba53dbc6d41'),
        ('user3', '65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5')
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

