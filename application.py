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
    print("\nModel              ", "Year       ", "Engine_Size (CC)   ", "Horsepower (hp)    ", "Top_Speed (kph)    ", "Weight (kg)   ", "Price (NZD)      ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<20}{motorcycle[2]:<12}{motorcycle[3]:<20}{motorcycle[4]:<20}{motorcycle[5]:<20}{motorcycle[6]:<15}{motorcycle[7]:<18}{motorcycle[8]}")
    #Loop finished
    db.close


def motorcycles_ordered_by_price():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"SELECT model, price FROM motorcycle ORDER BY price ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel              ", "Price (NZD)        ")
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
    print("\nModel              ", "Top_Speed (kph)     ")
    for motorcycle in results:
        print(f"{motorcycle[0]:<20}{motorcycle[1]}")
    #Loop finished
    db.close


def see_horsepowers():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT model, horsepower FROM motorcycle;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel              ", "Horsepower (hp)     ")
    for motorcycle in results:
        print(f"{motorcycle[0]:<20}{motorcycle[1]}")
    #Loop finished
    db.close


def see_weights():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT model, weight FROM motorcycle;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel              ", "Weight (kg)   ")
    for motorcycle in results:
        print(f"{motorcycle[0]:<20}{motorcycle[1]}")
    #Loop finished
    db.close


def see_engine_sizes():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT model, engine_size FROM motorcycle;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel              ", "Engine_Size (CC)  ")
    for motorcycle in results:
        print(f"{motorcycle[0]:<20}{motorcycle[1]}")
    #Loop finished
    db.close


def see_years():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT model, year FROM motorcycle;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel              ", "Year  ")
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
    print("\nModel         ", "Year       ", "Engine_Size (CC)   ", "Horsepower (hp)    ", "Top_Speed (kph)    ", "Weight (kg)   ", "Price (NZD)      ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<15}{motorcycle[2]:<12}{motorcycle[3]:<20}{motorcycle[4]:<20}{motorcycle[5]:<20}{motorcycle[6]:<15}{motorcycle[7]:<18}{motorcycle[8]}")
    #Loop finished
    db.close


def see_CBR1000RR():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'CBR1000RR'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel          ", "Year       ", "Engine_Size (CC)   ", "Horsepower (hp)    ", "Top_Speed (kph)    ", "Weight (kg)   ", "Price (NZD)      ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<16}{motorcycle[2]:<12}{motorcycle[3]:<20}{motorcycle[4]:<20}{motorcycle[5]:<20}{motorcycle[6]:<15}{motorcycle[7]:<18}{motorcycle[8]}")
    #Loop finished
    db.close


def see_Ninja_400():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'Ninja 400'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel           ", "Year       ", "Engine_Size (CC)   ", "Horsepower (hp)    ", "Top_Speed (kph)    ", "Weight (kg)   ", "Price (NZD)      ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<17}{motorcycle[2]:<12}{motorcycle[3]:<20}{motorcycle[4]:<20}{motorcycle[5]:<20}{motorcycle[6]:<15}{motorcycle[7]:<18}{motorcycle[8]}")
    #Loop finished
    db.close


def see_Panigale_V4():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'Panigale V4'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel             ", "Year       ", "Engine_Size (CC)   ", "Horsepower (hp)    ", "Top_Speed (kph)    ", "Weight (kg)   ", "Price (NZD)      ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<19}{motorcycle[2]:<12}{motorcycle[3]:<20}{motorcycle[4]:<20}{motorcycle[5]:<20}{motorcycle[6]:<15}{motorcycle[7]:<18}{motorcycle[8]}")
    #Loop finished
    db.close


