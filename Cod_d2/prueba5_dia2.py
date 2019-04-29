# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:39:52 2019

@author: luis9
"""

word = str(input("Enter a word: ")).casefold()
lett = str(input("Enter a letter: ")).casefold()

for char in word:
    if char == lett:
        word = word.replace(char,char.upper())
        
print(word)