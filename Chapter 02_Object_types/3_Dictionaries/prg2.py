#!/usr/bin/python

# Title: Mapping Operation

D = {}
D['Name'] = 'loki'  # Create keys by assignment
D['Age'] = 21
D['Designation'] = 'UI/UX Designer'
print(D)

bob1 = dict(name='Bob', job='dev', age=30)  # Create dictionaries by Keywords
print(bob1)

bob2 = dict(zip(['name', 'job', 'age'], ['Loki', 'Developer', 23]))  # Create dictionary by zipping
print(bob2)

l1 = ['name', 'job', 'age']
l2 = ['Loki', 'Developer', 23]
F = zip(l1, l2)
P = dict(F)
print(P)
