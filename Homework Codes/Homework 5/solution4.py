#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 14:13:06 2021

@author: emirtarikarici
"""

enFr = {'bread':"pain", "wine":"vin", "bring":"apporter", "I":"Je",
        "eat": "mange", "drink":"bois", "John-Michael":"Jean-Michel", 
        'friends':'amis', "and":"et", "of":"du", "red": "rouge", "from": "de",
        "town":"ville", "we":"nous", "Mary":"Marie",
        "For":"Pour", "years":"ans"}

def en_to_fr():
    sent1 = str(enFr["John-Michael"] + " " + enFr["and"] + "," +  " " + enFr["friends"] + " " + enFr["from"] + " " + enFr["town"] + " " + enFr["drink"] + " " + enFr["wine"] + ".")
    print(sent1)
    
    sent2 = str(enFr["I"] + " " + enFr["eat"]+ " " + enFr["bread"] + "!")
    print(sent2)
    
    sent3 = str(enFr["For"] + " " + "5" + " " + enFr["years"] + "," + " " + enFr["we"] + " " + enFr["bring"] + " " + enFr["red"] + " " + enFr["wine"] + " " + enFr["from"] + " " + enFr["town"] + " " + enFr["from"] + " " + enFr["Mary"] + ".")
    print(sent3)
    
    
    
en_to_fr()
