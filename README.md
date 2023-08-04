# Login System

A simple authentication system built for my portfolio and educational purposes. It was written in **Python 3.11**, and I used the **SQLite 3.42** database to store the credentials.

The file `main.py`:

```sh
python main.py
```

will show the menu:

```
Authentication Program
Chose an option:
(1) Sign in
(2) Sign up
(q) Quit
Your choice:
```

## Sign in

If the credentials match with any from the database, the program will show a message saying you are authenticated and exit. If the credentials do not match, it will show a message saying you are not authenticated and exit.

## Sign Up

The program will ask for a new username. If the username is already taken, it will show a message saying that this username is already taken, and keep prompting you for a valid username.

Then it will ask for a password. If the password doesn't fulfil all requirements, the program will show the following message:

```
This password isn't strong enough.
Please insert a password that meet these requirements:
- At least 8 characters.
- At least one numeric digit.
- At least one uppercase letter.
- At least one lowercase letter.
- At least one special character.
```

And ask for the password again.

Finally, the user has to confirm the password. If it is not correct, they will have to type a valid password again, then confirm the password.

## Setup a Database

The file `setup_db.py` will create a sample `sqlite3` database with some pre-defined users:

```sh
python setup_db.py
```

The credentials are:

| username | password  |
|----------|-----------|
|`user1`   |`Pa$$w0rd` |
|`user2`   |`Qwer1234%`|
|`user3`   |`asdF!234` |

If the database already exists, the program will show the name of each table, how many rows they have, and ask if you would like to erase the file and create a new one.

This is only for testing.

## Password Security

I used the function `getpass` from the module `getpass` to prompt the user for the password. So it is obfuscated while the user type it.

The passwords are stored **salted** and **hashed**.

The salt is generated with the module `secrets`, so each password has its own salt. And the salt is stored in a column next to the salted and hashed password.

For now, the hash algorithm is `SHA256`, provided by the module `hashlib`. But I will change it to **Argon2id**. Just need to do some research first.

## TODO

- [x] Refactor the code to use classes
- [x] Ask the user to confirm the password when signing up
- [x] Add password requirements
- [ ] Add option to change the password
- [ ] Add option to remove a user
- [ ] Use a better hashing algorithm (Argon2id)
- [x] Salt the passwords before hashing
