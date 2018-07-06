# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 08:54:09 2018

@author: joshu
"""

# Ask the user to input 2 values and store them in variables num1, num2
num1, num2 = input('Enter two numbers: ').split(" ")

# Convert the strings into regular numbers integers
num1 = int(num1)
num2 = int(num2)

# Add the values entered and store in sum
Sum = num1 + num2

# Subtract the values and store in difference
difference = num1 - num2 

# Multiply the values and store in product
product = num1 * num2

# Divide the values and store in quotient
quotient = num1 / num2

# Modulus the values and store in remainder
remainder = num1 % num2

# Print the results on the screen
print('.:RESULTS:.')
print("{} + {} = {}".format(num1, num2, Sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} / {} = {}".format(num1, num2, product))
print("{} * {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))

