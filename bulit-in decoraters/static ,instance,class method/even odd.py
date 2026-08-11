# Create a class MathOps with a static method is_even(num) that returns True if the number is even.
# Then call it both from the class and an instance.

class MathOps:
    @staticmethod
    def is_even(num):
        if num%2==0:
            print("even")
        else:
            print("odd")
MathOps.is_even(5)