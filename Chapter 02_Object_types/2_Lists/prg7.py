#!/usr/bin/python

# Title: List comprehension "expression"(generators,map function,sets)

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]  # matrix in the form of list
print('The matrix is:', M)

col1 = [row[0] for row in M]
print('Column 1 elements are:', col1)

G = (sum(row) for row in M)  # create a generator of row sums
print('Addition of row 1 is:', next(G))  # next method is used for iterations
print('Addition of row 2 is:', next(G))
print('Addition of row 3 is:', next(G))

# map function can do similar work
print(list(map(sum, M)))

set1 = {sum(row) for row in M}
print(set1)

dictionary = {i: sum(M[i]) for i in range(3)}
print(dictionary)

X = [ord(x) for x in 'spaam']  # List of character ordinals
print(X)

X = {ord(x) for x in 'spaam'}  # Sets remove duplicates
print(X)

X = (ord(x) for x in 'spaam')  # Generator of values
print(X)
