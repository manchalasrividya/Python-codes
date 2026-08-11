# def count_calls(func):
#     c = [0]
#     def wrapper(*args):
#
#         c[0]=c[0]+1
#         print(c[0])
#         result=func(*args)
#         return result
#     return wrapper
#
# @count_calls
# def hello():
#     print("hello")
# hello()
# hello()
# hello()
# print(hello.c[0])





# class Employee:
#     def __init__(self,n,exp,sal,dep):
#         self.name=n
#         self.exp=exp
#         self.sal=sal
#         self.dep=dep
#     def eligiblity(self):
#         if self.exp<5:
#             print("not eligible")
#         else:
#             self.promotion()
#
#     def promotion(self):
#         if self.dep.lower()=="emp":
#             self.dep="manager"
#             self.sal+=self.sal*0.15
#         elif self.dep.lower()=="manager":
#             self.dep="hr"
#             self.sal+=self.sal*0.25
#         else:
#             self.dep="admin"
#             self.sal+=self.sal*1.25
#         print(f"department: {self.dep},salary: {self.sal}")
# e1 = Employee("vidya", 6, 10000, "emp")
# e1.promotion()
