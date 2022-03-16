#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:53:52 2021

@author: emirtarikarici
"""


def gcd(int1,int2):
    if int(int2) == 0:
        return int1
    else:
        return gcd(int2, int1 % int2)
        
print(gcd(100, 15))