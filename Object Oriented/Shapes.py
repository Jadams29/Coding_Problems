# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 21:42:42 2018

@author: joshu
"""

import random
import math
import os

class Square:
    
    def __init__(self, height = '0', width = '0'):
        self.height = height
        self.width = width
    
    @property
    def height(self):
        print("Retrieving the Height")
        return self.__height
    
    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print('Please only enter numbers for height')
    
    @property
    def width(self):
        print("Retrieving the width")
        return self.__width
    
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")
            
    def getArea(self):
        return (int(self.__width) * int(self.__height))

def main():
    aSquare = Square()
    
    height = input("Enter Height : ")
    width = input("Enter Width : ")
    
    aSquare.height = height
    aSquare.width = width
    
    print("Height: {}".format(aSquare.height))
    print("Width: {}".format(aSquare.width))
    print("Area: {}".format(aSquare.getArea()))    
        
        
main()      
        
        
        
        
        
        
        