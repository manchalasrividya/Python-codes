class Loan:
    rate_of_interest=20
    threshold=40000
    def __init__(self,borrower_name,principal):
        self.borrower_name=borrower_name
        self.principal=principal
    def total_pay_amount(self,sala):
        if Loan.valid(sala):
            k=self.principal+(Loan.rate_of_interest/100*self.principal)
            return k
        else:
            return "not valid sala"
    @classmethod
    def update(cls,new):
        cls.rate_of_interest=new
    @staticmethod
    def valid(sala):
        return sala>=Loan.threshold
l1=Loan("vi",1000)
l2=Loan("kalyani",2000)
Loan.update(50)
print(l1.total_pay_amount(600000))
print(l2.total_pay_amount(2000))
