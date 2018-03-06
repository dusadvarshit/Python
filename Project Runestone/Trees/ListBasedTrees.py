# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 08:37:27 2018

@author: dusad
"""

# List representations of tree data structure in python.

'''
myTree = ['a', #root      
          ['b', #left subtree
           ['d', [], []],
           ['e', [], []] ],
          ['c', #right subtree
           ['f', [],[]],
           [] ]
          ]
       
print(myTree)
print('left subtree = ', myTree[1])
print('root = ', myTree[0])
print('right subtree = ', myTree[2])
'''
#### Now make binary tree function

def BinaryTree(r):
    return [r,[],[]]

def insertLeft(root,newBranch):
    t = root.pop(1)
    #print(t)
    if len(t)>1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [],[]])
    return root
        
def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t)>1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root
    
def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
#insertLeft(r[2],44)
l = getLeftChild(r)
print(l)

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))

            