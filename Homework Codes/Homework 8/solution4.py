#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:59:22 2021

@author: emirtarikarici
"""

import time


def fib_rec(n):
    if n <= 1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

    
def fib_nonrec(n):
    g = (1 + 5**.5) / 2
    return int((g**n - (1-g)**n) / 5**.5)

        
def golden_rec(n):
    return fib_rec(n) / fib_rec(n-1)

def golden_nonrec(n):
    return fib_nonrec(n) / fib_nonrec(n-1)


print("%-20s%-20s%-1000s"%("n","GOLDEN RATIO", "PERFORMANCE OF RECURSIVE Fn"))
for i in range(2,20):
    start = time.time()
    golden_rec(i)
    end = time.time()
    print("%-20s%-20f%-50f"%(i,golden_rec(i), end-start))

print()

print("%-20s%-20s%-1000s"%("n","GOLDEN RATIO", "PERFORMANCE OF NON-RECURSIVE Fn"))
for i in range(2,20):
    start = time.time()
    golden_nonrec(i)
    end = time.time()
    print("%-20i%-20f%-1000f"%(i,golden_nonrec(i), end-start))

print("""
The non-recursive function has much more high performance than recursive one.
      """)




