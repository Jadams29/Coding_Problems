# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 19:17:00 2018

@author: joshu
"""

# Solve for X
# x + 4 = 9

# X will always be the 1st value received and you only
# will deal with addition

def algebraic_expression(str_input):
    input_list = str_input.split(" ")
    x_value = int(input_list[4]) - int(input_list[2])
    return x_value

#formula = input("Enter the formula to solve: ")

#print("In the formula ", formula, ", x is {}".format(algebraic_expression(formula)))

def mult_divide(num1, num2):
    return (num1 * num2), (num1 / num2)

mult, divide = mult_divide(5,4)

print("5 * 4 = ", mult)
print("5 / 4 = ", divide)