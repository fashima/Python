while True:
    print("**********************")
    print("CALCULATOR")
    print("**********************")

    first_number = float(input("Type the first number: "))
    secound_number = float(input("Type the secound number: "))

    print("CHOOSE THE OPERATION")
    print("1 - ADITION")
    print("2 - SUBTRACTION")
    print("3 - MULTIPLICATION")
    print("4 - DIVISION")
    print("0 - EXIT")

    menu_select = int(input("Type the number: "))

    if menu_select == 1:
        result = first_number + secound_number
        print("Result: ", result)
    elif menu_select == 2:
        result = first_number - secound_number
        print("Result: ", result)
    elif menu_select == 3:
        result = first_number * secound_number
        print("Result: ", result)
    elif menu_select == 4:
        if secound_number != 0:
            result = first_number / secound_number
            print("Result: ", result)
        else:
            print("Error: Divison by 0")
    elif menu_select == 0:
        print("Logout...")
        break
    else:
        print("It's not a valid option, please try again")
