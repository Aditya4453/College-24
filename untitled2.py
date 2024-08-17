# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 15:46:57 2024

@author: LAB
"""

num1= int(input("Enter Length(in m) :"))
num2= int(input("Enter Width(in m) :"))

area=num1*num2

 

if num1<0 or num2<0 :
    print("Entered Value is invalid")
else:
    print("Area is ",area)
    
 