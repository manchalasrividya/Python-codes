# def my_decorator(func):
#     def greet():
#         print("before function exceution")
#         func()
#         print("after excection")
#     return greet
# def hiiiu():
#     print("hello student")
# hiiiu=my_decorator(hiiiu)
# hiiiu()


def my_decorator(func):
    def greet():
        print("Welcom Message")
        func()
        print("Thank you Message")
    return greet
@my_decorator
def say_hello():
    print("good morning")
say_hello()
