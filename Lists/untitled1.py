# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 09:38:48 2018

@author: joshu
"""
import random

def bubble_sort(unsorted_list):
    i = len(unsorted_list) - 1
    
    while i > 1:
        j = 0 
        while j < i:
            #print("\nIs {} > {}".format(unsorted_list[j], unsorted_list[j + 1]))
            if unsorted_list[j] > unsorted_list[j + 1]:
                #print("Swap")
                temp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j + 1]
                unsorted_list[j + 1] = temp
            else:
                j += 1
                
            #for k in unsorted_list:
                #print(k, end=', ')
            #print()
        #print("END OF ROUND")
        i -= 1
    return unsorted_list


random_list = [random.randrange(1,100) for i in range(10)]

print(random_list)

print(bubble_sort(random_list))