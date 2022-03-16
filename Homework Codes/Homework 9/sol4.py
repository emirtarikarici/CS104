#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 14:31:58 2021

@author: emirtarikarici
"""


class Student:
    def __init__(self,name,surname,birth_place,department,gpa):
        self.name = name
        self.surname = surname
        self.birth_place = birth_place
        self.department = department
        self.gpa = gpa             

    def print_name(self):
        print(self.name)
    def print_surname(self):
        print(self.surname)
    def print_birth_place(self):
        print(self.birth_place)
    def print_department(self):
        print(self.department)
    def print_gpa(self):
        print(self.gpa)
        
students = {}
with open("./students.dat", "r") as f:
    f.readline()
    f.readline()
    table = f.readlines()
    for record in table:
        fields = record.split()
        students[int(fields[0])] = Student(fields[1],fields[2],fields[3],fields[4],fields[5])

students[13726146].print_name()
students[30730594].print_surname()
students[81709043].print_birth_place()
students[23937852].print_department()
students[43447560].print_gpa()