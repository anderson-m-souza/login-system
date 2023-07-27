import sqlite3
from configparser import ConfigParser


def get_connection():
    db_filename = get_db_filename()
    connection = sqlite3.connect(db_filename)
    return connection


def get_password_hash(username):
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT password_hash FROM users WHERE username='{}'".format(username))
    res = cur.fetchone()
    cur.close()
    return res


def create_db():
    con = get_connection()
    cur = con.cursor()
    cur.execute("CREATE TABLE users (username VARCHAR, password_hash VARCHAR)")
    con.commit()
    cur.close()


def insert_users(users):
    con = get_connection()
    cur = con.cursor()
    cur.executemany("INSERT INTO users VALUES (?, ?)", users)
    con.commit()
    cur.close()


def user_exists(username):
    con = get_connection()
    cur = con.cursor()
    sql = "SELECT username FROM users WHERE username='{}'".format(username)
    cur.execute(sql)
    res = cur.fetchone()
    cur.close()

    if res == None:
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
    names = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

    for name in names.fetchall():
        rows = cur.execute("SELECT COUNT(*) FROM {}".format(name[0]))
        print("Table: {}. Rows: {}.".format(name[0], rows.fetchone()[0]))

    cur.close()

