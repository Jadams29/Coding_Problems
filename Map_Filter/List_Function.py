# ---------- PROBLEM ----------
# Create a function that receives a list and a function
# The function passed will return True or False if a list
#  value is odd.
# The surrounding function will return a list of odd numbers

import random

def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def change_list(list, func):
    oddList = []

    for i in list:
        if func(i):
            oddList.append(i)
    return oddList

testList = [random.randrange(1,20) for i in range(20)]

print(change_list(testList, is_it_odd))