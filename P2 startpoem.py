# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 22:31:04 2018

@author: junjiang
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 20:37:34 2018

script color and feeling poem
@author: junjiang
liense 
"""
import markovify 

import random

random.seed ( )

# line break
print ""


# list of words
minds = ["Plato", "Newton", "Da Vinci", "Goethe", "Einstein"]
nouns = ["sky", "grass", "rose"]
names = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "earth", ]
feelings = ["chaos", "powerful", "gentle", "soft", "radiant", "splendid", "mystery",]

second_nouns = ["eyes", "toast", "ocean", "lenses", "sights", "nights"]
verbs = ["are", "like", "are", "depict"]
adjectives = ["curved", "dark", "deep", "rigid"]
adverbs = ["and"]

#select random words from lists
mind = random.choice(minds)
name = random.choice(names)
feeling = random.choice(feelings)
noun = random.choice(nouns)
second_noun = random.choice(second_nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)
adverb = random.choice(adverbs)

#print a sentence with random words from the lists
print "{mind} {name} {feeling} {noun} {adverb} {second_noun} {verb} {adjective}.".format(mind=mind, name=name, feeling= feeling, noun=noun,adverb=adverb,
    second_noun=second_noun, verb=verb, adjective=adjective)

g=open("poem.md","w+")

g.write("{mind} {name} {feeling} {noun} {adverb} {second_noun} {verb} {adjective}.".format(mind=mind, name=name, feeling= feeling, noun=noun,adverb=adverb,
    second_noun=second_noun, verb=verb, adjective=adjective))

g.write("\n")

g.close()


"""

Combine text from Fun with Mail -- Flame Manual and Petronius' Satyricon

"""

# get raw text as string

with open("texts/Fun with Mail -- Flame Manual.txt") as f:

    fun = f.read()

with open("texts/For the AIlist.txt") as a:

    ailist = a.read()    
    
# build and combine the models
fun_model = markovify.Text(fun)

ailist_model = markovify.Text(ailist)

model_synthesis = markovify.combine([fun_model, ailist_model], 

    [ 1.5, 1 ])

# print five randomly-generated sentences

for i in range(5):

    print model_synthesis.make_sentence()
    
mylist = []
for i in range(0,5):
    mylist.append(model_synthesis.make_short_sentence(140))
    
with open("poem.md", "a") as w:
    for item in mylist:
        w.write(item)
        w.write("\n")



#singletext_model = markovify.Text(minds)

#mylist = []
#for i in range(0,5):
#    mylist.append(singletext_model.make_short_sentence(140))
    
#with open("poem.md", "w") as w:
#    for item in mylist:
 #       w.write(item)
 #       w.write("\n")
        