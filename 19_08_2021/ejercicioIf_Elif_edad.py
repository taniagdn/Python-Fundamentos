#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:34:22 2021

@author: taniagualli
"""

space=' '
print("¿Cuál es su nombre?")
nombre = input()
print("¿Cuál es su apellido?")
apellido = input()
print("¿Dónde vive?")
direccion = input()
print("¿Qué edad tiene?")
edad = int(input())
print(f"Me alegro de conocerle {nombre}{space}{apellido}.  Sus datos se han registrado correctamente!")


if edad >= 0 and edad<=11:
    print("La edad registrada corresponde a un niño/niña")
elif edad>=12 and edad<=18:
    print("La edad registrada corresponde a un adolescente")
elif edad>=19 and edad<=65:
    print("La edad registrada corresponde a un adulto")
else:
    print("La edad registrada corresponde a un adulto mayor")