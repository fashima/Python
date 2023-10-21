print("Mr. Smith, welcome to Brazilian Bank")

password = 'S@m$iTh_36y'

authentication = input("Before you access your account, please input the password number 75 of your security card: ")

attempt = 0
while authentication != password:
    print("Incorrect password, please try again...")
    attempt += 1
    authentication = input("Before you access your account, please input the password number 75 of your security card: ")
    
print("Access granted. You took", attempt, "attempts to log in.")
    
