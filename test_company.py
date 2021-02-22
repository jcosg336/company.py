"""
Program: test_company.py
Author: Jcosg336
Date: 3/29/2020

This file is a test program for the fuctions in company.py and person.py
"""

from company import Employee, Customer

customer1 = Customer("Andrew Coltor", \
                   "365 Jacob's Lane, Denver, CO, 33090", \
                   "661-555-2255", \
                   781)

employees = []
employees.append(Employee("James Chen", \
                   "99 Moulton Ave, Providence, RI, 07654", \
                   "504-555-6548", \
                   907, \
                   77000)
                 )

employees.append(Employee("Brady Parker", \
                   "66 Alberto Dr., Hartford, CT, 06963", \
                   "851-555-7913", \
                   321, \
                   91000)
                 )

print("Customers: \n")      #print customer information
print(customer1, "\n")

print("Employees: \n")      #print employee information
for employee in employees:
    print(employee, "\n")

for employee in employees:  #search badge number 321 and print associated employee information
    if (employee == employees[1]):
        print("Found the employee with badge #:", employee.get_badge())
        print(employee, "\n")
