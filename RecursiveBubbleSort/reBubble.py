# time complexity: O(n^2)
# https://en.wikipedia.org/wiki/Bubble_sort

def recursive_bubble(arr):
    for i, num in enumerate(arr):
        try:
            if arr[i+1] < num:
                arr[i] = arr[i+1]
                arr[i+1] = num
                recursive_bubble(arr)
        except IndexError:
            pass           
    return arr

arr = [90,7,85,13,71,22,67,36,59,45]
recursive_bubble(arr)

print('The sorted given list: ' + str(arr))

