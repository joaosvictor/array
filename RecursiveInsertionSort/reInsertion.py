# time complexity: O(n). It occurs in the case when the input is already/almost sorted. 
# https://en.wikipedia.org/wiki/Insertion_sort

def recursiveinsertion(arr, n):
    if n <= 1:
        return

    recursiveinsertion(arr, n-1)

    last = arr[n-1]
    j = n-2

    while (j >= 0 and arr[j] > last):
        arr[j+1] = arr[j]
        j = j-1

    arr[j+1] = last

def printarr(arr, n):
    print ('The sorted given list: '+ str(arr))

arr = [90,7,85,13,71,22,67,36,59,45]
n = len(arr)
recursiveinsertion(arr, n)
print(printarr(arr, n))
                
