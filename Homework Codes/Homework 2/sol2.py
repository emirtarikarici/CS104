"""
Created on Mon Oct 18 18:36:22 2021

@author: emirtarikarici
"""
#Create an empty list in a variable, numberList
numberList = []

#when it takes a positive number, the loop adds this number to the list
while True:
    nmbr = int(input("Write a number: "))
    if nmbr >= 0:
        numberList.append(nmbr)
        print(numberList)
        continue
    # when it takes a negative number, the loop stops and sum all the previous numbers, then it prints
    else:
        print(sum(numberList))
        break
