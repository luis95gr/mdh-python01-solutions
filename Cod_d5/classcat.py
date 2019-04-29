# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 12:23:39 2019

@author: Luis
"""

class Cat(): 

    def __init__(self, name, laziness_level, location): 
        self.name = name
        self.laziness_level = laziness_level
        self.location = location
        self.location2 = location

    def sense_earthquake(self, earthquake): 
        if earthquake:
            self.location = "gone dark"
            print("{0} has {1}".format(self.name,self.location))
        else:
            print("{0} is at {1}".format(self.name,self.location2))
       