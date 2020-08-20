import math
from time import sleep 
import re
#from classsum import sumAll

def sort_given_list():
    arr = []
    num  = int(input('How many numbers: '))# take the serie number
    for n in range(num):
        numbers = int(input('Enter number: '))
        arr.append(numbers)# add to the list the numbers in the serie
        arr.sort()
    sleep(0.1)
    print('The sorted given list is: ' + str(arr))
    sm = sum(arr[0:len(arr)])
    print('The sum list is: ' + str(sm))
sort_given_list()    


