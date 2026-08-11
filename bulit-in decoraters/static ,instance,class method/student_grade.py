# . Create a class Student with:
# •	class variable passing_marks = 40
# •	instance attributes name, marks
# •	instance method result() → prints pass/fail using class variable
# •	class method update_passing_marks(cls, new_marks)
# •	static method grade_category(marks) → returns "A", "B", "C" based on score ranges
# Use all three in a program that:
# 1.	Creates students
# 2.	Updates the passing criteria
# 3.	Displays grade category and result

class Student:
    passing_marks=40
    def __init__(self,n,m):
        self.name=n
        self.marks=m
    def result(self):
        if self.marks>=Student.passing_marks:
            print(self.name,"pass")
        else:
            print(self.name,"fail")
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.update_passing_marks(50)
    @staticmethod
    def grade_category(marks):
        if marks>=90:
            return "A"
        elif marks>=75:
            return "B"
        else:
            return "C"
c1=Student("vidya",90)
c2=Student("sri",30)
print(Student.grade_category(c1.marks))
print(Student.grade_category(c2.marks))