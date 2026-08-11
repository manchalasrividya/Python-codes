# . Create a class Student with instance attributes name and marks.
# Add an instance method is_passed() that returns True if marks > 40.
# Then create 2 student objects and print whether each has passed or failed.
class Student:
    def __init__(self,name,marks):
        self.n=name
        self.m=marks
    def is_passed(self):
        if self.m>40:
            print("passed")
        else:
            print("failed")
s1=Student("vidya",90)
s2=Student("sri",39)
s1.is_passed()
s2.is_passed()
