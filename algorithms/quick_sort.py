#python program for implementation of quicksort
#this implementation utilizes pivot as the last element in the numbers list.
#it has a pointer to keep track of the elements smaller than the pivot.
#at the very end of partition() function, the pointer is swapped with the pivot.
#to come up with a sorted nums relative to the pivot.

#function to find the partition position
def partition(array, low, high):

    #choose the rightmost element as pivot
    pivot = array[high]
    
    #pointer for greater element
    i = low - 1
    
    #traverse through all elements
    #compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            
            #if element smaller than pivot is found
            #swap it with the greater element pointed by i
            i = i + 1
            
            #swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            
    #swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    
    #return the position from where partition is done
    return i + 1
    
#function to perform quicksort
    
    
def quicksort(array, low, high):
    if low < high:
        
        #find pivot element such that
        #element smaller than pivot are on the leftt
        #element greater than pivot are on the right
        pi = partition(array, low, high)
            
        #recursive call on the left of pivot
        quickSort(array, low, pi - 1)
            
        #recursive call on the right of pivot
        quickSort(array, pi + 1, high)
            
data = [1, 7, 4, 1, 10, 9, -2]
print("unsorted array")
print(data)
    
size = len(data)
    
quickSort(data, 0, size - 1)
    
print('sorted array in ascending order:')
print(data)
