#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 09:50:51 2021

@author: taniagualli
"""


def fibo (n):
    a,b = 0,1
    while(a<n):
        print(a,end=' ')
        a,b=b, a+b
    print()
#fibo(8)
        
        