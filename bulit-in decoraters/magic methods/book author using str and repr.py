# __str__ and __repr__ Create a class Book with attributes title, author, and price.
# Define __str__ to return: 'Title by Author — Rs.Price' and __repr__ to return: "Book('Title', 'Author', Price)". Verify both using print(), repr(), and in an f-string.




class Author:
    def __init__(self,name,author,price):
        self.name=name
        self.author=author
        self.price=price
    def __str__(self):
        return f"this book {self.name} is written by {self.author}"
    def __repr__(self):
        return f"Book Title:{self.name},Author:{self.author},Price:{self.price}"
a=Author("python dunder methods ","vidya",100)
print(a)
print(repr(a))