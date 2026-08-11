# . Create a class Book with:
# •	instance attributes title, author
# •	a class variable total_books
# •	a class method from_string(cls, book_str) that creates an object from "title-author" format
# •	a static method is_valid_title(title) that checks if title has at least 3 characters
# •	increment total_books for every book created
# Demonstrate:
# •	Creating books using both the constructor and the class method
# •	Validating titles before creation

class Book:
    total=0
    def __init__(self,t,a):
        self.title=t
        self.author=a
        Book.total+=1
    @classmethod
    def from_string(cls,book_str):
        t,a=book_str.split("-")
        if cls.is_valid(t):
            b=cls(t,a)
            return b
        else:
            print("Invalid Title")
    @staticmethod
    def is_valid(t):
        return len(t)>3
    if book.is_valid("python"):
        b1=Book

