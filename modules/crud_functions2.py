import sqlite3
from distutils.util import execute

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')


def add_user(username, email, age):
    if is_included(username):
        return
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)", (username, email, age, 1000))
    connection.commit()


def is_included(username):
    cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    return cursor.fetchone() is not None

initiate_db()

#for i in range(1,5):
#    cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?,?,?,?)",(i, f"product{i}", f"description{i}", i * 100))


def get_all_products():
    cursor.execute("SELECT * FROM Products")
    all_products = cursor.fetchall()
    return all_products



connection.commit()
