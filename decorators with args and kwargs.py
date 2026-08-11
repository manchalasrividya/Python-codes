def my_decorator(func):
    def inner(*args, **kwargs):
         print("before")
         result=func(*args, **kwargs)
         print("after")
         return result
    return inner
@my_decorator
def add(a,b):
    return a+b
print(add(3,4 ))


