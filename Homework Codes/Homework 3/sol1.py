#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:52:13 2021

@author: emirtarikarici
"""
def is_prime_number():
    number = int(input("Write a number: ")) 
    if number > 1:
 
    # Iterate from 2 to n / 2
        for i in range(2, int(number/2)+1):
 
        # If number is divisible by any number between 2 and n / 2, it is not prime
            if (number % i) == 0:
                return False
                break
        else:
            return True
 
    else:
        return False
     

print(is_prime_number())
        
        