#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:28:38 2021

@author: emirtarikarici
"""
while True:
    try:
        mylist = [10, 45, 67, 3, 98]
        a = input("Enter a: ")
        b = input("Enter b: ")
        print(mylist[int(a) // int(b)])
    except ValueError:
        print("You should write a number. Try again.")
        continue
    except ZeroDivisionError:
        print("You can't write 0 to b. Try again.")
        continue
    except IndexError:
        print("The result is out of the range of list. Try again.")
        continue
    else:
        break