#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 13:44:39 2021

@author: emirtarikarici
"""

def isbn_check(isbn):
    # ISBN code must be 10 digit
    if len(isbn) != 10:
        return False
    
    list_isbn = list(isbn)
    isbn_10 = 0
    # ISBN-10 
    for i in range(1,11):
        isbn_10 += int(int(list_isbn[i - 1]) * (11 - i))
    if isbn_10 % 11 == 0:
        return True
    else:
        return False

        
isbn = "0536000069"
print(isbn_check(isbn))