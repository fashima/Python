import os

cars_list = [
 
    ("Chevrolet Tracker", 120),
    ("Chevrolet Onix", 90),
    ("Chevrolet Spin", 150),
    ("Fiat Uno", 60),
    ("Fiat Mobi", 70)
]

rent_list = [
    
]

def show_car_list(car_list):
    for i, car in enumerate(car_list):
        print(f"[{i}] {car[0]} - R$ {car[1]} /day.")


while True:
    os.system("cls")
    print("==========")
    print("Welcome to Car System ERP")
    print("==========")
    
    main_menu = {
        "0": "Show Portfolio",
        "1": "Rent a Car",
        "2": "Return a Car",
        "3": "Exit"
    }

    i = 0
    for keys, names in main_menu.items():
        print(f"{keys} - {names}")
        i += 1
    print("")
    print("Please, choose an option")
    option = int(input())
    
    os.system("cls")
    if option == 0:
        show_car_list(cars_list)
        
    elif option == 1:
        show_car_list(cars_list)
        print("================")
        print("Enter the car code to select a vehicle to rent: ")
        id_car = int(input())
        print("How long do you want to rent the car for: ")
        days = int(input())
        os.system("cls")
        
        print(f"You decided to rent the {cars_list[id_car][0]} for {days} days")
        print(f"You will pay $ {days * cars_list[id_car][1]}. Do you want to continue?")
        print("0 - YES | 1 - NO")
        rent_confirm = int(input())
        
        if rent_confirm == 0:
            print(f"Congrats! You rent a {cars_list[id_car][0]} for {days} days.")
            rent_list.append(cars_list.pop(id_car))
    
    elif option == 2:
        
        if len(rent_list) == 0:
            print("All vehicles are in stock. There has been no rent so far.")
        else:
            print("This is the list of rental vehicles, which one was returned?")
            show_car_list(rent_list)
            print("")
            print("Enter the ID: ")
            id_car = int(input())
            if rent_confirm == 0:
                print(f"Thank you to choose our services. We receive the vehicle {rent_list[id_car][0]}")
                cars_list.append(rent_list.pop(id_car))        
    elif option == 3:
        break
    else:
        print("Invalid option, try again...")
    
    print("===================")
    print("type: 0 - RETURN TO MAIN MENU | 1 - END PROGRAM")
    if int(input()) == 1:
        break
        
   