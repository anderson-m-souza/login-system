# Login System

A simple authentication system built for my portfolio and educational purposes. It was written in **Python 3.11**, and I used the **SQLite 3.42** database to store the hashed credentials.

## Login

The file `main.py` will prompt you for your username and password, and do the authentication:

```sh
python main.py
```

The password won't show up while you type. For this I used the `getpass` Python module.

If the credentials match with any one from the database, the program will show a message saying you are authenticated and exit. And if the credentials do not match, it will show a message saying you are not authenticated and exit.

## Sign Up

To add a new user to the database, execute the file `add_user.py`:

```sh
python add_user.py
```

But you will only be able to do this if the username doesn't exist yet. Otherwise, it will show a message saying that this username is already taken, and keep prompting you for a valid username.

The passwords are stored hashed with `SHA256`.

## Setup a Database

The file `setup_db.py` will create a sample `sqlite3` database with some pre-defined users:

```sh
python setup_db.py
```

The credentials are:

|username|password |
|--------|---------|
|`user1` |`pass123`|
|`user2` |`321pass`|
|`user3` |`qwerty` |

If the database already exists, the program will show the name of each table, how many rows they have, and ask if you would like to erase the file and create a new one.

## TODO

- [x] Refactor the code to use classes
- [x] Ask the user to confirm the password when signing up
- [x] Add password requirements
- [ ] Add option to change the password
- [ ] Add option to remove a user
- [ ] Use a better hashing algorithm (Argon2id)
- [ ] Salt and/or pepper the passwords before hashing
