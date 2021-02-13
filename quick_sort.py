## QUICK SORT ##
# quick sort is an inplace nlogn algorithm
# in practice it is a little fster than merge sort because it 
# has less operation for each element
# unstable algorithm
# Actual worst case complexity is O(N^2)/2 but is not observed
# in real world scenario due to random shuffling of array at the start
# after random shuffling the first element is taken as K
# Two pointers one just after k and another at the end are initialized
# suppose i and j are the two pointer
# if value at i is less than value at k we increment i else we stop and
# check if j is greater than k we decrement it otherwise we stop and
# swap values at i and j we do this until i > j
# then we swap value at j with k all elements to the left of k are
# smaller than k and all elements to the right of k are greater than k
# we repeat the operation at both halves until we get an sorted array
# quick sort doesn't work well for duplicates that is why generally
# 3 way quick sort is used
import random

def partition(a, lo, hi):
    i = lo + 1
    j = hi
    # print(i,j)
    while True:
        # print(a[i],i)
        while a[i] <= a[lo]:
            # print('here')
            i += 1
            if i == hi:
                break
        while a[j] >= a[lo]:
            # print('there')
            j -= 1
            if j == lo:
                break
        if i >= j:
            break
        a[i],a[j] = a[j],a[i]
        # print(a[i],a[j],i,j)
    a[j], a[lo] = a[lo], a[j]
    return j

def qs(iterable, lo , hi):
    # print(iterable[lo:hi+1])
    if lo >= hi:
        return
    j = partition(iterable, lo ,hi)
    # print(j)
    qs(iterable, lo, j-1)
    qs(iterable, j+1, hi)

def quick_sort(iterable):
    random.shuffle(iterable)
    # print(iterable)
    qs(iterable, 0 ,len(iterable)-1)
    # print(iterable)
    # return iterable
    
if __name__ =='__main__':
    iterable = [-6,5,2,6,32,3,2,6,3,7,2,1,1,1,4,6,41,1]
    
    quick_sort(iterable)
    print(iterable)
