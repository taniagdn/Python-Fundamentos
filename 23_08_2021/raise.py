#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Aug 23

@author: taniagualli
"""


def badFun (n):
    raise ZeroDivisionError

try: 
    badFun(0)
except ArithmeticError:
    print("What happened? An error?")
print("THE END.")