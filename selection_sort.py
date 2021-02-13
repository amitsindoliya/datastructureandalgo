## selection Sort ##
## In selection sort we find the minimum element or maximum element
# of the list and place it at the start 
# continue this operation until we have an sorted array
# complexity O(N^2)/2
# unstable
  
def selection_sort(iterable):
    for i in range(len(iterable)-1):
        for j in range(i+1,len(iterable)):
            if iterable[j] < iterable[i]:
                iterable[i], iterable[j] = iterable[j], iterable[i]
    return iterable
    
    
if __name__  == "__main__":
    iterable = [ 4,2,5,2,-6,2,8,5,2,1,8]
    print(selection_sort(iterable))
