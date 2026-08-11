def login(fun):
    def inner():
        user=input("enter userName: ")
        password=input("enter Password: ")
        if user == "vidya" and password =="1234":
            fun()
        else:
            print("invalid creditionals")
    return inner
@login
def file():
    print("secure file")
file()