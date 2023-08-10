"""Database Connection

Functions used to manipulate the database and get information from it.

Functions:

get_password_hash(username)
    Returns the hashed password for the username.

get_password_salt(username)
    Returns the salt used in the user's password.

create_db()
    Creates a database, with the users table.

insert_users(users)
    Insert users to the configured table.

user_exists(username)
    Queries the database for the username. And returns if it is present or not.

get_db_filename()
    Returns the database filename configured in the config file.

show_tables()
    Prints the name of the tables and how many rows each one have.
"""

__author__ = 'Anderson M Souza'
__version__ = '0.0.1'
__license__ = 'unlicensed'

import sqlite3
from configparser import ConfigParser


def get_connection():
    db_filename = get_db_filename()
    connection = sqlite3.connect(db_filename)
    return connection


def get_password_hash(username):
    con = get_connection()
    cur = con.cursor()
    sql = "SELECT password_hash FROM users WHERE username='{}'".format(username)
    cur.execute(sql)
    res = cur.fetchone()
    cur.close()
    return res


def get_password_salt(username):
    con = get_connection()
    cur = con.cursor()
    sql = "SELECT password_salt FROM users WHERE username='{}'".format(username)
    cur.execute(sql)
    res = cur.fetchone()
    cur.close()
    return res


def create_db():
    con = get_connection()
    cur = con.cursor()
    sql = """
        CREATE TABLE users (
            username VARCHAR,
            password_hash VARCHAR,
            password_salt VARCHAR
        )
    """
    cur.execute(sql)
    con.commit()
    cur.close()


def insert_users(users):
    con = get_connection()
    cur = con.cursor()
    sql = 'INSERT INTO users VALUES (?, ?, ?)'
    cur.executemany(sql, users)
    con.commit()
    cur.close()


def delete_user(username):
    con = get_connection()
    cur = con.cursor()
    sql = "DELETE FROM users WHERE username='{}'".format(username)
    cur.execute(sql)
    con.commit()
    cur.close()


def user_exists(username):
    con = get_connection()
    cur = con.cursor()
    sql = "SELECT username FROM users WHERE username='{}'".format(username)
    cur.execute(sql)
    res = cur.fetchone()
    cur.close()

    if res is None:
        return False
    else:
        return True


def get_db_filename():
    config = ConfigParser()
    config.read('config.ini')
    db_config = config['DATABASE']
    db_filename = db_config['filename']
    return db_filename


def show_tables():
    con = get_connection()
    cur = con.cursor()
    sql_select = "SELECT name FROM sqlite_master WHERE type='table';"
    names = cur.execute(sql_select)

    for name in names.fetchall():
        sql_count = 'SELECT COUNT(*) FROM {}'.format(name[0])
        rows = cur.execute(sql_count)
        print('Table: {}. Rows: {}.'.format(name[0], rows.fetchone()[0]))

    cur.close()

