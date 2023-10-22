balance = 500

while True:

    print("********************************")
    print("Select the options below")
    print("1 - Check Balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Exit")
    print("********************************")

    options = int(input("Type the option: "))

    if options == 1:
        print(f"Your current balance is: ${balance:.2f}")
    elif options == 2:
        deposit = float(input("Enter the DEPOSIT amount: $"))
        if deposit < 0:
            print("Invalid value, please use positive numbers")
        else:
            balance += deposit
            print(f"everything worked! You deposited ${deposit:.2f} dollars")
    elif options == 3:
        withdraw = float(input("Enter the WITHDRAW amount: $"))
        if withdraw < 0:
            print("Invalid value, please use positive numbers")
        elif withdraw > balance:
            print("Sorry, your balance is insufficient")
        else:
            balance -= withdraw
    elif options == 4:
        print("Logout successfully")
        break
    else:
        print("Please select a menu option")
    








