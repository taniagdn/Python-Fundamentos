#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 08:14:09 2021

@author: taniagualli
"""

#Tipos de datos
print (type('CEC-EPN'))
print (type(False))
print (type(8))
print (type(13.55))

#Comparaciones
print(1<2)
print(1>2)
print(13==3)
print(1!=4)
print(1<=2)
print(1>=72)

#Asignaciones
x=5
suma=x+2
print(suma)
print("CEC-EPN "*x)
print("\n"*x)
print("CEC-EPN "*x)

str1 = "Cisco"
str2 = "Networking"
str3 = "Academy"
space = " "

print(str1+space+str2+space+str3)

print(str1, str2, str3) #beneficio de espaciado con la coma

x=3
print('El valor '+x) #x es entero no es posible usar función de concatenación

print('El valor '+str(x)) #xx sigue siendo entero

x=str(x)
print(type(x))

x=float(x)
print(type(x))

x=int(x)
print(type(x))

x=bool(x)
print(type(x))

div=x/5
print (div)

#FORMATO

pi = 22/7
print(pi)
print("{:.2f}".format(pi))


#Estructuras
lista = [2, True, 5.8, "CEC", 2, False]
lista1 = [2, True, 5.8, "CEC", 2, False]
tupla = (2, True, 5.8, "CEC", 2, False)
print(type(lista))
print(type(tupla))
print(lista)
print(tupla)
print(lista[0])
print(lista[-6])
print(tupla[1])

del lista1[5]

#DICCIONARIOS
dict1={'1712226479':'Tania Guadalupe',
       1:"empleado1",
       "R1":"10.10.10.1",
       5:1999}

print(type(dict1))
print(dict1)
print(dict1[1])
print(dict1["1712226479"])

dict1[6]="AP"

1 in dict1


