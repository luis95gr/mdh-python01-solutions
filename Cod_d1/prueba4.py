# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:05:12 2019

@author: luis9
"""

my_num = int(input('Enter a number to find the sum up to: '))
sum_result = 0
current = my_num
while 0 <= current:
    sum_result += current
    current -= 1
print(sum_result)