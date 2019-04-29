# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:34:32 2019

@author: Luis
"""

number=str(input("Enter numbers: "))
lista=[]
listan=[]
listap=[]
numeros=[]
tup=()
nums=number.split(',')

if len(nums)%2 != 0:
    nums.pop()

print(nums)
i=0
while i < len(nums):
    numeros.append(int(nums[i]))
    i+=1
    

for it in numeros:
    if it%2 ==0:
        listap.append(it)
    else:
        listan.append(it)
 
contador=0
for it in listap:
    lista.append((listan[contador],it))
    contador+=1

print(lista)
