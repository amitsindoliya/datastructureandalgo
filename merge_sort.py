# --------------------------------------------  # 
#   Merge Sort : O(nlogn)                       #    
#   Follows Divide and Conquer Approach         #
# --------------------------------------------  #

def merge_sort(iterable):
    # Base condition return single element back
    if len(iterable) == 0 or len(iterable) == 1:
        return iterable
    # Calculating mid co-ordinate of the list
    n = len(iterable)//2
    # Finding Left and Right list 
    l = merge_sort(iterable[:n])
    r = merge_sort(iterable[n:])
    i, j = 0, 0
    m =[0]*len(iterable)
    # print(l,r)
    # Merging the left and right list O(n)
    for k in range(len(m)):
        if i == len(l) or j == len(r):
            break
        if l[i] <= r[j]:
            m[k] = l[i]
            i+=1
        elif r[j] <= l[i]:
            m[k] = r[j]
            j+=1
    
    # Sometimes elements are still present in left or right list
    # Adding those to merged list
    while i < len(l):
        m[k] = l[i]
        i+=1
        k+=1
    while j < len(r):
        m[k] = r[j]
        j+=1
        k+=1
    return m
    
if __name__ =="__main__":
    iterable = [7,9,1,4,7,8,1,5,6,8]
    print(merge_sort(iterable))
        
