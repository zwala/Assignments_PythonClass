#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 14:37:04 2019
@author: zwala
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Assignment 1:
    Write a Program with input function and using 8 
    different conversion functions
    int,float,str,bool,null
    list, tuple, set,dictionary
    
    input() was only able to receive numbers are inputs
    raw_input() was able to accept both string and ints
    """

def main():
    num= input("Enter some number: ")
    print "The number is: ", num
    print "The Type is: ", type(num)
    print "The Id is: ",id(num)
    
if(__name__== "__main__"):
    main()
    
    
#using the int() function to change the input()

def main():
    print ""
    print "##Conversion of a basic string to int##"
    num=input ("Enter some number, thats going to change in to int: ")
    num=int(num)
    print "The number is: ", num
    print "The Type is: ",type(num)
    print "The Id is: ", id(num)
main()

#Using the float() to change from input() source
def main():
    print ""
    print "##Conversion of a basic string to float##"
    num=input("Enter the number to convert to float: ")
    num=float(num)
    print "The number is: ",num
    print "The Type is : ", type(num)
    print "The id is: ", id(num)
main()

#Using str() to change from input() source
def main():
    print""
    print "##Conversion of the input to string##"
    num=input ("Enter the number to convert to string: ")
    num=str(num)
    print "The number/string is: ",num
    print "The type is: ", type(num)
    print "The id is: ", id(num)
main()

#Using the bool() to change from input() source
def main():
    print""
    print "##Conversion of some number to boolType##"
    num=input("Enter the number to convert the number to bool: ")
    num=bool(num)
    print "The number is: ",num
    print "The type is: ",type(num)
    print "The id is: ", id(num)
main()

"""  
#USing the null() to change the input source
def main():
    print""
    print "##Conversion of some number to Null Type##"
    num=raw_input("Enter the number to convert the number to bool: ")
    num= null
    print "The number is: ",num
    print "The type is: ",type(num)
    print "The id is: ", id(num)
main()
"""
   
#Convert the string in to a list#
def sequence():
    print ""
    print "##Conversion of a string into a LIST##"
    num=raw_input("Enter the string to convert in to list: ")
    num=list(num)
    print "The list is: ", num
    print "The type is: ",type(num)
    print "The id is: ",id(num)
sequence()

#Converts the string into a tuple#
def sequence():
    print ""
    print "##Conversion of a string into a TUPLE##"
    num=raw_input("Enter the string to convert in to tuple: ")
    num=tuple(num)
    print "The list is: ", num
    print "The type is: ",type(num)
    print "The id is: ",id(num)
sequence()

##Converts the string into a set##
def sequence():
    print""
    print "##Conversion of a string into a SET##"
    num=raw_input("Enter the string to convert in to SET: ")
    num=set(num)
    print "The list is: ", num
    print "The type is: ",type(num)
    print "The id is: ",id(num)
sequence()
    
##Converts the string into a Dictionary##
'''def sequence():
    print""
    print "##Conversion of a string into a Dictionary##"
    input("Enter the string to convert in to Dictionary: ")
    num=dict(num)
    print "The list is: ", num
    print "The type is: ",type(num)
    print "The id is: ",id(num)
sequence()
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    