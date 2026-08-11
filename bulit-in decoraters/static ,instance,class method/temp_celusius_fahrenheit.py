# . Create a class Temperature with:
# •	instance attribute celsius
# •	a static method to_fahrenheit(celsius)
# •	an instance method show_conversion() that uses the static method to print both values.

class Temperature:
    def __init__(self,celsius):
        self.c=celsius
    @staticmethod
    def to_fahrenheit(celsius):
        return(9/5)*celsius+32
    def show_conversion(self):
        f = Temperature.to_fahrenheit(self.celsius)
        print("Celsius:", self.celsius)
        print("Fahrenheit:", f)

t = Temperature(25)
t.show_conversion()