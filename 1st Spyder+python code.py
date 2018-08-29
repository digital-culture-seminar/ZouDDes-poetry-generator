# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 19:27:49 2018

@author: junjiang
"""

"""
Author: Jun Zou
Description: python text generator
Liense: General 
"""

import random

random.seed(50)

# list of nouns
nouns=["sailor", 
       "ship", 
       "anchor", 
       "hfgjfsjd"]

#list of verbs
verbs=["files",
       "jumps",
       "sinks",
       "cherishes",
       "dreams",
       "terrorizes"]

#list of adjectives
adjectives=["blue",
            "frozen",
            "bullish"]

#select radom items from word lists
noun=random.choice(nouns)
verb=random.choice(verbs)
adjective=random.choice(adjectives)
second_adjective=random.choice(adjectives)

#word poem
print "The "+adjective+ " " + noun + " "

#for loop iterate through verbs
i=1
for verb in verbs:
    whitespace=" "*i
    print whitespace + verb
    i=i+1
    

##concatenation
#print "The "+adjectives+ " "+ noun + " " + verb
#
##string formation
#print 
#
#print verbs[2]

#i=0
#for noun in nouns:
#    print nouns[i]
#    i=i+1