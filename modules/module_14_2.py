import sqlite3


connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')


cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

#for i in range(1,10):
#    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", f"{i*10}", "1000"))

cursor.execute("DELETE FROM Users WHERE id = 6")


cursor.execute("SELECT COUNT(*) FROM Users")
users_count = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
balance_sum = cursor.fetchone()[0]

#cursor.execute("SELECT AVG(balance) FROM Users")
#avg_balance = cursor.fetchone()[0]
#print(avg_balance)

print(balance_sum / users_count)


connection.commit()
connection.close()