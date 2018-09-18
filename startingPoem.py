# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:23:33 2018

@author: junjiang
"""

import random

names = ["hands", "mind"]
pronouns = ["he", "she", "it"]

# indexing list
print pronouns[1]

name = random.choice(names)
pronoun = random.choice(pronouns)

##print th opening lines of the story
#print "cold in the classroom \ busy at python work \ my {name} goes on and on \
#{pronoun} has interesting time".format(name=name, pronoun=pronoun.capitalize())

roll = random.randint(1,6)
print "{name} rolled a {roll}".format(name=name, roll=roll)

if roll == 1:
    print "bad luck!"
    
elif roll == 6 or name == "Action":
    print "good luck!"
    
else:
    print "not so bad luck ..."

#    print "Success! " + pronoun + " rolled a " + str(roll)
#    print "Success! {pronoun} rolled  {roll}".format(pronoun=pronoun, roll=roll)
    

#print pronoun.capitalize() + " " + name

## import libraries
#import random
#random.seed()
#
## assign variables
#names = ["Cloudy", "Echo", "Action"]
#name = random.choice(names)
#pronouns = ["he", "she"]
#pronoun = random.choice(pronouns)
#
## print the opening lines of the story
#print "One summer evening over cold beer and roasted peanuts \
#    my young friend {name} told me story. \
#    {pronoun} had gone to a fortune teller in the old town, \
#    paid with a fistful of crumpled old bills, \
#    and was handed a single die.\
#    ".format(name=name, pronoun=pronoun.capitalize())