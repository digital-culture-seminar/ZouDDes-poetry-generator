# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:10:06 2018

@author: junjiang
"""

import random

random.seed(4)

# whitespace
i = random.randint(6,10)
whitespace = " " * i

print whitespace + "hello world!"
