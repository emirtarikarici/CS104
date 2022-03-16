#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 14:31:57 2021

@author: emirtarikarici
"""

class Car:
    odometer = 0
    gear = 0
    def __init__(self,brand,color,gear):
        self.brand = brand
        self.color = color
        self.gear = gear
    
    def increment_gear(self):
        Car.self.gear += 1
    def decrement_gear(self):
        Car.self.gear -= 1
    def drive(self,hr,km):
        Car.odometer = km * hr
        return Car.odometer
    def display(self):
        print("Features of the car","Brand:",self.brand,"Odometer:",self.odometer,"Color:", self.color,"Gear:",self.gear,sep="\n")

def test():
    car1 = Car("Ferrari","Red",8)
    car1.drive(80, 100)
    car1.display()
    print()
    car2 = Car("Toyota","Grey",8)
    car2.drive(50, 200)
    car2.display()
    print()
    car3 = Car("Mercedes","Black",7)
    car3.drive(60, 150)
    car3.display()
test()