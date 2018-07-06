# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 15:20:42 2018

@author: joshu
"""

sample_string = "This is a very important string"

print(sample_string[:-6])
print(sample_string[-6:])
print(sample_string[10:14])

new_string = sample_string.split(" ")

print(new_string)


# Print characters in pairs
for i in range(0, len(sample_string) - 1, 2):
    print(sample_string[i] + sample_string[i + 1])
   
    
# UNICODE
# A - Z -> 65 - 90
# a - z -> 97 - 122
    
# Alphabet to unicode
print("A = ", ord("A"))
# Unicode to Alphabet 
print("65 = ", chr(65))