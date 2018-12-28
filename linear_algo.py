# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 20:19:48 2018

@author: kunal
"""

list=[]
num=int(input("enter the range of the list: \t"))
for n in range(num):
    number=int(input("enter the number to be added in list \t"))
    list.append(number)
x=int(input("enter the value to be searched  \n"))
found=False
for i in range(len(list)):
    if list[i]==x:
        found=True
        print("\n%d the number is found %d" % (x,i))
        break
    else:
        found=False
        print("\n%d the number is not found %d"%x)

    