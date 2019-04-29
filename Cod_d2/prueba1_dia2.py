# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:36:51 2019

@author: luis9
"""

import numpy as np
x = int(input("Enter a number:"))
i = 1
lista = []
listafor=[]
listafor.extend(range(1,x+1))

for num in listafor:
    if x%i == 0:
       lista.append(i)
       print(' 1 divisor ',i)
    i += 1


if lista[0]==1 and lista[1]==x:
    print("It is prime number")
else: 
    print("It is not a prime number")