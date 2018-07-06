# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 12:45:31 2018

@author: joshu
"""

# How tall is the tree : 5

    #    
   ###   
  #####  
 #######
#########
    #           

# Use 1 while loop and 3 for loops
# Line 1 = 4 spaces : 1 hash
# Line 2 = 3 spaces : 3 hash
# Line 3 = 2 spaces : 5 hash
# Line 4 = 1 space  : 7 hash
# Line 5 = 0 space  : 9 hash
# Line 6 = 4 spaces : 1 hash


height = eval(input("How tall is the tree? "))
#print()
#
#spaces = height
#i = 1
#while spaces > 0:
#    print(" " * (spaces - 1), end='')
#    print("#" * i)
#    spaces -= 1
#    i += 2
#print(" " * (height - 1), end='')
#print("#")

      


      
# Need to do
# 1. Decrement spaces by 1 each time through the loop
# 2. Increment the hashes by 2 each time through the loop
# 3. Save spaces to the stump by calculating tree height - 1
# 4. Decrement from tree height until it equals 0
# 5. Print spaces and then hashes for each row
# 6. Print stump spaces then 1 hash


hashes = 1
stump = 0

while (height > 0):
    spaces = height - 1
    print(" " * spaces, end='')
    print("#" * hashes)
    hashes += 2
    height -= 1
    stump += 1
print(" " * (stump - 1), end='')
print("#")