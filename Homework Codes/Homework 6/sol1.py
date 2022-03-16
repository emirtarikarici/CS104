#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:11:04 2021

@author: emirtarikarici
"""

import os

listDir = os.listdir()
print(listDir,"\n")


os.mkdir("cs104")
os.chdir("cs104")
cwdCS104 = os.getcwd()
print(cwdCS104,"\n")

with open("notes.txt", "w") as notes:
    notes.write("I like computer programming.")
with open("notes.txt", "r") as notes:
    read = notes.read()
    print(read,"\n")

os.mkdir("slides")
os.chdir("slides")
cwd = os.getcwd()
print(cwd,"\n")

with open("lecture1.txt", "w") as lec1:
    lec1.write('lecture 1: \n"Introduction"')
with open("lecture1.txt", "r") as lec1:
    read = lec1.read()
    print(read,"\n")

os.chdir(cwdCS104)
cwd = os.getcwd()
print(cwd,"\n")

os.mkdir("labs")
os.chdir("labs")
cwd = os.getcwd()
print(cwd,"\n")

os.mkdir("lab01")
os.mkdir("lab02")
os.chdir("lab02")
os.mkdir("solutions")
os.chdir("solutions")
cwd = os.getcwd()
print(cwd,"\n")

with open("solution.py", "w") as sol:
    sol.write('print("hello") \nfor i in range(5): \n\tprint(i**2)')
with open("solution.py", "r") as sol:
    read = sol.read()
    print(read,"\n")