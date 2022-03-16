#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:59:21 2021

@author: emirtarikarici
"""

def recaman(n):
    if n == 0:
        return [0]
    else: 
        seq = recaman(n-1)
        last = seq[-1] - n
        if last > 0 and last not in seq:
            seq.append(last)
        else:
            seq.append(seq[-1] + n)
    return seq
print(recaman(10))

