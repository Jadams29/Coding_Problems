# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 20:08:42 2018

@author: joshu
"""

import math
import random

# Fibbonacci
# 1,1,2,3,5,8,13....

# My Example
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fibonacci(num - 1) + fibonacci(num - 2) 
    return result
print(fibonacci(6))

# Derek Example
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        return result

print(fib(5))
    