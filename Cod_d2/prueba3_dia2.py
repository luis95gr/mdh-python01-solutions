# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:18:39 2019

@author: luis9
"""

word = str(input("Enter a word: "))

if word[len(word)-1] == "!":
    word = word[:-1]
    print(word.upper())
else:
    print(word.casefold())


