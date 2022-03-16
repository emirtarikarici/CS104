#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 13:43:44 2021

@author: emirtarikarici
"""


def population(x):
    if x == 0:
        return 1000000
    else:
        return population(x-1) * 1.01 + 1000 
        
print(population(10))