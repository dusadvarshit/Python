# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 00:14:57 2018

@author: dusad
"""

n = 8103
m = 9688

A = [0]*n
B = [0]*m
file = open("sample.txt", "r")
dec = 0
for lines in file:
    line = lines.split()    
    if dec == 0:
        for i in range(0,len(line)):
            A[i] = int(line[i])
        dec = 1
    else:
        for i in range(0,len(line)):
            B[i] = int(line[i])

C = [-1]*m

j = 0
for k in B:
    #print(k)
    for i in range(len(A)):
        if k == A[i]:  
            C[j] = i+1
    j = j+1
print(C)

        
    