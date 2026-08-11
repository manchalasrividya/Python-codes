# Create a class Employee with attributes name and company_name = "TechCorp".
# Add a class method change_company(cls, new_name) to update the company name for all employees.
# Demonstrate how this change affects all instances.

class Employee:
    company_name="TechCrop"
    def __init__(self,name):
        self.n=name
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
        # print("new_company:{cls.company_name}")
e1=Employee("vidya")
e2=Employee("sri")

print(e1.n, e1.company_name)
print(e2.n, e2.company_name)

Employee.change_company("Google")

print(e1.n, e1.company_name)
print(e2.n, e2.company_name)