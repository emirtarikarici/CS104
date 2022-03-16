#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 15:09:58 2021

@author: emirtarikarici
"""

common = []

# Define a function that takes 2 list and compare each other to find common elemets 
def common_sum(l1,l2):    
    l1 = set(l1)
    l2 = set(l2)
    
    for i in l1:
        if i in l2:
            common.append(i)

    print("The sum of common element of 2 list is", sum(common))
    
common_sum([17,7,13,11,4,19,17,6,4,1,3,6],[4, 16, 17, 8, 12, 14, 19])