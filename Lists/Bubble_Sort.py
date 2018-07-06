# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 20:31:22 2018

@author: joshu
"""

import random
import math

# 1. An outer loop decreases in size each time
# 2. The goal is to have the largest number at the end of the list
#        when the outer loop completes 1 cycle
# 3. The inner loop starts comparing indexes at the beginning of the loop
# 4. Check if list[Index] > list[Index + 1]
# 5. If so swap the index values
# 6. When the inner loop completes the largest number is at the end
#        of the list
# 7. Decrement the outer loop by 1



numList = []

for i in range(5):
    numList.append(random.randrange(1,10))

for i in numList:
    print(i)

# Using List Comprehensions
testList = [random.randrange(1,10) for i in range(5)]

print(testList)


def bubble_sort(unsorted_list):
    # Setting i equal to the lenth of the unsorted_list - 1 because if the list
    #  has 5 elements the indexes are 0,1,2,3,4 and that is 5 elements
    i = len(unsorted_list) - 1
    
    while i > 1:
        k = 0
        while k < i:
            if unsorted_list[k] > unsorted_list[k + 1]:
                # Swap
                temp = unsorted_list[k]
                unsorted_list[k] = unsorted_list[k + 1]
                unsorted_list[k + 1] = temp
            else:
                k += 1
        
        i -= 1
    return unsorted_list
    
random_list = [random.randrange(1,101) for i in range(10)]

print(random_list)
print(bubble_sort(random_list))


    