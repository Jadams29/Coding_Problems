# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:51:43 2018

@author: joshu
"""

import math
import random

# Recursive Factorial

def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
    return result

print(factorial(4))

def recursive_factorial(num):
    if num <= 1:
        return 1
    else:
         return (recursive_factorial(num - 1) * num)


print(recursive_factorial(4))