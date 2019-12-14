#!/usr/bin/python

# Title: Files

"""File objects are Python code’s main interface to external files on your computer.
 They can be used to read and write text memos, audio clips, etc."""

f = open('data.txt', 'w')  # Make a new file in output mode ('w' is write)
f.write('Hello\nWorld !!!')
f.close()

f = open('data.txt', 'r')  # read is the default processing mode ('r' is read)
text = f.read()  # read entire file into string
print(text)
print(text.split())

for line in open('data.txt'):
    print(line)
