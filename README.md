# Login System

A simple authentication system built for my portfolio and educational purposes. It was written in **Python 3.11**, and I used the **SQLite 3.42** database to store the credentials.

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

## Delete Account

To delete an account, first the program asks the user to login. If the credentials match, it prompts the user to confirm they really want to delete the account.

If the answer is **yes**, the entry is deleted from the database. If it is **no**, the program exits.

## Setup a Database

The script `setup_db.py` will create a sample `sqlite3` database with some pre-defined users. The credentials are:

| username | password  |
|----------|-----------|
|`user1`   |`Pa$$w0rd` |
|`user2`   |`Qwer1234%`|
|`user3`   |`asdF!234` |

If the database already exists, the program will show the name of each table, how many rows they have, and ask if you would like to erase the file and create a new one.

## Password Security

I used the function `getpass` from the module [`getpass`](https://docs.python.org/3/library/getpass.html#module-getpass) to obfuscate the password while prompting the user for it.

The passwords are stored **salted** and **hashed**.

The salt is generated with the module [`secrets`](https://docs.python.org/3/library/secrets.html#module-secrets). Each password has its own salt. And it is stored in a column next to the salted and hashed password.

The hash algorithm is [Argon2](https://en.wikipedia.org/wiki/Argon2), provided by the module [`pyargon2`](https://pypi.org/project/pyargon2/). It's configured as recommended in the [OWASP's Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html):

- Argon2id variant
- 19MiB of memory
- Iteration count of 2
- 1 degree of parallelism

## How to Run (Linux)

1. Create a virtual environment:

```sh
python -m venv venv
```

2. Activate the virtual environment:

```sh
source venv/bin/activate
```

3. Install the requirements:

```sh
pip install -r requirements.txt
```

4. Set up the database:

```sh
./setup_db.py
```

5. Run the script `main.py`:

```sh
./main.py
```

6. Choose an option from the menu and hit `Enter`:

```
Authentication Program
Choose an option:
(1) Sign in
(2) Sign up
(3) Delete Account
(q) Quit
Your choice:
```

7. You'll know what to do next.

## TODO

- [x] Refactor the code to use classes
- [x] Ask the user to confirm the password when signing up
- [x] Add password requirements
- [ ] Add option to change the password
- [x] Add option to remove a user
- [x] Use a better hashing algorithm (Argon2id)
- [x] Salt the passwords before hashing
- [x] Use Docstrings to document the code
- [x] Use the PEP 8 style guide
- [x] Add metadata
