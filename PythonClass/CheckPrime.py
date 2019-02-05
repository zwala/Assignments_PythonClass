#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 10:50:36 2019

@author: zwalaneelam
"""


def main():
    num=input("Enter the number to check: ")
    i=num-1
    check=0
    while (i>=2):
        if(num%i==0):
           check=1
           break
        i-=1
    
    if(check!=1):
        print "Number is Prime"
    else:
        print "Number is NOT prime"
        
if(__name__=="__main__"):
    main()
    