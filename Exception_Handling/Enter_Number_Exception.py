# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 14:52:28 2018

@author: joshu
"""

while True:
    
    try:
        number = int(input("Please enter a number : "))
        break
    
    except ValueError:
        print("You didnt enter a number!")
        
    except:
        print("An unknown error occured")

print("Thank you for entering a number: ", number)