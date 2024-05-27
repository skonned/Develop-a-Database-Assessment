#Docstring - Darren Leung - Motorcycle Database Application
#Imports
import sqlite3


#Constants and Variables
DATABASE = "motorcycles.db"


#Functions
def print_all_motorcycles():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("Model              ", "Year          ", "Engine_Size   ", "Horsepower    ", "Top_Speed     ", "Weight        ", "Price         ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<20}{motorcycle[2]:<15}{motorcycle[3]:<15}{motorcycle[4]:<15}{motorcycle[5]:<15}{motorcycle[6]:<15}{motorcycle[7]:<15}{motorcycle[8]}")
    #Loop finished
    db.close


def motorcycles_from_cheapest_to_most_expensive():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT model, price FROM motorcycle ORDER BY price ASC"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("Model              ", "Price         ")
    for motorcycle in results:
        print(f"{motorcycle[0]:<20}{motorcycle[1]}")
    #Loop finished
    db.close


#Main Code
while True:
    user_input = input("\nWhat would you like to do?\n1. Print all motorcycles\n2. See motorcycles from cheapest to most expensive\n3. Exit\n")
    if user_input == "1":
        print_all_motorcycles()
    elif user_input == "2":
        motorcycles_from_cheapest_to_most_expensive()
    elif user_input == "3":
        break
    else:
        print("That was not an option.\n")