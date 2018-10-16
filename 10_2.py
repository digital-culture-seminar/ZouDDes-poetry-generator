# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 18:55:38 2018

@author: junjiang
"""

#import libraries

import markovify 



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
    mylist.append(fun_model.make_short_sentence(140))
    
with open("poem.md", "w") as w:
    for item in mylist:
        w.write(item)
        w.write("\n")