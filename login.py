import base64


def newuser():
    Username = input("Choose an Username : ")
    Password = input("Choose a Password : ")
    Passwordchecker = input("Confirm the Password : ")
    password_try = 3
    while Password != Passwordchecker:
        print("Error, the password does not match")
        Password = input("Choose a Password : ")
        Passwordchecker = input("Confirm the Password : ")
        password_try -= 1
        print("You have ", password_try, " attempt left.")
        if password_try <= 0:
            print("you have tried too much wrong password, please try again later")
            break
    f = open("Userdata.txt", 'a')

    ########### Encoding Password ##############
    encoded = base64.b64encode(Password.encode("utf-8")).decode("utf-8")

    f.write(Username)
    f.write(",")
    f.write(encoded)
    f.write("\n")

    f.close()


def login():
    takingFromFile = open("Userdata.txt", "r")

    Username = input("Username : ")
    Password = input("Password : ")

    for lines in takingFromFile:
        lines = lines.strip()
        uName, pWord = lines.split(",")

        decpWord = base64.b64decode(pWord).decode("utf-8")

        if Username == uName:
            if Password == decpWord:
                print("welcome to the program")
                exit()


UserInput = input("Login = y  , Create a new User = n  : ")
if UserInput == "n":
    newuser()
elif UserInput == "y":
    login()
else:
    print("Wrong Character, please type 'y' for login or 'n' for create a new user. ")
