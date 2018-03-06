# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:55:54 2018

@author: dusad
"""

a0 = 0
a1 = 1

n = int(input("Enter the integer n"))

for i in range(2,n+1):
    ai = a0 + a1
    a0 = a1
    a1 = ai

print("The solution of nth term in Fibbonacci series is %d" %ai) 


