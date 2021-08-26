#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:24:08 2021

@author: taniagualli
"""

acl = int(input("Ingrese el # de ACL: "))
if acl >= 1 and acl<=99:
    print("Es una ACL estándar")
elif acl>=100 and acl<=199:
    print("Es una ACL extendida")
else:
    print("El # ingresado no es de una ACL")
