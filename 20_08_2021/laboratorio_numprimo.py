#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:36:30 2021

@author: taniagualli
"""


def is_prime(x):
    if x == 1:
        return False
    elif x==2:
        return True
    for x in range (1,x):
        if (x % 2):
            return True
        