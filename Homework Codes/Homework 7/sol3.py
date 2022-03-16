#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:50:08 2021

@author: emirtarikarici
"""

result = 0
def sum_recursively(l):
    global result
    if len(l) == 0:
        return result
    elif len(l) == 1:
        result += l[0]
        return result
    else:
        result += l[0]
        l.remove(l[0])
        return sum_recursively(l)
     
mylist = [19, 5, 6, 8]
print(sum_recursively(mylist))