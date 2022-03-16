#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:19:30 2021

@author: emirtarikarici
"""


matrix = []
for i in range(1,6,2):
    row = []
    for j in range(2):
        row.append(i+j)
    matrix.append(row)
print(matrix)

matrix2 = []
for i in range(1,10,3):
    row = []
    for j in range (3):
        if j % 2 == 0:
            row.append(i+j)
        else:
            row.append(i+j)
    matrix2.append(row)
print(matrix2)