# Create a class Car with:
# •	instance attribute mileage
# •	class attribute wheels = 4
# Add an instance method display_specs() that prints mileage and wheels.
# Then change wheels using a class method, and print again.

class Car:
    wheels=4
    def __init__(self,m):
        self.milage=m
    def display_specs(self):
        print(f"milage: {self.milage}")
        print(f"wheels:{self.wheels}")
    @classmethod
    def change(cls,new):
        cls.wheels=new
        print(f"wheels:{cls.wheels}")
c2=Car(15)
c1=Car(20)
c1.display_specs()
c1.change(8)
c1.display_specs()
c2.display_specs()