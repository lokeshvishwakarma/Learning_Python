#!/usr/bin/python

# Title: Type-specific operations

"""Python’s lists are related to arrays in other languages, but they tend to be more powerful.
For one thing, they have no fixed type constraint—the list we just looked at, for example,
contains three objects of completely different types (an integer, a string, and a
floating-point number). Further, lists have no fixed size. That is, they can grow and
shrink on demand, in response to list-specific operations:"""

L = [123, 'spam', 1.23, 'loki']  # list of three different types of items
print('Items in the list are:', L)
L += [56, 'abc', 'xyz']  # concatenation makes new list too
print('Items in the concatenated list are:', L)

L.append('NI')  # Growing: adding object at the end of the list
print('Items in the appended list are:', L)
L.append([99])  # appends as an object itself
print('Items in the appended list are:', L)
L.extend([38])  # extends the list as a new item in previous list
print('Items in the extended list are:', L)
M = L.pop(3)  # Shrinking: deleting an item by index
print('Deleted item is:', M)
print('Items in the list after deleting are:', L)
del L[2]  # "del L[2]" deletes from a list too
print('Items in the list after deleting are:', L)

M = ['bb', 'cc', 'aa']
print('\nItems in the list are:', M)
M.sort()
print('Items in the sorted list are:', M)
M.reverse()
print('Items in the reverse list are:', M)
