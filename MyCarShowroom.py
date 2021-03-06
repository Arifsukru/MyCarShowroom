import sqlite3
import random
import time


def LoggingOut():
    print("\nLogging out", end="")
    for logging_out in range(5):
        print(".", end="")
        time.sleep(1)
    print("\nYou logged out.")


def AddingEmployee():
    print("\nPlease enter employee's information\n")
    x = input("Enter worker's name:          ")
    y = input("Enter worker's gender:        ")
    z = int(input("Enter worker's age:       "))
    a = random.randrange(100000000, 999999999)
    b = input("Enter worker's position:      ")
    c = int(input("Enter worker's salary:    "))
    d = random.randrange(10000, 99999)
    cursor.execute("INSERT INTO workers (name, gender, age, phone, position, salary, number) "
                   "VALUES('{}', '{}', {}, {}, '{}', {}, {})".format(x, y, z, a, b, c, d))
    db.commit()
    cursor.execute("SELECT * FROM workers WHERE number= {}".format(d))
    print("\nOperation completed:")
    for name, gender, age, phone, position, salary, number in cursor:
        print("-" * 40)
        print("Worker's name:           {}".format(name))
        print("Worker's gender:         {}".format(gender))
        print("Worker's age:            {}".format(age))
        print("Worker's phone:          {}".format(phone))
        print("Worker's position:       {}".format(position))
        print("Worker's salary:         {}".format(salary))
        print("Worker's serial number:  {}".format(number))
        print("-" * 40)


def EmployeeList():
    cursor.execute("SELECT * FROM workers")
    for name, gender, age, position, phone, salary, number in cursor:
        print("Worker's name:           {}".format(name))
        print("Worker's gender:         {}".format(gender))
        print("Worker's age:            {}".format(age))
        print("Worker's position:       {}".format(position))
        print("Phone number:            {}".format(phone))
        print("Worker's salary:         {}".format(salary))
        print("Worker's serial number:  {}".format(number))
        print("-" * 50)


def FireEmployee():
    print("\nYou'll fire a person.")
    serial_number = input("Please enter serial number of worker that you want to remove: ")
    cursor.execute("DELETE FROM workers WHERE number = {}".format(serial_number))
    db.commit()
    print("\nPlease wait", end="")
    for removing in range(3):
        print(".", end="")
        time.sleep(1)
    print("\nRemoving operation is completed.")


def CarList():
    cursor.execute("SELECT * FROM cars")
    for brand, model, year, price, number, rent in cursor:
        print("Car's brand:     {}".format(brand))
        print("Car's model:     {}".format(model))
        print("Produced year:   {}".format(year))
        print("Car's price:     {}".format(price))
        print("Serial number:   {}".format(number))
        print("For rent:        {}".format(rent))
        print("-" * 50)


def AddingCar():
    print("\nPlease enter car's data\n")
    x = input("Enter brand: ")
    y = input("Enter model: ")
    z = int(input("Enter year: "))
    t = int(input("Enter price: "))
    q = random.randrange(10000, 99999)
    p = str("Available")
    cursor.execute("INSERT INTO cars (brand, model, year, price, number, rent) "
                   "VALUES('{}', '{}', {}, {}, {}, '{}')".format(x, y, z, t, q, p))
    db.commit()


def RemoveCar():
    print("\nYou'll remove a car from system.")
    serial_number = input("Please enter serial number of car that you want to remove: ")
    cursor.execute("DELETE FROM cars WHERE number = {}".format(serial_number))
    db.commit()
    print("\nPlease wait", end="")
    for removing in range(3):
        print(".", end="")
        time.sleep(1)
    print("\nRemoving operation is completed.")


def AvailableCarList():
    cursor.execute("SELECT * FROM cars WHERE rent='Available'")
    for brand, model, year, price, number, rent in cursor:
        print("Car's brand:     {}".format(brand))
        print("Car's model:     {}".format(model))
        print("Produced year:   {}".format(year))
        print("Car's price:     {}".format(price))
        print("Serial number:   {}".format(number))
        print("For rent:        {}".format(rent))
        print("-" * 50)


def RentingCar():
    serial_number = input("Enter serial number of the car that you want to rent: ")
    rent_date = input("Enter the date that renting will be finish: ")
    cursor.execute("UPDATE cars SET rent='Not Available until {}' "
                   "WHERE number={}".format(rent_date, serial_number))
    db.commit()


def ReturningCar():
    serial_number = \
        input("Enter the serial number of car that you want to make it available for renting: ")
    cursor.execute("UPDATE cars SET rent='Available' WHERE number={}".format(serial_number))
    db.commit()


def SellingCar():
    serial_number = input("\nPlease enter serial number of car that sold: ")
    cursor.execute("INSERT INTO sold SELECT * FROM cars WHERE number={}".format(serial_number))
    cursor.execute("DELETE FROM cars WHERE number={}".format(serial_number))
    db.commit()



db = sqlite3.connect("MyCarShowroom.db")
cursor = db.cursor()

