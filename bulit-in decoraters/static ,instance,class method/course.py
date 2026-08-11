# . Create a class Course with:
# •	class variable total_students
# •	instance variable student_name
# •	instance method enroll() → increments total_students
# •	class method show_total(cls) → prints total students
# •	static method is_eligible(age) → returns True if age ≥ 18
# Demonstrate enrolling multiple students and show total count

class Course:
    total_students=0
    def __init__(self,st):
        self.student_name=st
    def enroll(self):
        Course.total_students+=1
    @classmethod
    def show_total(cls):
        print(cls.total_students)
    @staticmethod
    def is_eligible(age):
        return age>=18

s1=Course("vidya")
s2=Course("sri")
s3=Course("nandhu")
s4=Course("lasya")
s1.enroll()
s2.enroll()
s3.enroll()
s4.enroll()
Course.show_total()
print(Course.is_eligible(30))
print(Course.is_eligible(10))
print(Course.is_eligible(60))
print(Course.is_eligible(0))
