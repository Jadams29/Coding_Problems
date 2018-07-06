# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 22:18:36 2018

@author: joshu
"""

import random
import math

# Warrior & Battle class

# Warriors will have names, health, attack and block maximums
# They have the capabilities to attack and block random amounts
# 
# Attack will use random() 0.0-1.0 * maxAttack + 0.5
# Block will use random() * maxBlock

# Battle Class capability of looping until 1 warrior dies
# Warriors will each get a turn to attack each other

# Function for attacking
# 1 warrior attacks another 

class Warrior:
    def __init__(self, name = 'Warrior', health = 0, attackMax = 0, blockMax = 0):
        self.name = name
        self.health = health
        self.attackMax = attackMax
        self.blockMax = blockMax
    
    def attack(self):
        attackAmt = self.attackMax * (random.random() + 0.5)
        return attackAmt
    
    def block(self):
        blockAmt = self.blockMax * (random.random() + 0.5)
        return blockAmt
    
class Battle:
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == 'Game Over':
                print('Game Over')
                break
            
            if self.getAttackResult(warrior2, warrior1) == 'Game Over':
                print('Game Over')
                break
            
    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorA_AttackAmt = warriorA.attack()
        warriorB_BlockAmt = warriorB.block()
        damageToWarriorB = math.ceil(warriorA_AttackAmt - warriorB_BlockAmt)
        
        warriorB.health = warriorB.health - damageToWarriorB
        
        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, damageToWarriorB))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))
        
        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"
        
def main():
    
    maximus = Warrior("Maximus", 50, 20, 10)
    galaxon = Warrior("Galaxon", 50, 20, 10)
    
    battle = Battle()
    battle.startFight(maximus, galaxon)
    
main()

