# def repeat(n):
#     def logger(func):
#         def wrapper(*args,**Kwargs):
#             print("hello")
#             for i in range(n):
#                 func(*args, **Kwargs)
#             print("bye")
#         return wrapper
#     return logger
# @logger(func)
# @repeat(3)
# def hello():
#     print("gfujir")
# hello()

def repeat(n):