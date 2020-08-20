# time complexity: O(n^2)
# https://en.wikipedia.org/wiki/Selection_sort    

def findSmallest(arr):
  smallest = arr[0]
  smallest_index = 0

  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]      
  return smallest_index

def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr

print('The sorted given list: ' + str(selectionSort([90,7,85,13,71,22,67,36,59,45])))   
#90,7,85,13,71,22,67,36,59,45
