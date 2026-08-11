class Members:
    shared_BMI_limit=25
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
    def BMI(self):
        BMI=self.height/(self.weight**2)
        if BMI>=Members.shared_BMI_limit:
            print("healthy")
        else:
            print("not")
    @classmethod
    def update(cls,new):
        cls.shared_BMI_limit=new
    @staticmethod
    def valid(weight,height):
        if weight>0 and height>0:
            print("valid")
        else:
            print("not valid")