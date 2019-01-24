#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 14:55:44 2019

@author: zwala
"""
##Conversions of int()

num1=raw_input("Please enter x: ")
num2=raw_input("Please enter y: ")
num=num1+num2
print "The Concatenation: ",num #Concatenation

num1=int(num1) 
num2=int(num2)
num=num1+num2
print "The Addition is: ", num # Does the addition now

num1=int(num1)
num2=float(num2)
num=num1+num2
print "One value is int, 2ns is float: ",num

num1=float(num1)
num2=float(num2)
num=num1+num2
print "The Float version: ",num

num1=bool(num1)
num2=bool(num2)
num=num1+num1
print "The Bool Version(Generally returns 1forT& 0forF:",num 
