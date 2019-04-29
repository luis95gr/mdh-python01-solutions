# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:01:38 2019

@author: luis9
"""

word = str(input("Enter a word: ")).casefold()
lett = str(input("Enter a letter: ")).casefold()

times=0

for char in word:
    if char == lett:
        times+=1

print('Times: {0}'.format(times))
