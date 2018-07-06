# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 20:23:04 2018

@author: joshu
"""

import random
import math
import os

with open('mydata.txt', mode = 'w', encoding = 'utf-8') as myFile:
    myFile.write('Some random text\nMore random text\nAnd some more')
    
with open('mydata.txt', encoding = 'utf-8') as myFile:
    # Print lines of text file
    print(myFile.read())
    
# Returns True/False based on if the file is closed or not
print(myFile.closed)

# Returns the name of the file
print(myFile.name)

# Returns the last used mode
print(myFile.mode)

# Rename a file
os.rename('mydata.txt', 'mydata2.txt')

# Remove a file
os.remove('mydata2.txt')

# Create a directory
os.mkdir("mydir")

# Change to a directory
os.chdir('mydir')

# Returns current working directory
print("Current Directory: {}".format(os.getcwd()))

# Before the removal of a directory, move out of that directory
# Moving back one directory

print("Current Directory: {}".format(os.getcwd()))

# Remove directory
os.rmdir('mydir')


