#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 15:07:02 2021

@author: emirtarikarici
"""

num = input("Number: ")
num = int(num)
assert type(num) == int, "Input is not integer"


def luhn_sum(n):
    """Return the digit sum of n computed by the Luhn algorithm"""
    assert type(n) == int, "n is not integer"
    assert n > 0, "n is not greater than 0" 
    if n < 10:
       return n
    else:
       all_but_last, last = split(n)
       tup = all_but_last, last
       assert type(tup) == tuple, "tup is not tuple"
       return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    """Return the Luhn sum of n, doubling the last digit."""
    assert type(n) == int, "n is not integer"
    assert n > 0, "n is not greater than 0" 
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
       return luhn_digit
    else:
       return luhn_sum(all_but_last) + luhn_digit
   
def split(n):
    """Split positive n into all but its last digit and its last digit."""
    assert type(n) == int, "n is not integer"
    assert n > 0, "n is not greater than 0" 
    return n // 10, n % 10

def sum_digits(n):
    """Return the sum of the digits of positive integer n."""
    assert type(n) == int, "n is not integer"
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        tup = all_but_last, last
        assert type(tup) == tuple, "tup is not tuple"
        return sum_digits(all_but_last) + last

result = luhn_sum(num)
print(result)
print("This number is valid for Luhn Algorithm")
assert result % 10 == 0, "This number is not True for Luhn Algorithm"