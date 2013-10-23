# -*- coding: cp936 -*-
""" compare different sort methods
@author:chenguofeng08qh@gmail.com 
"""

def partition(a,p,r):
    x = a[r]
    i = p-1
    for j in range(p,r):
        if a[j] <= x:
            i = i + 1
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
    temp = a[i+1]
    a[i+1] = a[r]
    a[r] = temp
    return i+1
def quicksort(a,p,r):
    if p<r:
        q = partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)

def insertionsort(a):
    for i in range (1,len(a)):
        temp = a[i]
        j = i-1
        while (j >= 0) and (a[j] > temp):
                a[j+1]= a[j]
                j = j-1;
        a[j+1] = temp

def merge(a,b):
    i = 0
    j = 0
    c = []
    while(i < len(a) and j < len(b)):
        if (a[i] > b[j]):
            c.append(b[j])
            j = j+1
        else:
            c.append(a[i])
            i = i + 1
    if i < len(a):
        c.extend(a[i:])
    if j< len(b):
        c.extend(b[j:])
    return c        
            
def mergesort(a):
    if (len(a)<=1):
        return a
    mid = (len(a))/2
    left= mergesort(a[:mid])
    right = mergesort(a[mid:])
    return list(merge(left,right))
        
def radixsort(a,n,maxLen):
    for x in range(maxLen):
        bins = [[] for i in range(n)]
        for y in a:
            bins[(y/10**x)%n].append(y)
        a=[]
        for section in bins:
            a.extend(section)
    return a
    
   
def main():
    from time import time
    import random
    #n = [10,100,1000,10000,100000,1000000,10**7,10**8,2*(10**8)]
    n = [10**7,10**8,2*(10**8)]
##    timeA = []
##    timeB = []
##    timeC = []
##    for number in n:        
##        temp1 = 0
##        temp2 = 0
##        temp3 = 0
##        for i in range(1):
##            a = []
##            b = []
##            c = []
##            for i in range(number):
##                x = random.randint(0, (2**32)-1)
##                a.append(x)
##                b.append(x)
##                c.append(x)
##            start = time()
##            quicksort(a,0,number-1)
##            stop = time()
##            time1 = stop-start
##            temp1 = temp1 + time1
##            if number <=10000:
##                start = time()
##                insertionsort(b)
##                stop = time()
##                time2 = stop-start
##                temp2 = temp2 + time2
##            else:
##                temp2 = 0
##            start = time()
##            mergesort(c)
##            stop = time()
##            time3 = stop-start
##            temp3 = temp3 + time3
##        temp1 = temp1/1.0
##        temp2 = temp2/1.0
##        temp3 = temp3/1.0
##        print str(number) + "quicksort :"
##        print temp1
##        #print str(number) + "insertionsort :"
##        #print temp2
##        print str(number) + "mergesort :"
##        print temp3
##        timeA.append(temp1)
##        timeB.append(temp2)
##        timeC.append(temp3)
##    #print timeA, timeB, timeC"""
    timeD = []
    timeE = []
    timeF = []
    timeG = []
    for number in n:        
        temp1 = 0
        temp2 = 0
        temp3 = 0
        temp4 = 0
        for i in range(1):
            a = []
            b = []
            c = []
            d = []
            for i in range(number):
                x = random.randint(0, (2**32)-1)
                a.append(x)
                b.append(x)
                c.append(x)
                d.append(x)
            start = time()
            radixsort(a,2^4,8)
            stop = time()
            time1 = stop-start
            temp1 = temp1 + time1
           
            start = time()
            radixsort(b,2^8,4)
            stop = time()
            time2 = stop-start
            temp2 = temp2 + time2
            start = time()
            radixsort(c,2^16,2)
            stop = time()
            time3 = stop-start
            temp3 = temp3 + time3
            start = time()
            radixsort(d,2^1,32)
            stop = time()
            time4 = stop-start
            temp4 = temp4 + time4
        temp1 = temp1/1.0
        temp2 = temp2/1.0
        temp3 = temp3/1.0
        temp4 = temp4/1.0
        print str(number) + "radix每段4bit :"
        print temp1
        print str(number) + "radix每段8bit :"
        print temp2
        print str(number) + "radix每段16bit:"
        print temp3
        print str(number) + "radix每段1bit:"
        print temp4
        timeD.append(temp1)
        timeE.append(temp2)
        timeF.append(temp3)
        timeG.append(temp3)
    print timeD, timeE, timeF, timeG
    
if __name__=='__main__':
    main()
    raw_input("finished")
