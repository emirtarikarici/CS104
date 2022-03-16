#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 22:11:24 2021

@author: emirtarikarici
"""

def knight(x0, y0):
    moves = [[-1, +2], [-2, +1], [-2, -1], [-1, -2], [+1, -2], [+2, -1], [+2, +1], [+1, +2]]
    position = []
    for x, y in moves:
        result_x = x0 + x
        result_y = y0 + y
        if 0 < result_x < 8 and 0 < result_y < 8:
            position.append([result_x, result_y])

    return position

print(knight(3,4))