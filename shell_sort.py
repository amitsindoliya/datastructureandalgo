## SHELL SORT ##
## It is a variation of insertion sort
# here first we take a shell size e.g. k 
# compare element with the element at current+k position and swap
# if necessary
# then we move to second pass were value of k is reduced and so on
# and finally we get an insertion sort since k is 1
# the idea is making the array partially sorted so in the 
# last pass insertion sort can quickly sort the list
# complexity UNCLEAR
# Unstable
# don't use even value for k
# many formulas to calculate k here we are using 3x+1


def shell_sort(iterable):
    k = 0
    while 3*k < len(iterable):
        k = 3*k + 1
    while k > 0:
        for i in range(len(iterable)-k):
            for j in range(i+k,-1,-k):
                if j-k >= 0 and iterable[j-k] > iterable[j]:
                    iterable[j-k], iterable[j] = iterable[j], iterable[j-k]
                else:
                    break
        k = int((k-1)/3)
        
    return iterable
    
if __name__  == "__main__":
    iterable = [ 4,2,5,2,-6,2,8,5,2,1,8]
    print(shell_sort(iterable))
