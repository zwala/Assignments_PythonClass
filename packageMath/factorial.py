#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 10:34:57 2019

@author: zwalaneelam
"""

def factorial(num):
    prod=1
    for each in range(1,num+1):
        prod*=each
    return prod