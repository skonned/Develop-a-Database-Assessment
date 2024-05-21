#Docstring - Darren Leung - Motorcycle Database Application
#Imports
import sqlite3

#Constants and Variables
DATABASE = "motorcycles.db"

#Functions
def print_all_motorcycle():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    db.close

#Main Code
print_all_motorcycle()