#! /usr/bin/env python3
import math
import decimal
import random
#implemented from book

def insertion_sort(arr):
    for i in range(1,len(arr)):
        c = arr[i]
        j = i-1
        while j >= 0 and arr[j]>c:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = c
    return arr
        
def bucket_sort(A):
    B = []
    n = len(A)
    for _ in range(n-1):
        B.append([])
    for i in A:
        B[math.floor((n-1)*(i))].append(i)
    print(B)
    for i in range(len(B)):
        if(len(B[i])>1):
            B[i] = insertion_sort(B[i])
    print(B)
    final = []
    for i in B:
        final+=i
    return final

A =[ 0.9, 0.1, 0.6, 0.7, 0.6, 0.2, 0.1 ]
print(A)
A1 = random.sample(range(100,1000),10)
for i in A1:
    i = i/100
print(bucket_sort(A))

