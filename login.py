
def newuser():
    Username = input("Choose an Username : ")
    Password = input("Choose a Password : ")
    Passwordchecker = input("Confirm the Password : ")
    if Password != Passwordchecker:
        print("Error, the password does not match")
        newuser()
    f = open("Userdata.txt",'w')
    f.write(Username )
    f.write("\n"+Password)
    f.close()


def login():
    lines = []
    with open ('Userdata.txt', 'rt') as in_file:
        for line in in_file:
            lines.append(line.rstrip('\n'))
    Username = input("Username : ")
    Password = input("Password : ")
    if Username != lines[0]:
        print("wrong Username")
    elif Password != lines[1]:
        print("Password doesnt match")
    elif Username == lines[0] and Password == lines[1]:
        print("welcome to the program")




newuser()
login()