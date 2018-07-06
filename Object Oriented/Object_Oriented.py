# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 21:33:23 2018

@author: joshu
"""

import os
import random
import math

# Real World Objects: Attributes & Capabilities

# Dog(Object) : 
# Dog(Attributes) : Height, Weight, Favorite Food
# Dog(Capabilities) : Run, Walk, Eat


class Dog:
    def __init__(self, name ='', height = 0, weight = 0):
        self.name = name
        self.height = height
        self.weight = weight
        
    def run(self):
        print("{} the dog runs".format(self.name))
        
    def eat(self):
        print("{} the dog eats".format(self.name))
        
    def bark(self):
        print("{} the dog barks".format(self.name))



def main():
    spot = Dog('Spot', 66, 26)
    
    spot.bark()
    
    bowser = Dog('Bowser')
    
    bowser.bark()
    
main()





