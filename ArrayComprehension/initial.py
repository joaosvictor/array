

Creation
L = ['yellow', 'red', 'blue', 'green', 'black']
>>>print L
returns: ['yellow', 'red', 'blue', 'green', 'black']

##########

Accessing / Indexing
L[0]  = returns 'yellow'

##########

Slicing
L[1:4]  = returns ['red', 'blue', 'green']
L[2:] 	= returns ['blue', 'green', 'black']
L[:2] 	= returns ['yellow', 'red']
L[-1]  	= returns 'black'
L[1:-1] = returns ['red', 'blue', 'green']

##########

Length - number of items in list
len(L)  = returns 5

##########

Sorting - sorting the list
sorted(L) = returns ['black', 'blue', 'green', 'red', 'yellow']

##########

Append - append to end of list
L.append("pink")

>>> print L
returns: ['black', 'blue', 'green', 'red', 'yellow', 'pink']

##########

Insert - insert into list
L.insert(0, "white")

>>> print L
returns: ['white', 'black', 'blue', 'green', 'red', 'yellow', 'pink']

##########

Extend - grow list

L.extend(L2)

##########

Remove - remove first item in list with value "white"

L.remove("white")

>>> print L
returns: ['black', 'blue', 'green', 'red', 'yellow', 'pink']

##########

Delete

Remove an item from a list given its index instead of its value
del.L[0]

>>> print L
['blue', 'green', 'red', 'yellow', 'pink']

##########

Pop

Remove last item in the list
L.pop()  = returns 'pink'

# remove indexed value from list
L.pop(1) = returns 'green'  

##########

Reverse - reversing the list
L.reverse()

##########

Count

Search list and return number of instances found
L.count('red')

##########

Keyword "in" - can be used to test if an item is in a list
 
if 'red' in L:
    print "list contains", 'red'

##########

For-in statement - makes it easy to loop over the items in a list
for item in L:
    print item

L = ['red', 'blue', 'green']
for col in L:
    print col
