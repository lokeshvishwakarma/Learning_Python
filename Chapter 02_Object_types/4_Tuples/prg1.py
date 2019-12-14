#!/usr/bin/python

# Title: Tuples

"""Tuples are sequences, like lists, but they are immutable, like strings.
Functionally, they’re used to represent fixed collections of items."""

T = (1, 2, 3, 4)  # A 4-item tuple
print(T)
T += (5, 6, 4)
print(T)  # Tuple concatenation
print(T.index(4))  # index method returns the value present at that particular index
print(T.count(4))  # count method returns the number of times a value occurs in the tuple
# T[0] = 2 # Tuples are immutable
T = 'spam', 3.0, [11, 22, 33]  # the parentheses enclosing a tuple’s items can usually be omitted
print(T)
