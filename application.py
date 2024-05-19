import sqlite3

db = sqlite3.connect("motorcycles.db")
cursor = db.cursor()
sql = "SELECT * FROM motorcycle;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close