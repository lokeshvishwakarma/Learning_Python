#!/usr/bin/python

#Title: List comprehension "expression"

M=[[1,2,3],
   [4,5,6],
   [7,8,9]]	   #matrix in the form of list
print('The matrix is:',M)
col1=[i[0] for i in M]
print('Column 1 elements are:',col1)
col2=[i[1] for i in M]
print('Column 2 elements are:',col2)
col3=[i[2] for i in M]
print('Column 3 elements are:',col3)

'''The SYNTAX is:
counter with index for counter in object
Here for loop is used with "i" as a counter'''
