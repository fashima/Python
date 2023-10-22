print("                          PASSWORD GENERATOR                ")
print("                          ------------------                ")

print(' ')
print('                             HOW TO USE?                    ')
print(' ')
print('                               """"""""                     ')
print(' ')
print('1 - You need to define a KEY. Each word you type will turn into a special character.')
print('2 - We recommend setting 8 or more characters to convert into a security password.')
print('3 - The more characters you use to create your password, the harder it is to crack.')
print('4 - When you do it, the program will convert your input into a strong password.')
print(' ')
print('                               """"""""                     ')

user_key = input("Type the KEY: ")

password = ""

for word in user_key:

    if word in "Aa": password = password + "@2"
    elif word in "Bb": password = password + "$5"
    elif word in "Cc": password = password + "4d"
    elif word in "Dd": password = password + "%2"
    elif word in "Ee": password = password + "-"
    elif word in "Ff": password = password + "_l"
    elif word in "Gg": password = password + "Lj"
    elif word in "Hh": password = password + "|x"
    elif word in "Ii": password = password + "+"
    elif word in "Jj": password = password + "1_"
    elif word in "Kk": password = password + "KM"
    elif word in "Ll": password = password + "*-"
    elif word in "Mm": password = password + "-*"
    elif word in "Nn": password = password + "+."
    elif word in "Oo": password = password + "nu"
    elif word in "Pp": password = password + "85"
    elif word in "Qq": password = password + "%*"
    elif word in "Rr": password = password + "&"
    elif word in "Ss": password = password + "!"
    elif word in "Tt": password = password + "?"
    elif word in "Uu": password = password + "_="
    elif word in "Vv": password = password + "s&"
    elif word in "Ww": password = password + "n@"
    elif word in "Xx": password = password + "<X>"
    elif word in "Yy": password = password + "k*"
    elif word in "Zz": password = password + "$$"
    else: password = password + word

print(password)
