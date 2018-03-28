#! /usr/bin/env python3

import random
import pylab
import timeit
import numpy as np
import matplotlib.pyplot as plt
import sys

def max_heapify(A,i):
    left = 2*(i+1)-1#get the two children
    right = 2*(i+1)
    if left < len(A) and A[left] > A[i]:#if the left is greater set as the largest
        largest = left
    else:
        largest = i#else assign it to the current index
    if right < len(A) and A[right] > A[largest]:#check if right is greater 
        largest = right
    if largest != i:#if the largest changed exchange
        temp = A[largest]
        A[largest] = A[i]
        A[i] = temp
        max_heapify(A,largest)
    
def build_max_heap(A):#call max heapify on the upper half of the heap
    for i in reversed(range((len(A)//2))):
        max_heapify(A,i)

def HeapBottomUp(A):
    for i in reversed(range(1,(len(A)//2))):#bottom up on the upper half only
        k = i#track current index
        v = A[k-1]#the value to be traversed
        heap = False#initialize heap as false
        while not heap and 2*k <= len(A):#while not heap and the child exists
            j = 2*k#assign the child index
            if j < len(A):
                if A[j-1]<A[j]:#check if left or right is greater
                    j = j+1
            if v >= A[j-1]:#if value is greater then change heap status to true
                heap = True
            else:
                A[k-1] = A[j-1]#exchange
                k = j
        A[k-1] = v

#for data analyzation purposes
times1 = []
times2 = []
for i in range(100):
    starthp = timeit.default_timer()
    build_max_heap(random.sample(range(1,1000),i*10))
    stophp = timeit.default_timer()
    
    startbu = timeit.default_timer()
    HeapBottomUp(random.sample(range(1,1000),i*10))
    stopbu = timeit.default_timer()


    times1.append([stophp-starthp,i*10])
    times2.append([stopbu-startbu,i*10])
    
t_1 = [x[0] for x in times1]
t_2 = [x[0] for x in times2]

n_1 = [x[1] for x in times1]
n_2 = [x[1] for x in times2]

plt.plot(n_1,t_1,'r-')
plt.plot(n_2,t_2,'g-')

plt.legend(['REGULAR MAX HEAP','BOTTOM UP HEAP'])
pylab.savefig("results.png")


