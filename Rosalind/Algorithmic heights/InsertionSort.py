# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 23:46:31 2018

@author: dusad
"""

def Swap(a,b):
    c = b
    b = a
    a = c
    return a,b
swap_count = 0
n = 904
A = [0]*n
file = open("sample.txt", "r")
dec = 0
for lines in file:
    line = lines.split()    

for i in range(0,len(line)):
    A[i] = int(line[i])
print(A)

for i in range(1,n):
    k = i
    while k>0 and A[k]<A[k-1]:
        swap_count = swap_count + 1
        [A[k-1],A[k]] = Swap(A[k-1],A[k])
        k = k-1

print(swap_count)
