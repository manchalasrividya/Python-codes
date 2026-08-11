# Create a class Student that:
# •	Keeps track of the total number of students created.
# •	Determines whether a student passed or failed based on a shared passing mark.
# •	Provides a method to curve marks by increasing everyone’s marks by a percentage.
# •	Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
# Demonstrate:
# 1.	Creating multiple students.
# 2.	Applying a grading curve.
# 3.	Displaying updated results with letter grades.

# class Student:
#     total_number=0
#     def __init__(self,name,marks,s):
#         self.n=name
#         self.m=marks
#         self
#         Student.total_number+=1
#     def is_passed(self):
#         if self.m>=40:
#             print("pass")
#         else:
#             print("fail")
#     @staticmethod
#     def perc():
#         print(self.m/)

class Student:
    total_number = 0
    passing_marks = 40

    def __init__(self, name, marks):
        self.n = name
        self.m = marks
        Student.total_number += 1

    def is_passed(self):
        if self.m >= Student.passing_marks:
            print("Pass")
        else:
            print("Fail")

    def curve_marks(self,percent):
        self.m=self.m+(percent/100*self.m)
        return self.m

    @staticmethod
    def grade(marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "F"


# Creating students
s1 = Student("Ram", 35)
s2 = Student("Ravi", 72)
s3 = Student("Sita", 88)

print("Total Students:", Student.total_number)
print(s1.curve_marks(10))
print(Student.grade(s1.m))

