import sqlite3
import hashlib

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    sql_create_users_table = """CREATE TABLE IF NOT EXISTS users (
                                    id integer PRIMARY KEY,
                                    username text NOT NULL,
                                    password text NOT NULL
                                );"""
    try:
        c = conn.cursor()
        c.execute(sql_create_users_table)
    except sqlite3.Error as e:
        print(e)


def create_user(conn, username, password):
    sql = '''INSERT INTO users(username, password) VALUES(?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, (username, password))
    conn.commit()
    return cur.lastrowid


def authenticate_user(conn, username, password):
    sql = '''SELECT * FROM users WHERE username=? AND password=?'''
    cur = conn.cursor()
    cur.execute(sql, (username, password))
    rows = cur.fetchall()
    return len(rows) > 0
