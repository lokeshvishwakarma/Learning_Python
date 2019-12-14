#!/usr/bin/python

# Title: Nesting Revisited

rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['Developer', 'Manager'],
       'age': 23
       }  # Nested dictionary
print(rec)
print(rec['name'])  # 'name' is a nested dictionary
print(rec['jobs'])  # 'jobs' is a nested list
print(rec['jobs'][-1])  # index the nested list
rec['jobs'].append('Janitor')  # expand Bob's job description in place
print(rec['jobs'])

rec = 0  # now the objects space is reclaimed
print(rec)
