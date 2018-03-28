#! /usr/bin/env python3
#Done by: Henok Seifu

########################    ALGORITHMS AND DATA STRUCTURES     ##########################     
import random
import pylab
import timeit
import numpy as np
import matplotlib.pyplot as plt
import sys

# Selection Sort implimenting function
def selection_sort(arr):
    result = []#resultant list
    for i in range(len(arr)):
        result.append(arr.pop(arr.index(min(arr))))
    #append minimum of parameter list into resultant list
    return result



# Testing implimentation with different lists with different length
lists = []#list for holding worst, best, and random lists
avg = []#list for holding lists that made of random values
true_avg = []#list for holding average times for best and worst case lists with different length 
counter = 0
for i in range (0,2000,100):#iteration growith is 0,100,200,300...,2000

    avg.append([])#list for holding multiple random values 
    for k in range (10):
        avg[counter].append(random.sample(range(1,2001),i))#append random values with size i ranging from 1-2000
    temp_time = []#list for holding run time of the algorithms with different lists
    for _ in avg[counter]:
        start = timeit.default_timer()#timer start
        ti = selection_sort(_)#call sort function
        stop = timeit.default_timer()#timer stop
        temp_time.append(stop-start)#register time difference
    true_avg.append([sum(temp_time)/len(temp_time),i])#append average time and number of elements sorted
    counter += 1

    temp2 = random.sample(range(1,2001),i)
    temp2.sort()
    lists.append(temp2)#best case: already sorted list

    temp3 = random.sample(range(1,2001),i)
    temp3.sort()
    temp3.reverse()
    lists.append(temp3)#worst case: completely unsorted(reverse sorted)


times = []
#for each element in list run the algorithm and time it
for i in range (len(lists)):
    start = timeit.default_timer()
    k = selection_sort(lists[i])
    stop = timeit.default_timer()
#assign list type based on the pattern they were added to the list 
    if (i)%2 == 0:
        list_type = "BEST"
    if (i)%2 == 1:
        list_type = "WORST"
#register time, length of array and type of the list
    times.append([stop-start,len(k),list_type])

#group the times according to list types
t = []
t.append([x[0] for x in times if (times.index(x))%2 == 0])
t.append([x[0] for x in times if (times.index(x))%2 == 1])
#group the number of elements according to the list types
n = []
n.append([x[1] for x in times if (times.index(x))%2 == 0])
n.append([x[1] for x in times if (times.index(x))%2 == 1])




#plot graph and save plot in a separate file
plt.plot(n[1],t[1],'r-', n[0],t[0],'g-') 

plt.plot([x[1] for x in true_avg], [x[0] for x in true_avg], color = "black")
plt.legend(['BEST', 'WORST','AVERAGE'], loc='upper left')
plt.show(block = False)
pylab.savefig('data.png')#file name 
