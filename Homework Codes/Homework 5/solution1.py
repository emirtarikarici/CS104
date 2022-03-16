#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 13:38:22 2021

@author: emirtarikarici
"""

A = {2,3,4,5,6,7,8}
B = {7,8,9,10}


def case_a(x):
    if x in A & B:
        return True
    elif x in (A - B) | (B - A):
        return False
    else:
        return True
    
    
def case_b(x):
    if x in (A - B) | (B - A):
        return True
    elif x in A & B:
        return False
    else:
        return False
    
def case_c(x):
    if x in A - B:
        return True
    else:
        return False
    
def case_d(x):
    if x in (A - B):
        return True
    elif x in B:
        return False
    else:
        return True

print(case_a(12))
print(case_b(12))
print(case_c(12))
print(case_d(12))