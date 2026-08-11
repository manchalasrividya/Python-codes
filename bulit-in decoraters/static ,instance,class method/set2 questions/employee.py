class Employee:
    minimum_experience=2
    def __init__(self,name,experience,department):
        self.n=name
        self.exp=experience
        self.dep=department
    def promotion(self):
        if Employee.valid(self.dep):
            if self.exp>=Employee.minimum_experience:
                return "Eligibile"
            else:
                return "not"
        else:
            return "dept is not valid"
    @classmethod
    def update(cls,new):
        cls.minimum_experience=new
    @staticmethod
    def valid(dep):
        return dep in ["hr","tech","admin"]
e1=Employee("vidya",5,"hr")
e2=Employee("sri",7,"tech")
e3=Employee("vida",5,"sales")
Employee.update(5)
print(e1.promotion())
print(e3.promotion())