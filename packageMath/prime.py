#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 10:35:16 2019

@author: zwalaneelam
"""

def prime(num):
    #To check whether the given num is prime or not
    key=0
    for each in range(2,num):
        if num%each==1:
            key=1
    if key==1:
        return "The number is Prime"
    else:
        return "The number is NOT Prime"