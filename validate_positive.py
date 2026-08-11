def validate_positive(func):
    def inner(*args):
        for i in args:
            if i<0:
                print("numbers is negative")
                return
        result=func(*args)
        return result
    return inner
@validate_positive
def multiply(a,b):
    print(a*b)
multiply(3,-5)