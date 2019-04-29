# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:47:29 2019

@author: luis9
"""

num = int(input("Enter a number: "))

lista=[]
lista.extend(range(1,num+1))

lista2=lista[::2]
print(lista2)