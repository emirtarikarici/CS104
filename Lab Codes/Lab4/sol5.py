#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:02:00 2021

@author: emirtarikarici
"""


def factorial(x):
    n = int(input("Write a number: "))
    factorial = 1
    
    if n < 0:
        print("Write a positive number.")
    elif n == 0:
        print("The factorial of 0 is 1.")
    else:
        for i in range(1,n + 1):
            factorial = factorial * i
        print("The factorial of" , n , "is" ,factorial)



def combination():
    n = int(input("n ="))
    k = int(input("k ="))
    
    combination = factorial(n) / factorial(n - k) * factorial(k)
    return combination

combination()