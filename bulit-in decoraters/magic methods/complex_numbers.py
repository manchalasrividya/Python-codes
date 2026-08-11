class Complex_numbers:
    def __init__(self,i,r):
        self.real=r
        self.imaginary=i
    def __add__(self, other):
        # return f"{self.real+other.real} + {self.imaginary+other.imaginary}i"
        return str(self.real+other.real)+ "+" +str(self.imaginary+other.imaginary)+ "i"
c1=Complex_numbers(2,6)
c2=Complex_numbers(5,9)
print(c1+c2)