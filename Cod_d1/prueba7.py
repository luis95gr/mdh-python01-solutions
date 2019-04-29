# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:22:45 2019

@author: luis9
"""
import copy
x= int(input('Enter a number to find its divisors: '))
y= int(input('Enter a number to find its divisors: '))

i = 1
ii=1
lista = []
lista2 = []
p=[]
q=[]

while i<=x:
   if x%i == 0:
       lista.append(i)
       print(' 1 divisor ',i)
   i += 1

while ii<=y:
   if x%ii == 0:
       lista2.append(ii)
       print(' 2 divisor ',ii)
   ii += 1


    
if len(lista) > len(lista2):
    p=lista2.copy()
    q=lista.copy()
elif len(lista) < len(lista2):
    p=lista.copy()
    q=lista2.copy()
else:
   p=lista.copy()
   q=lista2.copy()    

maximo=0
cont=0
for num in p:
    if num == q[cont]:
        maximo = num
    cont+=1    
        
    
print("Max divisor is: ",maximo)