import math


class Employee:

    def __init__(self, name, age, lname="Eren"):
        self.name = name
        self.age = age
        self.lname = lname

    def check_employee(self, given_age):

        if self.age > given_age:
            status = "older"
        else:
            status = "younger"

        print(f"Employee {self.name} is {status} than {given_age}")

    def __repr__(self):
        return f"{self.name} {self.lname} {self.age}"

    def __str__(self):
        return f"This is {self.name + ' ' + self.lname} and age is {self.age}"


if __name__ == '__main__':
    emp = Employee('Onder', 37)
    emp.check_employee(40)
    print(emp)
    print(repr(emp))
    print(emp.__repr__())
