#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 14:31:56 2021

@author: emirtarikarici
"""
import math

class Circle():
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
    
    def touches(self,c):
        hyp = math.sqrt(((self.x - c.x) ** 2) + ((self.y - c.y) ** 2))
        sum_rad = (self.r + c.r)
        
        if hyp == sum_rad:
            return True
        else:
            return False
        
#Case 1: False
c1 = Circle(0,0,3)
c2 = Circle(4,6,3)
print(c1.touches(c2))
#Case 2: True
c3 = Circle(0,0,3)
c4 = Circle(3,4,2)
print(c3.touches(c4))
#Case 3: False
c5 = Circle(0,0,1)
c6 = Circle(1,2,4)
print(c5.touches(c6))
#Case 4: False
c7 = Circle(0,0,1)
c8 = Circle(0,2,2)
print(c7.touches(c8))
#Case 5: False
c9 = Circle(0,0,1)
c10 = Circle(-1,-1,3)
print(c9.touches(c10))