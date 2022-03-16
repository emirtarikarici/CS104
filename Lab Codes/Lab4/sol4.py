#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:46:16 2021

@author: emirtarikarici
"""


    


def volume():
    r = int(input("Radius: "))
    pi = 3.14159
    
    volume = (4 / 3) * pi * r ** 3
    return volume

print(volume())