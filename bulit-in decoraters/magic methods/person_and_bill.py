class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def __gt__(self, other):
        return self.age>other.age
    def __str__(self):
        return f"name: {self.name},age={self.age}"

p1=Person("vidya",22)
p2=Person("lasya",23)
if p1>p2:
    print (f"{p1.name} will pay bill")
else:
    print( f"{p2.name} will pay bill")
# print(p1)