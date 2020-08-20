# time complexity: O(n^2)
# https://en.wikipedia.org/wiki/Bubble_sort

arr = [90,7,85,13,71,22,67,36,59,45]
for i in range(len(arr)):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                 
print('The sorted given list: ' + str(arr))                         
