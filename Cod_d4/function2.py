# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:08:47 2019

@author: Luis
"""

def beers(n=1):
    if n-1 == 0:
        print("No beers left")
        return
    else:
        print("Beers left!")
        print("Beers: {0}".format(n-1))
        return
    
    