# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 00:58:42 2018

@author: dusad
"""

k = 18 
C = [-1]*k
p = -1
index = 0
file = open("sample.txt", "r")
for lines in file:
    p = p+1
    line = lines.split() 
    A = []
    for i in range(0,len(line)):
        A.append(line[i])
    #print(A)
    
    for i in range(0,len(A)):
        index = 0
        for j in range(0,len(A)):
            if A[i] == A[j]:
                index = index+1
                #print(index)
        if index>float(len(A))/2:
            C[p] = A[i]
            #print("it haooend",A[i])            
            break
                                
print(C)
        
