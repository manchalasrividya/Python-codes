# Arithmetic Dunders Write a class Vector2D(x, y).
# Implement __add__, __sub__, __mul__ (scalar multiply), __truediv__ (scalar divide), __floordiv__, and __mod__ (element-wise).
# Also add __str__ and __repr__. Test: Vector2D(3,4) + Vector2D(1,2) should give Vector2D(4,6).
class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self, other):
        return self.x+other.x,self.y+other.y
    def __sub__(self,other):
        return (self.x-other.x,self.y-other.y)
    def __mul__(self, other):
        return (self.x*2,self.y*2)
    def __truediv__(self, other):
        return (self.x/2,self.y/2)
    def __str__(self):
        return f"{self.x,self.y}"
    def __repr__(self):
        return f"vector2D{self.x,self.y}"
v1=Vector2D(3,4)
v2=Vector2D(1,2)
print(v1+v2)
print(v1-v2)
print(v1/v2)
print(v1)
print(v1,v2)
print([v1])
