class Courses:
    total_courses=0
    minimum_duration=10
    def __init__(self,title,duration):
        self.title=title
        self.duration=duration
        self.enrolled_students=[]
        self.total_courses+=1
    def enroll(self,student):
        self.enrolled_students.append(student)
    @classmethod
    def update_min_duration(cls,new_duration):
        cls.minimum_duration=new_duration
    @staticmethod
    def is_relaistic_duration(duration):
        if 0<=duration<=1000:
            return "correct duration"
        else:
            return "wrong duration"
c1=Courses("python",20000)
c2=Courses("sql",30)
c1.enroll("vidya")
c2.enroll("sri")
print(Courses.is_relaistic_duration(c1.duration))
print(Courses.is_relaistic_duration(c2.duration))
Courses.update_min_duration(12)
print(c1.enrolled_students)
print(c2.enrolled_students)
print(Courses.is_relaistic_duration(59))
print(Courses.is_relaistic_duration(-23))
