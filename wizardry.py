# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 22:58:20 2017

@author: Karen
"""

#wizard_list = "spider legs, toe of frog, eye of newt, bat wing, slug butter, snake dandruff"
#print(wizard_list)
wizard_list = ["spider legs", "toe of frog", "eye of newt", "bat wing", "slug butter", "snake dandruff"]
print(wizard_list)
print(wizard_list[2])

wizard_list[2] = "snail tongue"
print(wizard_list)
print(wizard_list[2:5])

wizard_list.append("bear tail")
wizard_list.append("mandrake")
wizard_list.append("swamp gas")
print(wizard_list)

del wizard_list[5]
print(wizard_list)