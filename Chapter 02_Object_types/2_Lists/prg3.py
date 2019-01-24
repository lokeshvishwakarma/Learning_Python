#!/usr/bin/python3

#Title: Bounds checking

L=[123,'spam',1.23,'loki']			#list of three different types of items
print('Items in the list are:',L)

'''L[99]
IndexError: list index out of range
L[99] = 1
...error text omitted...
IndexError: list assignment index out of range'''
