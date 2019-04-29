# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:16:05 2019

@author: luis9
"""

x= int(input('Enter a number to find its divisors: '))
i = 1
while i<=x:
   if x%i == 0:
      print(' divisor ',i)
   i += 1