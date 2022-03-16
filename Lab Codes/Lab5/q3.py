#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:03:50 2021

@author: emirtarikarici
"""

n1 = int(input("First positive integer: "))
n2 = int(input("Second positive integer: "))

commonDivList = []

def commonDivs():    
    for i in range(1, min(n1,n2) + 1):
        if n1 % i == n2 % i == 0:
            commonDivList.append(i)
    print(commonDivList)

commonDivs()