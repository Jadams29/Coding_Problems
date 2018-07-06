# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 19:45:54 2018

@author: joshu
"""
import math

def get_area(shape):
    shape = shape.lower()
    if shape == 'rectangle':
        rectangle_area()
    elif shape == 'circle':
        circle_area()
    else:
        print("Please enter rectangle or circle ")
        
def rectangle_area():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    
    area = length * width
    print("The area of the rectanle is {:.2f}".format(area))
    
def circle_area():
    radius = float(input("Enter the radius: "))
    
    area = math.pi * (math.pow(radius,2))
    print("The area of the circle is {:.2f}".format(area))
    
    
    

def main():
    shape_type = input("Get area for what shape: ")
    get_area(shape_type)
        
main()