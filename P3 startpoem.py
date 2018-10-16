# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:28:28 2018

@author: junjiang
"""

import markovify 

import random

random.seed ( )

# line break
print ""


# list of words

names = ["red", "orange", "yellow", "green", "brown", "blue", "purple", "pink", ]
feelings = ["chaos", "powerful", "gentle", "soft", "radiant", "splendid", "mystery",]

nouns = ["eyes", "toast", "ocean", "lenses", "sights", "nights"]
verbs = ["are", "like", "are", "depict"]
adjectives = ["curved", "dark", "deep", "rigid"]
#adverbs = ["and"]

#select random words from lists

name = random.choice(names)
feeling = random.choice(feelings)
noun = random.choice(nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)
#adverb = random.choice(adverbs)

#print a sentence with random words from the lists
print "{name} {feeling} {noun}".format(name=name, 
       feeling= feeling, noun=noun)

print ""

print "{verb} {adjective}".format(verb=verb, adjective=adjective)

print ""

g=open("poem.md","w")

g.write("{name} {feeling} {noun}".format(name=name, 
        feeling= feeling, noun=noun))

g.write("\n")

g.write("{verb} {adjective}".format(verb=verb, adjective=adjective))

g.write("\n")
g.close()


"""

Combine text from Fun with Mail -- Flame Manual and Petronius' Satyricon

"""

# get raw text as string

with open("texts/ColorRed.txt") as r:

    red = r.read()

with open("texts/ColorOrange.txt") as o:

    orange = o.read()    
    
with open("texts/ColorYellow.txt") as y:

    yellow = y.read()

with open("texts/ColorGreen.txt") as g:

    green = g.read()    
    
# build and combine the models
red_model = markovify.Text(red)
orange_model = markovify.Text(orange)
yellow_model = markovify.Text(yellow)
green_model = markovify.Text(green)

model_synthesis = markovify.combine([red_model, orange_model, yellow_model, green_model], 

    [ 1, 1, 1, 1])

# print five randomly-generated sentences

   
mylist = []
for i in range(0,5):
    mylist.append(model_synthesis.make_short_sentence(80))
    
for i in range(5):

    print model_synthesis.make_short_sentence(80)
    
with open("poem.md", "a") as w:
    for item in mylist:
        w.write(item)
        w.write("\n")
