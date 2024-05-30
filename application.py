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
    sql = "SELECT model, price FROM motorcycle ORDER BY price ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("Model              ", "Price         ")
    for motorcycle in results:
        print(f"{motorcycle[0]:<20}{motorcycle[1]}")
    #Loop finished
    db.close


def see_motorcycle_manufacturers():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT motorcycle.model, manufacturer.name FROM motorcycle JOIN manufacturer ON manufacturer.id=motorcycle.manufacturer_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("Model              ", "Manufacturer         ")
    for motorcycle in results:
        print(f"{motorcycle[0]:<20}{motorcycle[1]}")
    #Loop finished
    db.close


def see_motorcycle_descriptions():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT model, description FROM motorcycle;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("Model              ", "Description       ")
    for motorcycle in results:
        print(f"{motorcycle[0]:<20}{motorcycle[1]}")
    #Loop finished
    db.close


def see_YZF_R6():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'YZF-R6'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("Model              ", "Year          ", "Engine_Size   ", "Horsepower    ", "Top_Speed     ", "Weight        ", "Price         ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<20}{motorcycle[2]:<15}{motorcycle[3]:<15}{motorcycle[4]:<15}{motorcycle[5]:<15}{motorcycle[6]:<15}{motorcycle[7]:<15}{motorcycle[8]}")
    #Loop finished
    db.close


#Main Code
while True:
    user_input = input("\nWhat would you like to do?\n1. Print all motorcycles\n2. See motorcycles from cheapest to most expensive\n3. See motorcycle manufacturers\n4. See motorcycle desriptions\n5. See information on a specific motorycle\n6. Exit\n")
    if user_input == "1":
        print_all_motorcycles()
    elif user_input == "2":
        motorcycles_from_cheapest_to_most_expensive()
    elif user_input == "3":
        see_motorcycle_manufacturers()
    elif user_input == "4":
        see_motorcycle_descriptions()
    elif user_input == "5":
        while True:
            user_input2 = input("\nWhich motorcycle would you like to see?\n1. YZF-R6\n2. Exit\n")
            if user_input2 == "1":
                see_YZF_R6()
            elif user_input2 == "2":
                break
            else:
                print("That was not an option.\n")
    elif user_input == "6":
        break
    else:
        print("That was not an option.\n")