# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 22:43:10 2018

@author: dusad
"""
# IMPORTANT: The dataset in question will have first line as number of nodes and edges and not connectivity information
A = []
B = []
max = 0
file = open("sample.txt", "r")
for lines in file:
    line = lines.split()
    
    A.append(int(line[0]))
    B.append(int(line[1]))
    if int(line[0])>int(line[1]):
        if max<int(line[0]):
            max = int(line[0])
    else:
        if max<int(line[1]):
            max = int(line[1])

D = [0]*max
#print(A,B)
for i in range(0,len(A)):
    #print(i, max)
    D[A[i]-1] = D[A[i]-1]+1
    D[B[i]-1] = D[B[i]-1]+1
    #print(D)

print(D)
