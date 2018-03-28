#! /usr/bin/env python3

#modified count sort to sort words at the dth index based on their ascii values
#runs in Theta(n)
def alpha_count_sort(A,d):#A = list of words, d= which digit to sort
    c = []
    k = 57 #the maximum value of the maximum ord decreased by 65
    a = [ord(x[d])-65 for x in A] 
    #decrease the value of the ASCII codes of the letters by 65 to avoid so many empty lists
    B = []
    
    for _ in range(k+1): # constant interation. (independent of n)
        c.append(0)
        
    for j in range (len(a)): # iterathrough the specified index of every word that means n times
        c[a[j]] += 1
        B.append(0)

    B.append(0) #extra zero to compensate for starting index of 0
    for i in range (1,k+1): # again constant iteration as 11
        c[i] += c[i-1]

    
    for j in reversed(range(len(a))):  #iterate n times 
        B[c[a[j]]] = A[j]
        c[a[j]] -= 1
    print(B)


    return(B[1:])




#runs in Theta(n) where the constant is K
def radix_alpha(A,k):#A = list of words, k = length of the words with equal lengths
    
    for i in reversed(range(k)):#iterate through each letter and call count_sort. 
        A = alpha_count_sort(A,i)
    return A

A = ["hELLO", "WORLD", "THISS", "HENOK", "FROMM", "COLEJ", "THREE"]



print(radix_alpha(A,5))
