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
    #loop through all the results
    print("Model              ", "Year          ", "Engine_Size   ", "Horsepower    ", "Top_Speed     ", "Weight        ", "Price         ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<20}{motorcycle[2]:<15}{motorcycle[3]:<15}{motorcycle[4]:<15}{motorcycle[5]:<15}{motorcycle[6]:<15}{motorcycle[7]:<15}{motorcycle[8]}")
    #loop finished
    db.close

#Main Code
print_all_motorcycle()