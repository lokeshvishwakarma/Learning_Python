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

with open('data.txt', 'r') as f:
    # data = f.read()
    lines = f.readline()
    # r = f.seek(7)
    lines = f.readline()

print(lines)
count = 0
for line in lines:
    words = line.split(" ")
    count += len(words)

print(count)

S = "File objects are Python code’s main interface to external files on your computer."

with open('newfile.txt', 'w') as f:
    f.writelines('loki')
