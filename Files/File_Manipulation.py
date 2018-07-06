# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 20:48:53 2018

@author: joshu
"""

import os

with open('mydata.txt', mode = 'w', encoding = 'UTF-8') as myFile:
    myFile.write("Some Random Text\nMore Random Text\nAnd Some More\n")


with open('mydata.txt', encoding = 'UTF-8') as myFile:
    
    lineNum = 1
    while True:
        line = myFile.readline()
        if not line:
            break
        temp = line.split()
        print('line', lineNum, ' : ', line, 'Number of Words: {}'.format(len(temp)), end='')
        print(" Average length of the word: {:.2f}".format((len(temp[0])+len(temp[1])+len(temp[2]))/len(temp)))
        print()
        lineNum += 1
        
        
        
