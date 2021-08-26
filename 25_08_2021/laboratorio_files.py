#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:48:12 2021

@author: taniagualli
"""


file = open("/Users/taniagualli/Documents/Curso_Python/25_08_2021/devicexs.txt",mode='a')


while True:
    newItem=str(input("Enter a new device: "))
    if newItem=="Exit":
        print("Äll done!")
        break
    file.write(newItem + "\n")    
file.close()