# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:54:56 2019

@author: luis9
"""

num = int(input("Enter a number: "))
num2 = int(input("Enter second number: "))

lista=[]
lista2=[]
lista.extend(range(0,num+1))

for dig in lista:
    if num2 % dig == 0:
        lista2.append(dig)
        
print(lista2)