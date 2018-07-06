# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 21:56:51 2018

@author: joshu
"""

import os
import random
import math

# Sam attacks Paul and deals 9 damage
# Paul is down to 10 health
# Paul attacks Sam and deals 7 damage
# Sam is down to 7 health
# Sam attacks Paul and deals 19 damage
# Paul is down to -9 health
# Paul has died and Sam is Victorius
# Game Over


class Warrior:
    def __init__(self, name = '', health = 0):
        self.health = health
        self.name = name
    
    def attack(self, victim):
        damage = random.randrange(1,20)
        print("{} attack {} for {} damage ".format(self.name, victim.name, damage))
        return damage
    
#    @property
    def getHealth(self):
        print("{} is down to {} health".format(self.name, self.health))
        return
    
#    @health.setter
    def setHealth(self, value):
        if value.isdigit():
            self.__health = value
        else:
            print("Please enter a valid number")
            
    def getName(self):
        return self.name
        
        
    

def main():
    warrior1, health1 = input("Enter Warrior1 name and health: ").split()
    warrior2, health2 = input("Enter Warrior2 name and health: ").split()
    warrior1 = Warrior(warrior1, health1)
    warrior2 = Warrior(warrior2, health2)
    
    warrior1.attack(warrior2)
    warrior2.getHealth()

main()
        
        
        
        