#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 22:11:22 2021

@author: emirtarikarici
"""


def symmetric(matrix, n):
    for i in range(n):
        for j in range(n):
            if (matrix[i][j] != matrix[j][i]):
                return False
    return True
    

matrix = [[ 11, 2, 13, 1 ], 
          [ 2, 10, 5, 24 ],
          [ 13, 5, 3, 4  ],
          [ 1, 24, 4, 47 ] ]



print(symmetric(matrix, 4))
print(matrix[0][0],matrix[1][1],matrix[2][2],matrix[3][3])