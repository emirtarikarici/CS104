#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 14:31:57 2021

@author: emirtarikarici
"""

class TeaCup:
    volume = 0.1
    temp = 30
    lemon = False
    
    def report():
        print("Volume: ", TeaCup.volume, "Temperature: ", TeaCup.temp, "Lemon: ", TeaCup.lemon, end="\n")
    
    def inc_temp():
        TeaCup.temp += 20
    def dec_temp():
        TeaCup.temp -= 20
    def inc_volume():
        TeaCup.volume += 0.1
    def add_lemon():
        TeaCup.lemon = True
    def takeout_lemon():
        TeaCup.lemon = False

c = TeaCup
print("Welcome to TeaCup recipe!") #START
c.report() #State 1
c.inc_temp()
c.report() #State 2
c.dec_temp()
c.report() #State 1
c.inc_volume()
c.report() #State 3
c.add_lemon()
c.report() #State 4
c.takeout_lemon() 
c.report() #State 3
c.add_lemon() 
c.report() #State 4
print("End of the recipe!") #STOP