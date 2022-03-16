#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 09:47:47 2021

@author: emirtarikarici
"""

with open("students.dat", "r") as student:
    studentlist = []
    for i in student:
        dictionary = {}
        row = i[:-1]
        split = row.split()
        if len(split) == 6:
            dictionary["number"] = str(split[0])
            dictionary["name"] = split[1]
            dictionary["surname"] = split[2]
            dictionary["birth"] = split[3]
            dictionary["department"] = split[4]
            dictionary["gpa"] = split[5]
            studentlist.append(dictionary)

            
def print_name(student_number):
    for i in studentlist:
        if student_number == i["number"]:
            print(i["name"])
        else:
            continue

def print_surname(student_number):
    for i in studentlist:
        if student_number == i["number"]:
            print(i["surname"])

    
def print_birth_place(student_number):
    for i in studentlist:
        if student_number == i["number"]:
            print(i["birth"])
    
def print_department(student_number):
    for i in studentlist:
        if student_number == i["number"]:
            print(i["department"])

def print_gpa(student_number):
    for i in studentlist:
        if student_number == i["number"]:
            print(i["gpa"])

print_name("13726146")
print_surname("13726146")
print_birth_place("13726146")
print_department("13726146")
print_gpa("13726146")