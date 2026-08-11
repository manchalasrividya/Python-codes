class Students:
    batch="Py16"
    total=0
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        Students.total+=1
s1=Students("vidya",21,"knr")
s2=Students("lasya",21,"knr")
s2=Students("nandhu",21,"knr")
print(Students.total)