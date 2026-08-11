class Vehicle:
    charge_rate=6
    def __init__(self,model,kilometers_run,service_history):
        self.model=model
        self.kilometers_run=kilometers_run
        self.service_history=service_history

    def service_charge(self):
        x=self.kilometers_run*Vehicle.charge_rate
        return x
    @classmethod
    def update(cls,new):
        cls.charge_rate=new
    @staticmethod
    def valid(years):
        if years<=15:
            return "not eligible"
        else:
            return "eligible"
v1=Vehicle("ss",5,["oil check","enginee check"],)
v2=Vehicle("ps",9,["oil check","enginee check"],)
Vehicle.update(10)
print(v1.service_charge())
print(v2.service_charge())
print(v1.valid(20))
print(v2.valid(4))