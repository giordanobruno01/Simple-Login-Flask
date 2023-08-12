import sqlite3

connection = sqlite3.connect('database.db')


with open('user.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (email, passwo) VALUES (?, ?)",
            ('abc@gmail.com', '123')
            )

cur.execute("INSERT INTO users (email, passwo) VALUES (?, ?)",
            ('qwe@gmail.com', '123')
            )

connection.commit()
connection.close()