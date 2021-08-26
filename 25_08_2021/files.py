#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:29:50 2021

@author: taniagualli
"""


file = open("/Users/taniagualli/Documents/Curso_Python/25_08_2021/devices.txt")
for i in file:
    i=i.strip()
    lista.append(i)
    print(i)
file.close()
print(lista)
