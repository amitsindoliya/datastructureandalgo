### jump search
# works on sorted array
# complexity is O(√N), Because we select a jump size m
# and if the value is below jumped value we traverse m-1
# so the equation is n/m + (m-1) which is minimum when m = root n

import math

def jump_search(iterable, term):
    
    # find size of m 
    m = int(math.sqrt(len(iterable)))
    # print(m)
    # since list starts from index 0
    k = m-1
    while k<=len(iterable):
        # print("-")
        if iterable[k] == term:
            return k
        if iterable[k] > term:
            break
        k += min(m,len(iterable)-k-1)
    
    # traversing the element in the m
    for x in range(k-1, k-m-1, -1):
        # print("-")
        if iterable[x] == term:
            return x
    return -1
 
if __name__ == "__main__"
    sample_list = [1,3,5,5,6,7,8,9,9,10]
    print(jump_search(sample_list,8))
        
        
    
