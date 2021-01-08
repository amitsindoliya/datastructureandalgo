# -----------------------------------------------------------------#
# --------------------Binary Search O(logn)------------------------#
# -----------------------------------------------------------------#

def binary_search(iterable, elem):
    # Intialize left and right to start and end 
    # calculate mid element
    l = 0
    r = len(iterable)-1
    m = (l+r)//2
    # print(l,r)
    # If elem in mid then return
    # if elem in mid is higher than search term then reduce r to m
    # if elem in mid is lower than search term then increase l to m
    while l <= r:
        # print(l,r,m)
        if iterable[m] == elem:
            return m
        if iterable[m] > elem:
            r = m -1
            m = (l+r)//2
        elif iterable[m] < elem:
            l = m + 1
            m = (l+r)//2
    

    return -1
   
