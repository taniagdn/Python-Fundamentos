#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Aug 23

@author: taniagualli
"""
def badFun (n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise
try:
    badFun(0)
except ArithmeticError:
    print("I see!")
print ("THE END")

