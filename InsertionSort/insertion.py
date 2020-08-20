# time complexity: O(n)
# https://en.wikipedia.org/wiki/Insertion_sort

def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [90,7,85,13,71,22,67,36,59,45]        
insertionsort(arr)
print('The sorted given list: ' + str(arr))

