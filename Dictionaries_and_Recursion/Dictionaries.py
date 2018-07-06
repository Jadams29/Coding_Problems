# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 10:30:18 2018

@author: joshu
"""

import math
import random



derekDict = {"fName" : "Derek", "lName" : "Banas",
             "address" : "123 Main St"}

print("My name: ", derekDict["fName"])
print()
print("My name: {}".format(derekDict["fName"]))

derekDict["address"] = "215 North ST"

# Setting the key 'city' to the value 'Pittsburgh'
derekDict['city'] = 'Pittsburgh'

# This will check if 'city' is in derekDict and will return True/False
print("Is there a city :", 'city' in derekDict)

# Returns the Values from the dict
print(derekDict.values())

# Returns the Keys from the dict
print(derekDict.keys())

# Must use derekDict.items() or printing k,v will not work
for k, v in derekDict.items():
    print(k,v)
print()

# Searches for 'mName' and will return the value if it exists
#  if the value does not exist it will return "Not Here"
print(derekDict.get("mName", "Not Here"))

# Delete a key:Value pair from dictionary
del derekDict['fName']

for i in derekDict:
    print(i)

# Clear all data from dictionary
derekDict.clear()

employees = []

fName, lName = input("Enter Employee Name: ").split()

employees.append({'fName':fName, 'lName':lName})

print(employees)




