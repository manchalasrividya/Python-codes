def calculate(func):
    def sub(a=10,b=20):
        print(a-b)
        func()
    return sub
@calculate         #edhi main function
def add(a=15,b=20):
    print(a+b)
add()