db.execute("CREATE TABLE IF NOT EXISTS workers "
           "(name TEXT, gender TEXT, age INTEGER, phone INTEGER, position TEXT, salary INTEGER, number INTEGER)")
db.execute("CREATE TABLE IF NOT EXISTS cars "
           "(brand TEXT, model TEXT, year INTEGER, price INTEGER,"
           " number INTEGER, rent TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS sold "
           "(brand TEXT, model TEXT, year INTEGER, price INTEGER,"
           " number INTEGER, rent TEXT)")


print("\nSystem opened.")
while True:
    print("\n1. ADMIN LOGIN\n2. EMPLOYEE LOGIN\n3. EXIT SYSTEM")
    login_choice = input("\nWhat would you like to do: ")
    if login_choice == "1":
        while True:
            print("\n1.Adding employee\n2.Removing employee\n3.List of employees\n4.List of cars\n5.Logout")
            admin_choice = input("\nWhat would you like to do? ")
            if admin_choice == "1":
                AddingEmployee()
                continue_operation = input("\nWould you like to do another operation? ")
                positive = ["Yes", "yes", "YES", "I do", "ı do"]
                negative = ["No", "no", "NO", "I don't", "I do not", "ı dont", "ı do not"]
                if continue_operation in positive:
                    pass
                elif continue_operation in negative:
                    LoggingOut()
                    break
            elif admin_choice == "2":
                EmployeeList()
                FireEmployee()
                continue_operation = input("\nWould you like to do another operation? ")
                positive = ["Yes", "yes", "YES", "I do", "ı do"]
                negative = ["No", "no", "NO", "I don't", "I do not", "ı dont", "ı do not"]
                if continue_operation in positive:
                    pass
                elif continue_operation in negative:
                    LoggingOut()
                    break
            elif admin_choice == "3":
                EmployeeList()
                continue_operation = input("\nWould you like to do another operation? ")
                positive = ["Yes", "yes", "YES", "I do", "ı do"]
                negative = ["No", "no", "NO", "I don't", "I do not", "ı dont", "ı do not"]
                if continue_operation in positive:
                    pass
                elif continue_operation in negative:
                    LoggingOut()
                    break
            elif admin_choice == "4":
                CarList()
                continue_operation = input("\nWould you like to do another operation? ")
                positive = ["Yes", "yes", "YES", "I do", "ı do"]
                negative = ["No", "no", "NO", "I don't", "I do not", "ı dont", "ı do not"]
                if continue_operation in positive:
                    pass
                elif continue_operation in negative:
                    LoggingOut()
                    break
            elif admin_choice == "5":
                LoggingOut()
                break
    elif login_choice == "2":
        while True:
            print("\n1.Adding car\n2.Removing car\n3.Renting car\n4.Selling car\n5.Logout\n")
            employee_choice = input("\nWhat would you like to do: ")
            if employee_choice == "1":
                AddingCar()
                continue_operation = input("\nWould you like to do another operation? ")
                positive = ["Yes", "yes", "YES", "I do", "ı do"]
                negative = ["No", "no", "NO", "I don't", "I do not", "ı dont", "ı do not"]
                if continue_operation in positive:
                    pass
                elif continue_operation in negative:
                    LoggingOut()
                    break
            elif employee_choice == "2":
                CarList()
                RemoveCar()
                continue_operation = input("\nWould you like to do another operation? ")
                positive = ["Yes", "yes", "YES", "I do", "ı do"]
                negative = ["No", "no", "NO", "I don't", "I do not", "ı dont", "ı do not"]
                if continue_operation in positive:
                    pass
                elif continue_operation in negative:
                    LoggingOut()
                    break
            elif employee_choice == "3":
                print("\n1.Start of a renting date\n2.Expiration of a renting date")
                while True:
                    rent_choose = ""
                    rent_choose = input("What would you like to do:")
                    if rent_choose == "1":
                        AvailableCarList()
                        RentingCar()
                        break
                    elif rent_choose == "2":
                        CarList()
                        ReturningCar()
                        break
                    else:
                        pass
                continue_operation = input("\nWould you like to do another operation? ")
                positive = ["Yes", "yes", "YES", "I do", "ı do"]
                negative = ["No", "no", "NO", "I don't", "I do not", "ı dont", "ı do not"]
                if continue_operation in positive:
                    pass
                elif continue_operation in negative:
                    LoggingOut()
                    break
            elif employee_choice == "4":
                AvailableCarList()
                SellingCar()
                continue_operation = input("\nWould you like to do another operation? ")
                positive = ["Yes", "yes", "YES", "I do", "ı do"]
                negative = ["No", "no", "NO", "I don't", "I do not", "ı dont", "ı do not"]
                if continue_operation in positive:
                    pass
                elif continue_operation in negative:
                    LoggingOut()
                    break
            elif employee_choice == "5":
                LoggingOut()
                break
    elif login_choice == "3":
        print("\nClosing system", end="")
        for logging_out in range(5):
            print(".", end="")
            time.sleep(1)
        print("\nSystem closed.")
        break
    else:
        pass
