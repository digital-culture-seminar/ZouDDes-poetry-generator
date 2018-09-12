# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 21:58:38 2018

@author: junjiang

Exercise repeat 1
Author: Jun Zou
Copyright: GNU General Public License V2.

"""
import random

# set the random seed
random.seed()

# line break
print ""

# list of words
nouns = ["my", "eyes", "toast", "ocean", "lenses", "sights", "nights"]
second_nouns = ["eyes", "toast", "ocean", "lenses", "sights", "nights"]
verbs = ["are", "like", "are", "depict"]
adjectives = ["curved", "dark", "deep", "rigid"]
adverbs = ["and"]

#select random words from lists
noun = random.choice(nouns)
second_noun = random.choice(second_nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)
adverb = random.choice(adverbs)

#print a sentence with random words from the lists
print "{noun} {adverb} {second_noun} {verb} {adjective}.".format(noun=noun,adverb=adverb,
       second_noun=second_noun, verb=verb, adjective=adjective)

#select random words from lists
noun = random.choice(nouns)
second_noun = random.choice(second_nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)
adverb = random.choice(adverbs)

#print a sentence with random words from the lists
print "{noun} {adverb} {second_noun} {verb} {adjective}.".format(noun=noun,adverb=adverb,
       second_noun=second_noun, verb=verb, adjective=adjective)

#line break
print ""

#shuffle the list of adjectves
random.shuffle(adjectives)

#print the shuffled list of adjectives with increasing whitespace
i = 0
print "The"
for adjectives in adjectives:
    i = i + 2
    whitespace = " " * i
    print whitespace + adjective
    
## print the rest of the sentence
#    print "{noun} {verb}.".format(noun=noun, verb=verb)
               
            


