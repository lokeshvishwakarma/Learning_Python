#!/usr/bin/python

# Title: Pattern Matching

"""import a module called "re" i.e, regular expression
This module has analogous calls for searching, splitting, and replacement"""

import re

match = re.match('Hello[\t]*(.*)world', 'Hello	Python world')
m = match.group(1)
print(m)  # here in this case starting and ending word is matched & everything lying in between is returned
'''This example searches for a substring that begins with the word
“Hello,” followed by zero or more tabs or spaces, followed by arbitrary
characters to be saved as a matched group, terminated by the word
“world.” If such a substring is found, portions of the substring
matched by parts of the pattern enclosed in parentheses are available
as groups.'''

print()

match = re.match('/(.*)/(.*)/(.*)', '/usr/bin/loki')
m = match.groups()
print(m)

match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
m = match.groups()
print(m)

m = re.split('[/:]', '/usr/home:lumberjack')
print(m)
