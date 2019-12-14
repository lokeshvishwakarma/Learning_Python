#!/usr/bin/python

# Title: Nesting

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]  # matrix in the form of list
print('The matrix is:', M)
print(M[1])  # get row 2, as index starts from 0
print(M[1][2])  # get row 2, column 3
print(M[-1][-2])  # get last row, second last column

'''negative numbering starts from last'''
