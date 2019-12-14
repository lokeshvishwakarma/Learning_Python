#!/usr/bin/python

# Title: Sequence operation

L = [123, 'spam', 1.23, 'loki']  # list of three different types of items
print('Items in the list are:', L)
print('Length of the list is:', len(L))  # returns the numbers of items in the list
print(L[0])  # indexing by position
print(L[:-1])  # removes one element from the end of the list
print(L[:-2])  # removes two elements from the end of the list
print(L[1:])  # removes one element from the start of the list
print(L[2:])  # removes two elements from the start of the list
print(L[-1:])  # returns the last one element
print(L[-2:])  # returns the last two element
print(L[-3:])  # returns the last three element
L += [56, 'abc', 'xyz']  # concatenation makes new list too
print('Items in the new list are:', L)

'''negative  numbering starts from last'''
