# time complexity: O(n log n)
# https://en.wikipedia.org/wiki/Quicksort

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:                                                                 
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print('The sorted given list: ' + str(quicksort([90,7,85,13,71,22,67,36,59,45])))    
