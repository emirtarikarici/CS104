#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:00:04 2021

@author: emirtarikarici
"""

#\oooooooo/
# \oooooo/
#  \oooo/
#   \oo/
#    \/
#    /\
#   /oo\
#  /oooo\
# /oooooo\
#/oooooooo\
    
def up2():
    for i in range(1,11,):
        for j in range(1,i):
            print("\\", end="")
        for j in range(1, 2*i):
            print("o", end="")
        print()    
        
up2()