#! /usr/bin/env python3
import random


#A = list to be sorted, d = maximum number of digits with index of 0, count initialized to zero and incremented through every iteration
def hollerith_radix(A, d, count = 0, base = 10):
    if len(A) == 1 or count > d:
        return A
    else:
        final = []
        buckets = []

        for _ in range(base): # append base number of empty lists
            buckets.append([])

        for number in A: # append each element in A to an empty list in B based on which element is being compared
            d1 = (number//base**(d-count)%base)
            buckets[d1].append(number)

        count += 1 # increase the digit to be compared
    
        for i in range(len(buckets)):   # for each element in the buckets call the function again on it to further classify that
            if len(buckets[i]) != 0:
                buckets[i] = hollerith_radix(buckets[i],d,count)
                

        for i in range(len(buckets)):
            if len(buckets[i]) != 0:
                for j in buckets[i]: # append individual elements to the final list to flatten the list
                    final.append(j)


        return(final)


#function for generating random integer with n digits
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)


A = []
for _ in range(20):
    A.append((random_with_N_digits(4)))
res1 = hollerith_radix(A,3)

print("----unsorted---- \n",A)
print("-----sorted----- \n",res1)

A2 = random.sample(range(1,100),10)
res2 = hollerith_radix(A2,1)

print("----unsorted---- \n",A2)
print("-----sorted----- \n",res2)

A3 = [11101111,1100011,1101001,11,110001,1000100,111001,11011010,1010,10111111]
res3 = hollerith_radix(A3,7,0,2)

print("----unsorted binary---- \n",A3)
print("------sorted binary----- \n",res3)


A4 = [1385, 2223, 3757, 7753, 2102, 7473, 9954, 6569, 2101, 70, 2566, 847, 6339, 1218, 1779, 9294, 7491, 2543, 6139, 9867]
res4 = hollerith_radix(A4,3)

print("----unsorted---- \n",A4)
print("-----sorted----- \n",res4)

A5 = [200,200,200,200]
res5 = hollerith_radix(A5,2)

print("----unsorted---- \n",A5)
print("-----sorted----- \n",res5)