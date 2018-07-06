# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 19:44:09 2018

@author: joshu
"""

def sumAll(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sumAll(1,2,3,4,5))
print(sumAll(2,3,4))