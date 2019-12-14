#!/usr/bin/python3

# Title: Immutability of objects

S = 'loki'
print('Length of the string is: ', len(S))  # length of string stored in 'S'
print('The string is:' + S)
print('The string is:', S)

# strings are 'immutable' in python i.e they cannot be changed in-place after they are created.

# for example

# S[0] = 'z'

''' Immutable objects cannot be changed
...error text omitted...
TypeError: 'str' object does not support item assignment

But we can run expressions to make new objects'''
S = 'vishwakarma' + S[0:]  # Everything past 0th character
print('Now the string is: ' + S)

S = 'loki'
S = 'vishwakarma' + S[1:]  # Everything past 1st character
print('Now the string is: ' + S)

'''The core types, numbers, strings, and tuples are immutable;
lists and dictionaries are not (they can be changed in-place freely)'''

S = 'shrubbery'
L = list(S)  # gets a list of characters
print(L)

L[3] = 'c'
print(L)

S = ''.join(L)  # join with empty(blank-space) delimiter
print(S)

B = bytearray(b'spam')  # 'b' is required in python3.x not in python2.x
print(B)

B.extend(b' eggs')
print(B)

print(B.capitalize())  # capitalize first letter of first word of the sentence

print(B.decode())  # decode to original string

B.append(3)  # here append takes only integer
print(B)
