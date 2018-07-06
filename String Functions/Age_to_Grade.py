# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 11:37:46 2018

@author: joshu
"""

# If the age is 5 -> "Go to Kindergarten"

# Ages 6-17 -> " Go to grades 1-12"

# If age is greater than 17 -> "Go to College"

# Less than 10 lines

age = eval(input("Please Enter your age: "))
if (age < 5):
    print("Stay at Home")
elif (age == 5):
    print("Go to Kindergarten")
elif (age >= 6) and (age <= 17):
    grade = age - 5
    print("Go to grade {}.".format(grade))
elif (age >= 17):
    print("Go to College")
