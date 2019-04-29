# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 09:25:47 2019

@author: Luis
"""

def get_evens(n=5): 
    evens = []
    for element in range(n): 
        if element % 2 == 0: 
            evens.append(element)
    return evens