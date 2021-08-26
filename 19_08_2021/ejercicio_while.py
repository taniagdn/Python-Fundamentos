#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:20:51 2021

@author: taniagualli
"""


contar = input("Ingrese el # veces a contar:")
contar = int(contar)
contador = 1
while True:
    print(contador)
    contador = contador+1
    if contador>contar:
        break
