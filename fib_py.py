# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 23:12:54 2021

@author: win10
"""

def Fibonacci(n):

    if n < 0:
        print("Incorrect input")
 

    elif n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(9))