def see_Street_Glide():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'Street Glide'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel              ", "Year       ", "Engine_Size (CC)   ", "Horsepower (hp)    ", "Top_Speed (kph)    ", "Weight (kg)   ", "Price (NZD)      ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<20}{motorcycle[2]:<12}{motorcycle[3]:<20}{motorcycle[4]:<20}{motorcycle[5]:<20}{motorcycle[6]:<15}{motorcycle[7]:<18}{motorcycle[8]}")
    #Loop finished
    db.close


def see_GSX_R750():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'GSX-R750'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel          ", "Year       ", "Engine_Size (CC)   ", "Horsepower (hp)    ", "Top_Speed (kph)    ", "Weight (kg)   ", "Price (NZD)      ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<16}{motorcycle[2]:<12}{motorcycle[3]:<20}{motorcycle[4]:<20}{motorcycle[5]:<20}{motorcycle[6]:<15}{motorcycle[7]:<18}{motorcycle[8]}")
    #Loop finished
    db.close


def see_S1000RR():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'S1000RR'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel         ", "Year       ", "Engine_Size (CC)   ", "Horsepower (hp)    ", "Top_Speed (kph)    ", "Weight (kg)   ", "Price (NZD)      ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<15}{motorcycle[2]:<12}{motorcycle[3]:<20}{motorcycle[4]:<20}{motorcycle[5]:<20}{motorcycle[6]:<15}{motorcycle[7]:<18}{motorcycle[8]}")
    #Loop finished
    db.close


def see_Street_Triple():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'Street Triple'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel              ", "Year       ", "Engine_Size (CC)   ", "Horsepower (hp)    ", "Top_Speed (kph)    ", "Weight (kg)   ", "Price (NZD)      ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<20}{motorcycle[2]:<12}{motorcycle[3]:<20}{motorcycle[4]:<20}{motorcycle[5]:<20}{motorcycle[6]:<15}{motorcycle[7]:<18}{motorcycle[8]}")
    #Loop finished
    db.close


def see_Duke_390():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'Duke 390'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel          ", "Year       ", "Engine_Size (CC)   ", "Horsepower (hp)    ", "Top_Speed (kph)    ", "Weight (kg)   ", "Price (NZD)      ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<16}{motorcycle[2]:<12}{motorcycle[3]:<20}{motorcycle[4]:<20}{motorcycle[5]:<20}{motorcycle[6]:<15}{motorcycle[7]:<18}{motorcycle[8]}")
    #Loop finished
    db.close


def see_RSV4():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM motorcycle WHERE model = 'RSV4'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop through all the results
    print("\nModel        ", "Year       ", "Engine_Size (CC)   ", "Horsepower (hp)    ", "Top_Speed (kph)    ", "Weight (kg)   ", "Price (NZD)      ", "Description")
    for motorcycle in results:
        print(f"{motorcycle[1]:<14}{motorcycle[2]:<12}{motorcycle[3]:<20}{motorcycle[4]:<20}{motorcycle[5]:<20}{motorcycle[6]:<15}{motorcycle[7]:<18}{motorcycle[8]}")
    #Loop finished
    db.close


#Main Code
while True:
    user_input = input("\nWhat would you like to do?\n1. Print all motorcycles\n2. See motorcycles ordered by price\n3. See motorcycle manufacturers\n4. See motorcycle desriptions\n5. See top speeds\n6. See horsepowers\n7. See weights\n8. See engine sizes\n9. See years\n10. See information on a specific motorcycle\n11. Exit\n")
    if user_input == "1":
        print_all_motorcycles()
    elif user_input == "2":
        motorcycles_ordered_by_price()
    elif user_input == "3":
        see_motorcycle_manufacturers()
    elif user_input == "4":
        see_motorcycle_descriptions()
    elif user_input == "5":
        see_top_speeds()
    elif user_input == "6":
        see_horsepowers()
    elif user_input == "7":
        see_weights()
    elif user_input == "8":
        see_engine_sizes()
    elif user_input == "9":
        see_years()
    elif user_input == "10":
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
    elif user_input == "11":
        break
    else:
        print("That was not an option.\n")