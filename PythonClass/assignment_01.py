#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Assignment 1:
    Write a Program with raw_input function and using 8 
    different conversion functions"""

def main():
    num= raw_input("Enter some number: ")
    print "The number is: ", num
    print "The Type is: ", type(num)
    print "The Id is: ",id(num)
    
if(__name__== "__main__"):
    main()
    
    
#using the int() function to change the raw_input

def main():
    print ""
    print "##Conversion of a basic string to int##"
    num= raw_input ("Enter some number, thats going to change in to int: ")
    num=int(num)
    print "The number is: ", num
    print "The Type is: ",type(num)
    print "The Id is: ", id(num)
main()

#Using the float() to change from raw_input source
def main():
    print ""
    print "##Conversion of a basic string to float##"
    num=raw_input("Enter the number to convert to float: ")
    num=float(num)
    print "The number is: ",num
    print "The Type is : ", type(num)
    print "The id is: ", id(num)
main()
