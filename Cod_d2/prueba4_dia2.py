# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:28:40 2019

@author: luis9
"""

word = str(input("Enter a word: "))
vowels=["a","e","i","o","u"]

for char in word:
    for vow in vowels:
        if char == vow:
            print(char)
            word = word.replace(char," ")
        
print(word)