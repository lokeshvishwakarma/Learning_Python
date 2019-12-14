#!/usr/bin/python

# Title: Getting help
S = 'spam'
d = dir(S)  # dir() simply gives the methods' names
print('The list of method names are as follows:\n\n', d)
print('\n\n')
h = help(S.replace)  # help on built-in function replace

print(S + ' loki')
print(S.__add__(' loki'))
'''The methods starting end ending with underscores represent
the implementation of the string object.
In general, leading and trailing double underscores is the
naming pattern Python uses for implementation details.
The names without the underscores in this list are the
callable methods on string objects.'''
