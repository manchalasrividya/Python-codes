class Inventory:
    def __init__(self,l=[]):
        self.l=l
    def __len__(self):
        return len(self.l)
    def __repr__(self):
        return f"{self.l}"
    def __add__(self, other):
        if isinstance(other,Inventory):
            l=self.l+other.l
            return Inventory(l)
        else:
            self.l.append(other)
            return self
i1=Inventory()
i2=Inventory()
print((i1))
print(len(i1+i2))
print(i1+"milk"+"ff"+1)
print(len(i1))
print(i2+"vishnu")
print(i1+i2)