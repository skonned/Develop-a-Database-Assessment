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
    print("\nModel              ", "Year          ", "Engine_Size   ", "Horsepower    ", "Top_Speed     ", "Weight        ", "Price         ", "Description")
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
    print("\nModel              ", "Price         ")
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
    print("\nModel              ", "Manufacturer         ")
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
    print("\nModel              ", "Description       ")
    for motorcycle in results:
        print(f"{motorcycle[0]:<20}{motorcycle[1]}")
    #Loop finished
    db.close


def see_top_speeds():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT model, top_speed FROM motorcycle;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel              ", "Top_Speed      ")
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
    print("\nModel              ", "Year          ", "Engine_Size   ", "Horsepower    ", "Top_Speed     ", "Weight        ", "Price         ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<20}{motorcycle[2]:<15}{motorcycle[3]:<15}{motorcycle[4]:<15}{motorcycle[5]:<15}{motorcycle[6]:<15}{motorcycle[7]:<15}{motorcycle[8]}")
    #Loop finished
    db.close


def see_CBR1000RR():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'CBR1000RR'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel              ", "Year          ", "Engine_Size   ", "Horsepower    ", "Top_Speed     ", "Weight        ", "Price         ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<20}{motorcycle[2]:<15}{motorcycle[3]:<15}{motorcycle[4]:<15}{motorcycle[5]:<15}{motorcycle[6]:<15}{motorcycle[7]:<15}{motorcycle[8]}")
    #Loop finished
    db.close


def see_Ninja_400():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'Ninja 400'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel              ", "Year          ", "Engine_Size   ", "Horsepower    ", "Top_Speed     ", "Weight        ", "Price         ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<20}{motorcycle[2]:<15}{motorcycle[3]:<15}{motorcycle[4]:<15}{motorcycle[5]:<15}{motorcycle[6]:<15}{motorcycle[7]:<15}{motorcycle[8]}")
    #Loop finished
    db.close


def see_Panigale_V4():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'Panigale V4'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel              ", "Year          ", "Engine_Size   ", "Horsepower    ", "Top_Speed     ", "Weight        ", "Price         ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<20}{motorcycle[2]:<15}{motorcycle[3]:<15}{motorcycle[4]:<15}{motorcycle[5]:<15}{motorcycle[6]:<15}{motorcycle[7]:<15}{motorcycle[8]}")
    #Loop finished
    db.close


def see_Street_Glide():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'Street Glide'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel              ", "Year          ", "Engine_Size   ", "Horsepower    ", "Top_Speed     ", "Weight        ", "Price         ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<20}{motorcycle[2]:<15}{motorcycle[3]:<15}{motorcycle[4]:<15}{motorcycle[5]:<15}{motorcycle[6]:<15}{motorcycle[7]:<15}{motorcycle[8]}")
    #Loop finished
    db.close


def see_GSX_R750():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'GSX-R750'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel              ", "Year          ", "Engine_Size   ", "Horsepower    ", "Top_Speed     ", "Weight        ", "Price         ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<20}{motorcycle[2]:<15}{motorcycle[3]:<15}{motorcycle[4]:<15}{motorcycle[5]:<15}{motorcycle[6]:<15}{motorcycle[7]:<15}{motorcycle[8]}")
    #Loop finished
    db.close


def see_S1000RR():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'S1000RR'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel              ", "Year          ", "Engine_Size   ", "Horsepower    ", "Top_Speed     ", "Weight        ", "Price         ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<20}{motorcycle[2]:<15}{motorcycle[3]:<15}{motorcycle[4]:<15}{motorcycle[5]:<15}{motorcycle[6]:<15}{motorcycle[7]:<15}{motorcycle[8]}")
    #Loop finished
    db.close


def see_Street_Triple():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'Street Triple'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel              ", "Year          ", "Engine_Size   ", "Horsepower    ", "Top_Speed     ", "Weight        ", "Price         ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<20}{motorcycle[2]:<15}{motorcycle[3]:<15}{motorcycle[4]:<15}{motorcycle[5]:<15}{motorcycle[6]:<15}{motorcycle[7]:<15}{motorcycle[8]}")
    #Loop finished
    db.close


def see_Duke_390():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'Duke 390'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel              ", "Year          ", "Engine_Size   ", "Horsepower    ", "Top_Speed     ", "Weight        ", "Price         ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<20}{motorcycle[2]:<15}{motorcycle[3]:<15}{motorcycle[4]:<15}{motorcycle[5]:<15}{motorcycle[6]:<15}{motorcycle[7]:<15}{motorcycle[8]}")
    #Loop finished
    db.close


def see_RSV4():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'RSV4'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel              ", "Year          ", "Engine_Size   ", "Horsepower    ", "Top_Speed     ", "Weight        ", "Price         ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<20}{motorcycle[2]:<15}{motorcycle[3]:<15}{motorcycle[4]:<15}{motorcycle[5]:<15}{motorcycle[6]:<15}{motorcycle[7]:<15}{motorcycle[8]}")
    #Loop finished
    db.close


#Main Code
while True:
    user_input = input("\nWhat would you like to do?\n1. Print all motorcycles\n2. See motorcycles from cheapest to most expensive\n3. See motorcycle manufacturers\n4. See motorcycle desriptions\n5. See top speeds\n6. See information on a specific motorycle\n7. Exit\n")
    if user_input == "1":
        print_all_motorcycles()
    elif user_input == "2":
        motorcycles_from_cheapest_to_most_expensive()
    elif user_input == "3":
        see_motorcycle_manufacturers()
    elif user_input == "4":
        see_motorcycle_descriptions()
    elif user_input == "5":
        see_top_speeds()
    elif user_input == "6":
        while True:
            user_input2 = input("\nWhich motorcycle would you like to see?\n1. YZF-R6\n2. CBR1000RR\n3. Ninja 400\n4. Panigale V4\n5. Street Glide\n6. GSX-R750\n7. S1000RR\n8. Street Triple\n9. Duke 390\n10. RSV4\n11. Return to Main Menu\n")
            if user_input2 == "1":
                see_YZF_R6()
            elif user_input2 == "2":
                see_CBR1000RR()
            elif user_input2 == "3":
                see_Ninja_400()
            elif user_input2 == "4":
                see_Panigale_V4()
            elif user_input2 == "5":
                see_Street_Glide()
            elif user_input2 == "6":
                see_GSX_R750()
            elif user_input2 == "7":
                see_S1000RR()
            elif user_input2 == "8":
                see_Street_Triple()
            elif user_input2 == "9":
                see_Duke_390()
            elif user_input2 == "10":
                see_RSV4()
            elif user_input2 == "11":
                break
            else:
                print("That was not an option.\n")
    elif user_input == "7":
        break
    else:
        print("That was not an option.\n")