# Create a Python program using a class named Calculator with methods for addition, subtraction, multiplication, and division.
# Output
# Addition (10 + 5): 15
# Subtraction (10 - 5): 5
# Multiplication (10 * 5): 50
# Division (10 / 5): 2.0
# Division (10 / 0): Error: Division by zero is not allowed.
# <-------------------------------------------------------------------------------------------------------------------------------------->
class Calculator :
    def __init__(self,a,b):
        self.a=a
        self.b=b
    #This function addition is used to add the two numbers provided by the user here they are stored in a,b variables.
    def addition(self,a,b):
        return a+b
    # This function subtraction is used to subtract the two numbers provided by the user here they are stored in a,b variables.
    def subtraction(self,a,b):
        return a-b
    # This function  multiply is used to multiply the two numbers provided by the user here they are stored in a,b variables.
    def multiply(self,a,b):
        return a*b
    # This function divide is used to divide the two numbers provided by the user here they are stored in a,b variables.
    # And The function also handles the exceptions when the number is divided by Zero,done using try and except blocks.
    def divide(self,a,b):
        try:
            ans=a/b
            return ans
        except ZeroDivisionError:
            print(f"DivisionError({a} / {b}) : Division by zero is not allowed")
            exit()
a,b=list(map(int,input().strip().split()))
p=Calculator(a,b)
print(f"Addition({a} + {b}): {p.addition(a,b)}")
print(f"Subtraction({a} - {b}): {p.subtraction(a,b)}")
print(f"Multiplication({a} * {b}): {p.multiply(a,b)}")
print(f"Division({a} / {b}): {p.divide(a,b)}")