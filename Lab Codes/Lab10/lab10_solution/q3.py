#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 13:57:18 2021

@author: emirtarikarici
"""

def prime(x):
    for i in range(1,x):
        if x % i != 0:
            return True
    else:
        return 