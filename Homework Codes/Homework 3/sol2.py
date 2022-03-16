#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 11:22:59 2021

@author: emirtarikarici
"""

pi = 3.141592
radii = int(input("Radius: "))
height = int(input("Height: "))

def area():
    area = (pi * radii ** 2) * 2
    return float(area)

def lateral():
    lateral = (2 * pi * radii) * height
    return float(lateral)

def surface():
    return area() + lateral()

print(area())
print(lateral())
print(surface())