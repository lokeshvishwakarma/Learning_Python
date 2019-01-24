#!/usr/bin/python

#Title: List comprehension "expression"(complex operations)

M=[[1,2,3],
   [4,5,6],
   [7,8,9]]	#matrix in the form of list
print('The matrix is:',M)
col1=[row[0] for row in M]
print('Column 1 elements are:',col1)

M1=[row[1]+4 for row in M]	#add 4 to each element in column 2
print('The matrix with addition is:',M1)

M2=[row[1] for row in M if row[1]%2==0]	#filter out odd items in column 2
print('The filtered even column is:',M2)

diag=[M[i][i] for i in [0,1,2]]	#collect diagonal elements from matrix
print('Diagonal elements of the matrix are:',diag)

doubles=[i*2 for i in 'spam']	#repeat the letters in a string
print(doubles)

'''The SYNTAX is:
counter with index for counter in object
Here for loop is used with "i" as a counter'''

'''M=[i[1]-1 for i in M]	#add 4 to each element in column 2
print('The matrix with subtraction is:',M)
TypeError: 'int' object is not subscriptable'''

'''Matrix subtraction doesn't take place in "lists" '''
