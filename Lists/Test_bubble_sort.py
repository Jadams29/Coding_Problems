# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 09:23:53 2018

@author: joshu
"""
import random
# 1. An outer loop decreases in size each time
# 2. The goal is to have the largest number at the end of the list
#        when the outer loop completes 1 cycle
# 3. The inner loop starts comparing indexes at the beginning of the loop
# 4. Check if list[Index] > list[Index + 1]
# 5. If so swap the index values
# 6. When the inner loop completes the largest number is at the end
#        of the list
# 7. Decrement the outer loop by 1

def bubble_sort(unsorted_list):
    # Length of the list
    i = len(unsorted_list) - 1

    while i > 1:
        # Iterator for innerloop
        k = 0
        while k < i:
            if unsorted_list[k] > unsorted_list[k + 1]:
                # swap
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
