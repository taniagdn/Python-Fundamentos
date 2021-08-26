#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:39:47 2021

@author: taniagualli
"""


class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(a,name, salary):
      a.name = name
      a.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d", Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

"This would create first object of Employee class"      
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Sandra", 5000)
emp3 = Employee("Ana",8000)
emp4 = Employee("Briguitte",8000)
emp5 = Employee ('Juan',1200)
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()
emp5.displayEmployee()
print ("Total Employee %d" % Employee.empCount)


Employee.displayEmployee(emp1)