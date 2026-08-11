def check_number(func):
    def num(c):
        if c%2==0:
            print("even number")
        else:
            print("odd")
        func(c)
    return num
@check_number
def show(n):
    print("number accepted")
show(10)