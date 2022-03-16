#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:59:18 2021

@author: emirtarikarici
"""



rev = 0
def isPalindrome(num):
    def reverse(num):
        global rev
        if num == 0:
            return rev
        elif num < 0:
            return reverse(abs(num))
        else:
            if num > 0:
                rev = (rev * 10) + (num % 10)
                num = num // 10
                return reverse(num)
    if reverse(num) == num:
        return True
    else:
        return False
print(isPalindrome(121))
