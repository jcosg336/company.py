"""
Program: person.py
Author: Jcosg336
Date: 3/29/2020

The class in this script allow the test_company.py program to run by creating objects that support
it's needs, while also inheriting functions from the Person class in the person.py file.

Input:  Object from the main file inputed to call the desired inheritance

Output: A string that displays the information gathered from the main file, sorted
        and outputted in a formatted text form.
"""

#Defines information for the person object and assigns the values to the pointer address associated
class Person(object):
    
    #constructor
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    #mutator
    def set_address(self, address):
        self.address = address
    
    #accessor
    def get_address(self):
        return self.address
    
    #mutator
    def set_phone(self, phone):
        self.phone = phone
    
    #accessor
    def get_phone(self):
        return self.phone
    
    #accessor
    def get_name(self):
        return self.name
    
    #override __str__ in person.py
    def __str__(self):
        return "Name: " + self.name + \
               "\nAddress: " + self.address + \
               "\nPhone: " + self.phone
