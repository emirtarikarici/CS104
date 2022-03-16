#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 14:07:55 2021

@author: emirtarikarici
"""

matrix = [[1, 2], [-1, 1]]

vector = [5, 4]

def mat_vec_product(): 
    product = [[sum(i * j for i,j in zip(matrix_r,vector_c)) for vector_c in vector] for matrix_r in matrix]
    print(product)

mat_vec_product()