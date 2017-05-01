# -*- coding: utf-8 -*-
"""
Created on Mon May  1 23:04:00 2017

@author: Karen
"""
import random
def rps (p1, p2):
    #Draw cases
    
    if (p1 == 0) and (p2 == 0):
        return("Draw!")
    if (p1 == 1) and (p2 == 1):
        return("Draw!")
    if (p1 == 2) and (p2 == 2):
        return("Draw!")
    
    #Player 1 wins
    #rock beats scissors
    if p1 == 0 and p2 == 2:
        return("Player 1 won!")
    #paper wraps rock
    if p1 == 1 and p2 == 0:
        return("Player 1 won!")
    #scissors cut paper
    if p1 == 2 and p2 == 1:
        return("Player 1 won!")
    
    #Player 2 wins
    #rock beats scissors
    if p2 == 0 and p1 == 2:
        return("Player 2 won!")
    #paper wraps rock
    if p2 == 1 and p1 == 0:
        return("Player 2 won!")
    #scissors cut paper
    if p2 == 2 and p1 == 1:
        return("Player 2 won!")
while True:  
    p1 = random.randint(0,2)
#int(input("Player 1. Input 0 for rock, 1 for paper, or 2 for scissors: "))

    p2 = random.randint(0,2)
#int(input("Player 2. Input 0 for rock, 1 for paper, or 2 for scissors: "))
    print(rps(p1,p2))