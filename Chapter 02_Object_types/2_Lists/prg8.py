#!/usr/bin/python

print(list(range(4)))
print(list(range(-6,7,2)))
l1 = [[x**2,x**3] for x in range(4)]    #list comprehension
print(l1)                               #syntax is : [expression iteration condition]
l2 = [[x, x // 2, x * 2] for x in range(-6,7,2) if x > 0]
print(l2)