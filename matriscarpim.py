# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

A = []
for i in range(3):
    for j in range(4):
        A.append(random.randrange(10))
B = []
for i in range(4):
    for j in range(5):
        B.append(random.randrange(10))
def multiply(A,B):
    C = [[0 for x in range(len(A))] for y in range(len(B[0]))] 
    for i in len(A):
        for j in len(B[0]):
            for k in len(B):
                C[i][j] += A[i][k]*B[k][j]
    return C
    
