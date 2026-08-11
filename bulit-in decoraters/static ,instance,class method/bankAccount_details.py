# Create a class BankAccount with:
# •	class variable bank_name
# •	instance variables holder and balance
# •	instance method deposit(amount)
# •	class method change_bank_name(cls, new_name)
# •	static method validate_amount(amount) → returns True if amount > 0
# Show transactions and how static + class methods work together

class BankAccount:
    bank_name="sbi"
    def __init__(self,h,b):
        self.holder=h
        self.balance=b
    def deposit(self,amount):
        return self.balance+amount
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    @staticmethod
    def validate_amount(amount):
        return amount > 0
a1=BankAccount("sri",5000)
a2=BankAccount("vidya",400000)
print("Bank Name:", BankAccount.bank_name)
a1.deposit(1000)
a2.deposit(500)
a1.deposit(-100)
BankAccount.change_bank_name("HDFC")
print("Updated Bank Name:", BankAccount.bank_name)