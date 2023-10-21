print("WELCOME TO SUM PROGRAM")
print("Type many numbers as you want to sum")
print("Type the number '0' when you want to finish the inputs. The machine will show the result. ")
print("**********************")
numbers = int(input("Type an integer number: "))

count = 0
while numbers != 0:
    print(f"You type the number: {numbers}")
    count += numbers
    numbers = int(input("Type an integer number: "))
print("SUM: ", count)


