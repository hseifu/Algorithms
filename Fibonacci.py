#! /usr/bin/env python3

import random
import random
import pylab
import timeit
import numpy as np
import matplotlib.pyplot as plt
import sys

def fibonacci_nv(n):#subtract one when calling 
    if n<2:
        return n
    else:
        return fibonacci_nv(n-1)+fibonacci_nv(n-2)

def fibonacci_bu(n):#bottom up method
    prev = 0
    cur = 1
    res = 0
    for i in range(n-2):
        res = prev + cur
        prev = cur
        cur = res
    return res

def fibonacci_cf(n):#closed form
    a = 1
    for i in range(n):
        a = 1.61803398875*a
    return (a/2.2360679775)



def fibonacci_ma(n):#matrix form 
    arr2 = [[1,1],[1,0]]
    arr1 = arr2
    if n==0:
        return 0
    if n==1:
        return 1
    for i in range(n-1):
        w = arr1[0][0]*arr2[0][0] + arr1[0][1]*arr2[1][0]
        x = arr1[0][0]*arr2[0][1] + arr1[0][1]*arr2[1][1]
        y = arr1[1][0]*arr2[0][0] + arr1[1][1]*arr2[1][0]
        z = arr1[1][0]*arr2[0][1] + arr1[1][1]*arr2[1][1]
        arr1[0][0] = w
        arr1[0][1] = x
        arr1[1][0] = y
        arr1[1][1] = z
        t = x
        arr2 = [[1,1],[1,0]]
    return t



times = []
ran = 5
a = 0
while(1):
    startnv = timeit.default_timer()
    fibonacci_nv(a)
    stopnv = timeit.default_timer()
    times.append(stopnv-startnv)
    startbu = timeit.default_timer()
    fibonacci_bu(a+1)
    stopbu = timeit.default_timer()
    times.append(stopbu-startbu)
    startcf = timeit.default_timer()
    fibonacci_cf(a)
    stopcf = timeit.default_timer()
    times.append(stopcf-startcf)
    startma = timeit.default_timer()
    fibonacci_ma(a)
    stopma = timeit.default_timer()
    times.append(stopma-startma)
    a += 1
    if (max(times))>3:
        break

methods = 4
print(len(times))
plt.plot([x for x in range(len(times)//methods)],[x for x in times if times.index(x)%methods==0], 'r-')
plt.plot([x for x in range(len(times)//methods)],[x for x in times if times.index(x)%methods==1], 'g-')
plt.plot([x for x in range(len(times)//methods)],[x for x in times if times.index(x)%methods==2],color = "black")
plt.plot([x for x in range(len(times)//methods)],[x for x in times if times.index(x)%methods==3],'b-')
plt.yscale('log')
plt.xscale('log')
pylab.savefig("data.png")
