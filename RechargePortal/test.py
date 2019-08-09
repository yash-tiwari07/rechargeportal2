import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")
cur = conn.cursor()
print(cur.execute("SELECT * FROM customers").rowcount)


