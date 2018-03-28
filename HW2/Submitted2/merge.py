    #! /usr/bin/env python3
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

#insertion sort
#implemented based on psuedo code from slide
def insertion_sort(arr):
    for i in range(1,len(arr)):
        c = arr[i]
        j = i-1
        while j >= 0 and arr[j]>c:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = c

def simple_merge(arr,k):
    if len(arr) <= k:
        insertion_sort(arr)
        #return sorted list if length <= k
        return arr
    else:
        l = simple_merge(arr[:len(arr)//2],k)
        r = simple_merge(arr[len(arr)//2:],k)
        #recursively call the merge function with half the list and passed as parameters
        res = []
        l.reverse()
        r.reverse()
        #reverse to be able to use pop
        for k in range (len(arr)):
            if len(l) == 0 or len(r) == 0:
                break
            #iterate through length of the entire loop until one reaches zero
            e = l.pop()
            f = r.pop()
            if e <= f:
                res.append(e)
                r.append(f)
            if e > f:
                res.append(f)
                l.append(e)
            #append the least of the two by comparing their last values
        l.reverse()
        r.reverse()
        #reverse back since they were initailly reversed
        res += l + r
        #if there are any elements left in either of the list just append the list
        return res


el = 80    #k value
times = []
times2 = []
lists = []#list for holding worst, best, and random lists
avg = []#list for holding lists that made of random values
sel_avg= []#list for holding lists that are made of random values for selection sort
sel_avg2 =[]#list for holding average times for selection sort with different length 
true_avg = []#list for holding average times for best and worst case lists with different length 
counter = 0
for i in range (0,2000,100):#iteration growith is 0,100,200,300...,2000

    avg.append([])#list for holding multiple random values 
    sel_avg.append([])#list for holding multiple random values for selection sort
    for k in range (10):
        avg[counter].append(random.sample(range(1,2001),i))#append random values with size i ranging from 1-2000
    for k in range (10):
        sel_avg[counter].append(random.sample(range(1,2001),i))
    temp_time = []#list for holding run time of the algorithms with different lists
    sel_times = []#list for holding run time of the algorithms with different lists for selection sort
    for _ in avg[counter]:
        start = timeit.default_timer()#timer start
        ti = simple_merge(_,el)#call sort function
        stop = timeit.default_timer()#timer stop
        temp_time.append(stop-start)#register time difference
    for _ in sel_avg[counter]:
        start = timeit.default_timer()#timer start
        tim = selection_sort(_)#call sort function
        stop = timeit.default_timer()#timer stop
        sel_times.append(stop-start)#register time difference
    true_avg.append([sum(temp_time)/len(temp_time),i])
    sel_avg2.append([sum(sel_times)/len(sel_times),i])
    #append average time and number of elements sorted
    counter += 1

    temp2 = random.sample(range(1,2001),i)
    temp2.sort()
    lists.append(temp2)#best case: already sorted list

    temp3 = random.sample(range(1,2001),i)
    temp3.sort()
    temp3.reverse()
    lists.append(temp3)#worst case: completely unsorted(reverse sorted)


#for best and worst case in list run both algorithms and time them
for i in range (len(lists)):
    #measuring time for merge sort
    start = timeit.default_timer()
    k = simple_merge(lists[i],el)
    stop = timeit.default_timer()
    #measuring time for selection sort
    start2 = timeit.default_timer()
    l = selection_sort(lists[i])
    stop2 = timeit.default_timer()
    #assign list type based on the pattern they were added to the list
    if (i)%2 == 0:
        list_type = "BEST"
    if (i)%2 == 1:
        list_type = "WORST"
#register time, length of array and type of the list
    times.append([stop-start,len(k),list_type])#for merge sort
    times2.append([stop2-start2,len(l),list_type])#for selection sort

#group the times according to list types
t = []
t.append([x[0] for x in times if (times.index(x))%2 == 0])
t.append([x[0] for x in times if (times.index(x))%2 == 1])
#group the number of elements according to the list types
n = []
n.append([x[1] for x in times if (times.index(x))%2 == 0])
n.append([x[1] for x in times if (times.index(x))%2 == 1])
#for selection sort
t_2 = []
t_2.append([x[0] for x in times2 if (times2.index(x))%2 == 0])
t_2.append([x[0] for x in times2 if (times2.index(x))%2 == 1])
n_2 = []
n_2.append([x[1] for x in times2 if (times2.index(x))%2 == 0])
n_2.append([x[1] for x in times2 if (times2.index(x))%2 == 1])


#plot graph and save plot in a separate file
plt.plot(n[1],t[1],'r-', n[0],t[0],'g-') 

plt.plot([x[1] for x in true_avg], [x[0] for x in true_avg], color = "black")
plt.plot([x[1] for x in sel_avg2], [x[0] for x in sel_avg2], 'y')
plt.plot(n_2[1],t_2[1],'c-', n_2[0],t_2[0],'m-') 
plt.ylabel("Run time")
plt.xlabel("Number of elements")
plt.title("K = "+str(el))
plt.legend(['MERGE_WORST', 'MERGE_BEST','MERGE_AVERAGE','SELECTION_AVG','SELECTION_WORST','SELECTION_BEST'], loc='upper left')
plt.show(block = False)
pylab.savefig(str(el)+'_.png')#file name 
