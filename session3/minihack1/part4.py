Username = input("Enter your username:")
Email = input("Enter your email:")
while True: 
    if "@gmail.com" in Email:
        print("Verified Email")
        Password = input("Enter your password:")
        if Password.isdigit():
            print("Password must contain numbers and letters")
        elif Password.isalpha():
            print("Password must contain numbers and letters")
        elif len(Password) <= 8:
            print("Password must contain more than 8 digits")
        else: 
            print("Verified Password")
    else: 
        print("Email must contain @gmail.com")
    break


    

