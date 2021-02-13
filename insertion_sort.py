### insertion sort #####
# items before key are sorted the new item is inserted based on its value
# compares with each value until e are at the start of the list or we are
# at the required position
# stable sort
# complexity O(N^2)/4
# best case when list is partitially sorted O(N)

def insertion_sort(iterable_item):
    for i in range(len(iterable_item)-1):
        for j in range(i+1,-1,-1):
            # print(iterable_item[j],j,i, iterable_item[j-1])
            if j-1 >= 0 and iterable_item[j] < iterable_item[j-1]:
                iterable_item[j-1], iterable_item[j] = iterable_item[j], iterable_item[j-1]
                # print(iterable_item)
            else:
                break
    return iterable_item
            
    
    
if __name__  == "__main__":
    iterable = [ 4,2,5,2,6,2,8,5,2,1,8]
    print(insertion_sort(iterable))
