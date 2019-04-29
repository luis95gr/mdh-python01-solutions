# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 11:07:51 2019

@author: Luis
"""

class Dog(): 
    def __init__(self, name, happiness_level=5): 
        self.happiness_level=happiness_level

    def wag_tail(self, n): 
        self.happiness_level += n*5