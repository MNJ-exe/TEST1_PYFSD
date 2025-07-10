# Write a Python program to implement a class Student that has the following functionalities:
# Private Attributes:name (a string representing the student's name)marks (an integer representing the student's marks, ranging from 0 to 100)
# Methods:A setter method set_name(name) that sets the student's name.A getter method get_name() that returns the student's name.
# A setter method set_marks(marks) that sets the student's marks (ensuring marks are between 0 and 100).
# A getter method get_marks() that returns the student's marks.Constraints:Marks should be between 0 and 100 (both inclusive).
# If invalid marks are entered (like negative values or values above 100), print an error message.
# Output:
# Student Name: Alice
# Student Marks: 85
# Error: Marks should be between 0 and 100.
# Student Marks (after invalid input): 85
# <-------------------------------------------------------------------------------------------------------------------------------------------->
class Student:
    def __init__(self):
        # '__' represents that the attribute is private.
        self.__name = "<NAME>"
        self.__marks=90
    #This function set_name will take name of the student as the input and assigns it to the name variable which is private.
    def set_name(self,name):
        self.__name = name
    #This function set_marks will take marks of the student as the input and assigns it to the marks variable which is private.
    #It also makes sure that the numbers that are being entered are between 0 and 100
    def set_marks(self,marks):
        if 0<=marks<=100:
            self.__marks=marks
        else:
            print("Error:Marks must be between 0 and 100")
            exit()
    #This function get_name is used to print the name that was assigned using the set_name function
    def get_name(self):
        print("Student Name:",self.__name)
    #This function get_marks is used to print the marks that was assigned using the set_marks function
    def get_marks(self):
        print("Student Marks:",self.__marks)
std=Student() #This creates an object for the class to manipulate the data init.
std.set_name(input("Enter your name:")) #Name will be taken as input from the user.
std.set_marks(int(input("Enter your marks:"))) #Marks will be taken as input from the user.
std.get_name()  #Prints the Name
std.get_marks() #Prints the Marks.