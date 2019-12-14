#!/usr/bin/python

# Title: Type specific methods(functions)

S = 'lokesh vishwakarma'
print('The string is: ' + S)

offset = S.find('vish')  # Find the offset of a substring including 'blank-space'
print('The offset is: ', offset)

S = S.replace(' ', ' premshankar ')  # Replace occurrences of a substring with another
print('After replacement the string is: ' + S)

line = 'aaa, bbb, ccccc, dd\n'
print(line.split(','))  # split on a delimiter i.e(,) into a list of substrings
# delimiter can be any symbol(even a space)

print(line.rstrip())  # remove whitespace characters on the right side

print(line.rstrip().split())  # combine two operations

S = 'spam'
print(S.upper())  # upper case conversion
print(S.lower())  # lower case conversion

print(S.isalpha())  # content tests: isalpha,isdigit,etc
print('%s,abc, %d , xyz and %s' % ('pqr', 123, 'lmn'))  # formatting expression
print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))  # format() method
print('{}, eggs, and {}'.format('spam', 'SPAM!'))  # numbers optional in python2.7+
