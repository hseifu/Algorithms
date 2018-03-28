#! /usr/bin/env python3
# Done by Henok_S
import random
import timeit
import pylab
import matplotlib.pyplot as plt
import numpy as np

def double_pivot_quick_sort(A,p,r):
    if p < r:
        q,t = double_pivot_partition(A,p,r)
        double_pivot_quick_sort(A,p,q-1)
        double_pivot_quick_sort(A,q+1,t-1)
        double_pivot_quick_sort(A,t+1,r)

def random_double_pivot_quick_sort(A,p,r):
    if p < r:
        val1,val2 = random.sample([x for x in range(p,r+1)],2)#generate random values from p-r
        temp4 = A[val1]#exchange values at random index with values at the first two indices
        A[val1] = A[p+1]
        A[p+1] = temp4
        temp5 = A[val2]
        A[val2] = A[p]
        A[p] = temp5
        q,t = double_pivot_partition(A,p,r)
        random_double_pivot_quick_sort(A,p,q-1)
        random_double_pivot_quick_sort(A,q+1,t-1)
        random_double_pivot_quick_sort(A,t+1,r)

def double_pivot_partition(A,p,r):
    #first partition on first pivot
    x = A[p]
    i = p
    for j in range(p+1,r+1):
#note that the first value is not changed since we exchange it by itself
#Therefore this would not mess up the location of the second pivot
        if A[j] < x:
            i = i + 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp2 = A[i]
    A[i] = A[p]
    A[p] = temp2
    #Second q sort on second pivot
    x1 = A[p+1]
    i_1 = p+1
    for j in range(p+2,r+1):
        if A[j] < x1:
            i_1 = i_1 + 1
            temp = A[i_1]
            A[i_1] = A[j]
            A[j] = temp
    temp2 = A[i_1]
    A[i_1] = A[p+1]
    A[p+1] = temp2
    return i, i_1

def quick_sort(A,p,r):#regular quick sort
    if p < r:
        q = partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)
    
def partition(A,p,r):#regular partition
    x = A[p]
    i = p
    for j in range(p+1,r+1):
        if A[j] <= x:
            i = i + 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp2 = A[i]
    A[i] = A[p]
    A[p] = temp2
    return i

#################################### FOR DATA COLLECTION PURPOSES #####################################
def main():
    times1 = []
    times2 = []
    times3 = []
    times4 = []
    times5 = []
    times6 = []
    for i in range(10):
        A = random.sample(range(1,1000),100*i)
        B = random.sample(range(1,1000),100*i)
        E = random.sample(range(1,1000),100*i)
        C = sorted(A)
        D = sorted(B)
        F = sorted(E)
        start1 = timeit.default_timer()
        quick_sort(A,0,len(A)-1)
        stop1 = timeit.default_timer()
        start2 = timeit.default_timer()
        double_pivot_quick_sort(B,0,len(B)-1)
        stop2 = timeit.default_timer()
        start3 = timeit.default_timer()
        quick_sort(C,0,len(A)-1)
        stop3 = timeit.default_timer()
        start4 = timeit.default_timer()
        double_pivot_quick_sort(D,0,len(B)-1)
        stop4 = timeit.default_timer()
        start5 = timeit.default_timer()
        random_double_pivot_quick_sort(E,0,len(E)-1)
        stop5 = timeit.default_timer()
        start6 = timeit.default_timer()
        random_double_pivot_quick_sort(F,0,len(F)-1)
        stop6 = timeit.default_timer()
        times1.append(stop1-start1)
        times2.append(stop2-start2)
        times3.append(stop3-start3)
        times4.append(stop4-start4)
        times5.append(stop5-start5)
        times6.append(stop6-start6)

    plt.plot([x*100 for x in range(10)],times1,"r-")
    plt.plot([x*100 for x in range(10)],times2,"g-")   
    plt.plot([x*100 for x in range(10)],times3,color = "black")
    plt.plot([x*100 for x in range(10)],times4,color = "blue")
    plt.plot([x*100 for x in range(10)],times5,'m-')
    plt.plot([x*100 for x in range(10)],times6,'y-')
    
    plt.ylabel("Run time")
    plt.xlabel("Number of elements")
    plt.legend(["Regular","Modified","Regular Worst","Modified Worst","Randomized", "Randomized Worst"])
    pylab.savefig("Data.png")

main()
