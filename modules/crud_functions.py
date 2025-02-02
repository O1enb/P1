import sqlite3


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
    '''
    )

initiate_db()

#for i in range(1,5):
#    cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?,?,?,?)",(i, f"product{i}", f"description{i}", i * 100))


def get_all_products():
    cursor.execute("SELECT * FROM Products")
    all_products = cursor.fetchall()
    return all_products



connection.commit()
