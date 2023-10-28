import os

def main_menu():
    print("0 : Addition")
    print("1 : Subtraction")
    print("2 : multiplication")
    print("3 : Division")
    print("4 : Exponentiation")
    print("\n")
    print("Which of the mathematical operations would you like to calculate?")   

while True:
    main_menu()
    menu = int(input())
    if menu == 0:
        print(">>> + was chosen")
        print("\n")
        print("Input the first value:")
        n1 = int(input())
        print("\n")
        print("input the secound value:")
        n2 = int(input())
        print("\n")
        addition = n1 + n2
        print(f"{n1} + {n2} = {addition} ")
        print(" ")
        print("=" * 20)
        print("Would you like to perform another mathematical operation? 0 - YES, 1 - NO")
        option = int(input())
        if option == 0:
            os.system('cls')
        elif option == 1:
            break
        else:
            print("Invalid Option")
    elif menu == 1:
        print(">>> - was chosen")
        print("\n")
        print("Input the first value:")
        n1 = int(input())
        print("\n")
        print("Input the secound value:")
        n2 = int(input())
        print("\n")
        subtraction = n1 - n2
        print(f"{n1} - {n2} = {subtraction} ")
        print(" ")
        print("=" * 20)
        print("Would you like to perform another mathematical operation? 0 - YES, 1 - NO")
        opcao = int(input())
        if option == 0:
            os.system('cls')
        elif option == 1:
            break
        else:
            print("Invalid Option")
    elif menu == 2:
        print(">>> * was chosen")
        print("\n")
        print("Input the first value:")
        n1 = int(input())
        print("\n")
        print("Input the secound value:")
        n2 = int(input())
        print("\n")
        multiplication = n1 * n2
        print(f"{n1} * {n2} = {multiplication} ")
        print(" ")
        print("=" * 20)
        print("Would you like to perform another mathematical operation? 0 - YES, 1 - NO")
        option = int(input())
        if option == 0:
            os.system('cls')
        elif option == 1:
            break
        else:
            print("Invalid Option")
    elif menu == 3:
        print(">>> / was chosen")
        print("\n")
        print("Input the first value:")
        n1 = int(input())
        print("\n")
        print("Input the secound value:")
        n2 = int(input())
        print("\n")
        division = n1 / n2
        print(f"{n1} / {n2} = {division} ")
        print(" ")
        print("=" * 20)
        print("Would you like to perform another mathematical operation? 0 - YES, 1 - NO")
        option = int(input())
        if option == 0:
            os.system('cls')
        elif option == 1:
            break
        else:
            print("Invalid Option")
    elif menu == 4:
        print(">>> ** was chosen")
        print("\n")
        print("Input the first value:")
        n1 = int(input())
        print("\n")
        print("Input the secound value:")
        n2 = int(input())
        print("\n")
        exponentiation = n1 ** n2
        print(f"{n1} ** {n2} = {exponentiation} ")
        print(" ")
        print("=" * 20)
        print("Would you like to perform another mathematical operation? 0 - YES, 1 - NO")
        option = int(input())
        if option == 0:
            os.system('cls')
        elif option == 1:
            break
        else:
            print("Invalid Option")
    else:
        print("Invalid Option")