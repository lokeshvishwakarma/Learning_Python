#!/usr/bin/python

# Title: References vs copies

X = [1, 2, 3]
L = ['a', X, 'b']  # Embed references to X's object
D = {'x': X, 'y': 2}

print(X)
print(L)
print(D)

X[1] = 'surprise'
print(X)
print(L)
print(D)

L = [1, 2, 3]
D = {'a': 1, 'b': 2}
A = L[:]  # Instead of A = L (or list(L))A = L[:]
B = D.copy()  # Instead of B = D (ditto for sets)
A[1] = 'Ni'
B['c'] = 'spam'
print(L)
print(D)
print(A)
print(B)
