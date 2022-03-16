#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 10:04:50 2021

@author: emirtarikarici
"""

quotes = "quotes.txt"

with open(quotes, "r") as q:
    read = q.read()
    read = read.replace(" ", "")
    read = read.replace("\n", "")
    read = read.replace(":", "")
    read = read.replace(";", "")
    read = read.replace(",", "")
    read = read.replace(".", "")
    read = read.lower()


count = {}
def letter_count(string):
    for i in string:
        keys = count.keys()
        if i in keys:
            count[i] += 1
        else:
            count[i] = 1
    return count
letter_count(sorted(read))


with open("letters.txt","w") as l:
    for i in count:
        l.write(str(i) + " ")
        l.write(str(count[i]))
        l.write("\n")
