#! /usr/bin/env python3

import random
#implemented from the book
def countsort(A,k):
    c = []
    for _ in range(k+1): 
        c.append(0)
    print(c)
    B = []
    B.append(0)
    for j in range (1,len(A)+1): 
        c[A[j-1]] += 1
        B.append(0)
    print(c)
    for i in range (1,k+1):
        c[i] += c[i-1]
    print(c)
    for j in reversed(range(1,len(A)+1)):
        B[c[A[j-1]]] = A[j-1]
        c[A[j-1]] -= 1
    print(c)
    print(B)
    del(B[0])
    print(B)


A = [ 9, 1, 6, 7, 6, 2, 1 ]



countsort(A,max(A))




