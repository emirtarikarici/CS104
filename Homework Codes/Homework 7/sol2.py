#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 21:14:05 2021

@author: emirtarikarici
"""

def pow_recursively(a,b):
    if b == 1:
        return a
    elif b == 0:
        return 1
    else:
        if b >1:    
            return  a * pow_recursively(a, b-1)
        elif b < 0:
            return 1 / a * pow_recursively(a, b+1)
    
print(pow_recursively(3, 4))