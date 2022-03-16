#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:59:21 2021

@author: emirtarikarici
"""

import time, random


def linear_search(data, value):
    for index in range(len(data)):
        if value == data[index]:
            return index
    raise ValueError('Value not found in the list')

def binary_search(data, value):
    n = len(data)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle
    raise ValueError('Value is not in the list')

print("%-20s%-50s"%("VALUE","PERFORMANCE OF LINEAR SEARCH"))
if __name__ == '__main__':
    try:
        n = [10, 100, 1000, 10000, 1000000, 10000000]
        for i in n:
            data = range(1, i)
            for j in range(10):
                value_to_look_for = random.randint(1, i-1)
                start = time.time()
                linear_search(data, value_to_look_for)
                end = time.time()
                print("%-20i%-50f"%(value_to_look_for,end-start))
    except ValueError:
        print("Value is not in data")

print()

print("%-20s%-50s"%("VALUE","PERFORMANCE OF BINARY SEARCH"))
if __name__ == '__main__':
    try:
        n = [10, 100, 1000, 10000, 1000000, 10000000]
        for i in n:
            data = range(1, i)
            for j in range(10):
                value_to_look_for = random.randint(1, i-1)
                start = time.time()
                binary_search(data, value_to_look_for)
                end = time.time()
                print("%-20i%-50f"%(value_to_look_for,end-start))
    except ValueError:
        print("Value is not in data")
        
print("""
      \nThe performance of linear and binary search while using the little numbers is almost the same.
But when the value of numbers are increasing, the binary search is faster than the linear search.
      """)


