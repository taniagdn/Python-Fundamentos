#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 09:09:17 2021

@author: taniagualli
"""


#Laboratorio Manejo de errores

def readint(promt, min, max):
    try:
        number=int(input(promt))
        assert(number>=min and number<=max)
        return number
    except AssertionError:
        print("Error: el valor no está en el rango permitido")
        return False
    except:
        print("Error: Error en el ingreso")
        return False
while True:
    v=readint("Enter a number from -10 to 10: ", -10, 10)
    if v:
        print("The number is: ", v)
        break
