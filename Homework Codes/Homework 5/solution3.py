#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 14:12:43 2021

@author: emirtarikarici
"""

A = (4,5,6)
B = (1,2,3,4)
C = (3)
D = (1,5,7)
E = (2,6,7)


Ver = {A, B, C, D, E}
Edg = {1, 2, 3, 4, 5, 6, 7}

vertex = {A:(4,5,6), B:(1,2,3,4), C:(3), D:(1,5,7), E:(2,6,7)}
edges = {1:("B","D"),2:("B","E"),3:("B","C"),4:("A","B"),5:("A","D"),6:("A","E"),7:("D","E")}

def give_edges(v):
    if v in set(Ver):
        return vertex[v]

def give_vertices(e):
    if e in set(Edg):
        return edges[e]

print(give_edges(A))
print(give_vertices(2))
