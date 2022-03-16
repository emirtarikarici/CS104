#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 21:19:07 2021

@author: emirtarikarici
"""
# define a for loop b/w 1 to 71 (20th prime number)
for p in range(1,72):
# prime numbers are only divisible by 1 and itself 
    if p == 1:
        continue
    if p / 2 == p // 2:
        if p / 2 == 1:
            print(p)
            continue
    elif p / 3 == p // 3:     
        if p / 3 == 1:
            print(p)
            continue
    elif p / 5 == p // 5:     
        if p / 5 == 1:
            print(p)
            continue 
    elif p / 7 == p // 7:     
        if p / 7 == 1:
            print(p)
            continue
    else:
        print(p)