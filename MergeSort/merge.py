# time complexity: O(1), O(2), O(n log n)   
# https://en.wikipedia.org/wiki/Merge_sort

def mergesort(a):
  if len(a) == 1:
    return a
  elif len(a) == 2:
    if a[0] > a[1]:
      return [a[1], a[0]]
    else:
      return a

  p = len(a)//2
  m1 = mergesort(a[:p])
  m2 = mergesort(a[p:])

  ret = []
  while 1:
    if len(m1) > 0 and len(m2) > 0:
      if m1[0] <= m2[0]:
        ret.append(m1[0])
        m1 = m1[1:]
      else:
        ret.append(m2[0])
        m2 = m2[1:]
    elif len(m1) > 0:
      ret += m1
      m1 = []
    elif len(m2) > 0:
      ret += m2
      m2 = []
    else:
      break
  return ret

a = [90,7,85,13,71,22,67,36,59,45]
print('The sorted given list: '+ str(mergesort(a)))














'''
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
'''

