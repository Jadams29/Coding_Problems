# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 11:27:53 2018

@author: joshu
"""

# Will provide different outputs based on age
# 1-18 -> Important
# 21, 50, or > 65 -> Important
# All others -> Not Important
# 

age = eval(input("Please enter your age: "))

if ((age >= 1) and (age <= 18)):
    print("IMPORTANT")
elif ((age == 21) or (age == 50) or (age > 65)):
    print("IMPORTANT")
else:
    print("NOT IMPORTANT")
    