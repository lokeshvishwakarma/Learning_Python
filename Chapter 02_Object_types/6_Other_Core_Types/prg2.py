#!/usr/bin/python

# Title: Print to a file

x = 1
y = 2
z = 3
print(x, y, z, sep='...', file=open('data.txt', 'w'))  # Print to a file
