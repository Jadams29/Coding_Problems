# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 09:14:15 2018

@author: joshu
"""

# Calculator
# Prompt user for input
# Display the entered problem and solution
# .:Example:.
# Enter Calculation: 5 * 6
# 5 * 6 = 30

num1, operation, num2  = input("Enter Calculation: ").split()
num1 = int(num1)
num2 = int(num2)
if operation == '+':
    solution =  (num1 + num2)
elif operation == '-':
    solution = (num1 - num2)
elif operation == '*':
    solution = (num1 * num2)
elif operation == '/':
    solution = (num1 / num2)
elif operation == '%':
    solution = (num1 % num2)
else:
    print("You did not enter a valid calculation")
    
print("{} {} {} = {}".format(num1, operation, num2, solution))