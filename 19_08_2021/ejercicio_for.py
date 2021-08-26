#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:56:53 2021

@author: taniagualli
"""

lista=['R1','R2','R3','S1','S3']
for j in lista:
    if "R" in j:
        print(j)
    
lista1=[]  
for i in lista:
    if "S" in i:
        lista1.append(i)
        
#Dada una lista, los valores con R va a la lista1 y con S a la lista2
lista=['R1','R2','R3','S1','S3']
lista1=[]
lista2=[]
for i in lista:
    if "R" in i:
        lista1.append(i)
    elif "S" in i:
        lista2.append(i)

    
