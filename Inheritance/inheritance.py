# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:28:02 2018

@author: joshu
"""

import os
import math
import random

class Animal:
    def __init__(self, birthType = 'Unknown',
                 appearance = 'Unknown', blooded = 'Unknown'):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded
        
        
    @property
    def birthType(self):
        return self.__birthType
    
    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType
        
    @property
    def appearance(self):
        return self.__appearance
    
    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance
        
    @property
    def blooded(self):
        return self.__blooded
    
    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded
        
    # Magic Method 
    
    def __str__(self):
        return "A {} is {} it is {} and it is {}".format(type(self).__name__,
                  self.birthType, self.appearance, self.blooded)
        
class Mammal(Animal):
    def __init__(self, birthType = "Born Alive", appearance = "Hair or Fur",
                 blooded = "Warm Blooded", nurseYoung = True):
        Animal.__init__(self, birthType, appearance, blooded)
        self.__nurseYoung = nurseYoung
            
    @property
    def nurseYoung(self):
        return self.__nurseYoung
    
    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung
    
    def __str__(self):
        return super().__str__() + " and it is {} they nurse their young".format(self.nurseYoung)

class Reptile(Animal):
    def __init__(self, birthType = "Born in an egg or born alive",
                 appearance = "Dry scales",
                 blooded = "Cold Blooded"):
        Animal.__init__(self, birthType, appearance, blooded)

def getBirthType(theObject):
        print("The {} is {}".format(type(theObject).__name__,
                                    theObject.birthType))
def main():
    animal1 = Animal("born alive")
    
    print(animal1.birthType)
    
    print(animal1)
    print()
    
    mammal1 = Mammal()
    print(mammal1.birthType)
    print(mammal1)
    print()

    reptile1 = Reptile()
    print(reptile1.birthType)
    print(reptile1)

    getBirthType(mammal1)
    getBirthType(reptile1)





    
main()





