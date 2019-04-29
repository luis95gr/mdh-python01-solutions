# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:00:05 2019

@author: luis9
"""

num1 = int(input('Enter a number: '))
num2 = int(input('Enter the second number: '))

if num1 > num2:
    print("The first number is larger")
elif num1 < num2:
    print("The second number is larger")
else:
    print("Both numbers are equal")