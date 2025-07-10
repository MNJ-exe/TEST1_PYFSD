# You are tasked with writing a Python class Employee to represent an employee's information.
# The class should have the following features:
# Private Attributes: name: The name of the employee (string),
# salary: The salary of the employee (float).age: The age of the employee (integer).
# Methods:A setter method set_name(name) to set the employee's name.
# A getter method get_name() to retrieve the employee's name.
# A setter method set_salary(salary) to set the employee's salary ,
# (it should be validated to ensure salary is greater than 0).
# A getter method get_salary() to retrieve the employee's salary.
# A setter method set_age(age) to set the employee's age (age should be between 18 and 100).
# A getter method get_age() to retrieve the employee's age.Constraints:Salary must be greater than 0.
# Age must be between 18 and 100 (inclusive).
# If invalid data is entered, print appropriate error messages.

# Output
# Employee Name: John Doe
# Employee Salary: 50000.0
# Employee Age: 30
# Error: Salary must be greater than 0.
# <---------------------------------------------------------------------------------------------------------->
class Employee:
    def __init__(self):
        self.__name = "<NAME>"
        self.__salary = 1000
        self.__age = 20

    # This function set_name will take name of the employee as the input and assigns it to the name variable which is private.
    def set_name(self,name):
        self.__name = name

    # This function set_salary will take name of the employee as the input and assigns it to the name variable which is private and make sures that the salary >0.
    def set_salary(self,salary):
        if salary>0:
            self.__salary = salary
        else:
            print("Error : Salary should be greater than 0")
            exit()

    # This function set_age will take name of the employee as the input and assigns it to the name variable which is private and makes sure that the age is between 18 and 100.
    def set_age(self,age):
        if 18<=age<=100:
            self.__age = age
        else:
            print("Error : Age should be between 18 and 100")
            exit()

    # This function get_name is used to print the name that was assigned using the set_name function
    def get_name(self):
        print(f"Employee Name : {self.__name}")
    # This function get_salary is used to print the salary that was assigned using the set_salary function
    def get_salary(self):
        print(f"Employee Salary : {self.__salary}")
    # This function get_age is used to print the age that was assigned using the set_age function
    def get_age(self):
        print(f"Employee Age : {self.__age}")
emp = Employee()
emp.set_name(input("Enter Employee Name for input : "))
emp.set_salary(int(input("Enter Employee Salary for input : ")))
emp.set_age(int(input("Enter Employee Age for input : ")))
emp.get_name()
emp.get_salary()
emp.get_age()
