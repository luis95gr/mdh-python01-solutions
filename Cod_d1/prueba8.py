# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:55:29 2019

@author: luis9
"""
import numpy as np
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

x=np.lcm(num1,num2)
print("LCM: ",x)