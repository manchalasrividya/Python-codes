class Product:
    base_tax=18
    def __init__ (self,name,base_price):
        self.n=name
        self.bp=base_price
    def finial_price(self):
        return self.bp+(self.bp*Product.base_tax / 100)
    @classmethod
    def change_tax_rate(cls,new_rate):
        cls.base_tax=new_rate
    @staticmethod
    def is_valid_price(base_price):
        if base_price>0:
            print("corect")
        else:
            print("wrong")
p1=Product("soap",50)
p2=Product("pen",20)
print(p1.finial_price())
print(p2.finial_price())
Product.change_tax_rate(10)
print(p1.finial_price())
print(p2.finial_price())
Product.is_valid_price(500)
Product.is_valid_price(-3)
