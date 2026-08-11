class Bank:
    def __init__(self,n,acc,pin):
        self.name=n
        self.acc=acc
        self.pin=pin
        self.balance=0
    def valid_pin(self):
        p=int(input("enter ur pin: "))
        return p==self.pin
    def deposite(self):
        m=int(input())
        if m>=0:
            self.balance+=m
        else:
            print("invalid money")
    def withdraw(self):
        if self.valid_pin():
            m=int(input("enter the withdraw money: "))
            if 0<=m<=self.balance:
                print("withdraw successfully")
                self.balance-=m
            else:
                print("invalid /insufficent money")
        else:
            print("wrong pin")
    def change_pin(self):
        if self.valid_pin():
            p=int(input("enter new pin: "))
            self.pin=0
            print("pin changed successfully")
        else:
            print("wrong pin")
    def __str__(self):
        if self.valid_pin():
            return f"name: {self.name}\n account no: {self.acc} \n balance: {self.balance}"
        else:
            return "wrong pin"
    def __repr__(self):
        return self.name




