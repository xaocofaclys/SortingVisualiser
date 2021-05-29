# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'


from random import randint
from time import time
from pandas import DataFrame
from matplotlib import pyplot as plt


def create_array(size=10,max=50):
    #print(f"log{size}")
    return [randint(0,max) for _ in range(size)]
####-----------------------Merge Sort--------------------------------------------############
def merge(a,b):
    c = list()
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if(a[i] < b[j]):
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    if i == len(a):c.extend(b[j:])
    else: c.extend(a[i:])
    return c

def merge_sort(a):
    if(len(a)<=1):return a
    left,right = merge_sort(a[:len(a)//2]),merge_sort(a[len(a)//2:])
    return merge(left,right)

########################################---Bubble Sort---------------------##############################
def bubblesort(a):
    for i in range(len(a)-1):
        for j in range(0,len(a)-i-1):
            if(a[j] > a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]

    
#####################################---- Selection Sort-----------------------#########################
def selection_sort(a):
    slen = 0
    while(slen < len(a)):
        minid = None
        for i,x in enumerate(a[slen:]):
            if minid == None or x < a[minid]:
                minid = i+slen
        a[slen],a[minid] = a[minid],a[slen]
        slen+=1
    return a

    #xaocofachlys
################--------------------------Insertion Sort------------------------------##############
def insertion_sort(a):
    for slen in range(1,len(a)):
        citem = a[slen]
        inidx = slen
        while inidx >0 and citem < a[inidx - 1]:
            a[inidx] = a[inidx-1]
            inidx -= 1
        a[inidx] = citem
    return a
#####################################---- Quick Sort-----------------------#####################
def quicksort(a):
    if len(a) <= 1: return a
    s,e,l = [],[],[]
    pivot = a[randint(0,len(a)-1)]
    for x in a:
        if x < pivot: s.append(x)
        elif x == pivot : e.append(x)
        else : l.append(x)
    return quicksort(s)+e+quicksort(l)
def partition(a,l,h):
    i = l-1
    pivot = a[h]
    for j in range(l,h):
        if(a[j] <= pivot):
            i+=1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[h] = a[h],a[i+1]
    return i+1
def quicksort_implace(a,l = 0,h = None):
    if h == None:
        h = len(a) - 1
    if l<h:
        pidx = partition(a,l,h)
        quicksort_implace(a,l,pidx - 1)
        quicksort_implace(a,pidx+1,h)
################--------------------------Visualiser------------------------------##############
def visualise(tos):
    n = list(randint(0,1000) for _ in range(0,randint(1000,1050)))
    if(tos == 2):
        times = []
        for s in n:
            a = create_array(s,s)
            startingtime = time()
            merge_sort(a)
            endtime = time()
            times.append(endtime-startingtime)
        X = DataFrame(times)
        Y = DataFrame(n)
        plt.scatter(X,Y)
        plt.xlabel('time_taken_to_sort_the_array')
        plt.ylabel('Size_of_the_array')
        plt.title('Merge_Sort!!')
        plt.show()
    if(tos == 1):
        times = list()
        for s in n:
            a = create_array(s,s)
            startingtime = time()
            bubblesort(a)
            #print(f"colog{s}")
            endtime = time()
            times.append(endtime-startingtime)
        X = DataFrame(times)
        Y = DataFrame(n)
        plt.scatter(X,Y)
        plt.xlabel('time_taken_to_sort_the_array')
        plt.ylabel('Size_of_the_array')
        plt.title('Bubble_Sort!!')
        plt.show()
    if(tos == 3):
        times = list()
        for s in n:
            a = create_array(s,s)
            startingtime = time()
            selection_sort(a)
            endtime = time()
            times.append(endtime-startingtime)
        X = DataFrame(times)
        Y = DataFrame(n)
        plt.scatter(X,Y)
        plt.xlabel('time_taken_to_sort_the_array')
        plt.ylabel('Size_of_the_array')
        plt.title('Selection_Sort!!')
        plt.show()
    if(tos == 4):
        times = list()
        for s in n:
            a = create_array(s,s)
            startingtime = time()
            insertion_sort(a)
            endtime = time()
            times.append(endtime-startingtime)
        X = DataFrame(times)
        Y = DataFrame(n)
        plt.scatter(X,Y)
        plt.xlabel('time_taken_to_sort_the_array')
        plt.ylabel('Size_of_the_array')
        plt.title('Insertion_Sort!!')
        plt.show()
    if(tos == 5):
        times = list()
        for s in n:
            a = create_array(s,s)
            startingtime = time()
            selection_sort(a)
            endtime = time()
            times.append(endtime-startingtime)
        X = DataFrame(times)
        Y = DataFrame(n)
        plt.scatter(X,Y)
        plt.xlabel('time_taken_to_sort_the_array')
        plt.ylabel('Size_of_the_array')
        plt.title('Quick_Sort!!')
        plt.show()
    if(tos == 6):
        times = list()
        for s in n:
            a = create_array(s,s)
            startingtime = time()
            quicksort_implace(a)
            endtime = time()
            times.append(endtime - startingtime)
        X = DataFrame(times)
        Y = DataFrame(n)
        plt.scatter(X,Y)
        plt.xlabel('time_taken_to_sort_the_array')
        plt.ylabel('Size_of_the_array')
        plt.title('Quick_Sort_Implace!!')
        plt.show()

        #xaocofachlys




# ###--------------------------------Main------------------------------------

# while(True):
#     print("Enter 1. For the graph of  Bubble sort!!")
#     print("Enter 2. For the graph of  Merge sort!!")
#     print("Enter 3. For the graph of  Selection sort!!")
#     print("Enter 4. For the graph of  Insertion sort!!")
#     print("Enter 5. For the graph of  Quick sort!!")
#     print("Enter 6. For the graph of  Quick sort implace !!")
#     print("Enter 7. to  quit the program !!")

#     choice = int(input())

#     if(choice == 1): visualise(1)
#     elif(choice == 2): visualise(2)
#     elif(choice == 3): visualise(3)
#     elif(choice == 4): visualise(4)
#     elif(choice == 5): visualise(5)
#     elif(choice == 6): visualise(6)
#     elif(choice == 7): break
#     else:print("Wrong Choice Check again!!")

#     #xaocofachlys







































