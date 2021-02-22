"""
Program: company.py
Author: Jcosg336
Date: 3/29/2020

The classes in this script allow the test_company.py program to run by creating values that support
it's needs, while also inheriting functions from the Person class in the person.py file.

Input:  Object from the main file inputed to call the desired inheritance

Output: A string that displays the information gathered from the main file, sorted
        and outputted in a formatted text form.
"""

#import Person class from person.py
from person import Person

#Customer class
class Customer(object):

    #constructor
    def __init__(self, name, address, phone, credit_score):
        self.name = name
        self.address = address
        self.phone = phone
        self.credit_score = credit_score

    #mutator
    def set_score(self, credit_score):
        self.credit_score = credit_score

    #accessor
    def get_score(self):
        return(self.credit_score)

    #override __str__ in person.py
    def __str__(self):
        return "Name: " + str(self.name) + "\n" + \
               "Address: " + str(self.address) + "\n" + \
               "Phone: " + str(self.phone) + "\n" + \
               "Credit Score: " + str(self.credit_score)

#Employee class
class Employee(object):
    
    #constructor
    def __init__(self, name, address, phone, badge, salary):
        self.name = name
        self.address = address
        self.phone = phone
        self.badge = badge
        self.salary = salary

    #mutator
    def set_badge(self, badge):
        self.badge = badge

    #accessor
    def get_badge(self):
        return(self.badge)

    #mutator
    def set_salary(self, salary):
        self.salary = salary

    #accessor
    def get_salary(self):
        return(self.salary)

    #override __str__ in person.py
    def __str__(self):
        return "Name: " + str(self.name) + "\n" + \
               "Address: " + str(self.address) + "\n" + \
               "Phone: " + str(self.phone) + "\n" + \
               "Badge: " + str(self.badge)

