#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 23:25:15 2022

@author: emirtarikarici
"""

import random

n = 10  # Modify this for n = 10, 100, 1000, 10000, 100000, 1000000
f = open("numbers10.dat", "w")
for i in range(n):
    a = random.randint(1, 10000000)
    f.write(str(a) + "\n")
    
f.close()


