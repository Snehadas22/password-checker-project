password = input("Enter your password: ")

if len(password) < 6:
    print("Weak Password")
else:
    print("Strong Password")
