#! /usr/bin/env python3
import random

def quick_sort(A,p,r):#randomized quick sort
    if p < r:
        temp = random.randint(p,r)
        temp1 = A[p]
        A[p] = A[temp]
        A[temp] = temp1
        q = partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)
    
def partition(A,p,r):#regular partition
    x = A[p].f
    i = p
    for j in range(p+1,r+1):
        if A[j].f <= x:
            i = i + 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp2 = A[i]
    A[i] = A[p]
    A[p] = temp2
    return i

def Greedy(S):
    quick_sort(S, 0, len(S)-1)
    A = S[0]
    j = 0
    for i in range(1,len(S)-1):
        if S[i].s >= S[j].f:
            A += S[i]
            j = i
    return A

class Activity:
    def __init__(self, s, f):
        self.s = s
        self.f = f

def Greedy_unsorted(S, B):
    if len(S) == 1:
        B.append(S[0])
        return 
    if len(S) == 0:
        return
    A = S[0]

    for i in range(1,len(S)-1):
        if A.s < S[i].s:
            A = S[i]
    B.append(A)
    Greedy_unsorted([x for x in S if x.f <= A.s], B)

def main():
    S = [Activity(1,4), Activity(3,5), Activity(0,6), Activity(5,7), Activity(3,8), Activity(5,9), Activity(6,10), Activity(8,11), Activity(8,12), Activity(2,13), Activity(12,14)]
    B = []
    random.shuffle(S)
    Greedy_unsorted(S,B)
    for i in B:
        print(i.s)
    
main()