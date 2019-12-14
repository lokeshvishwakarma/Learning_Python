#!/usr/bin/python

# Title: Unicode Text Files

"""Text files are used to process all sorts of text-based data, from memos to email content
 to JSON and XML documents."""

S = 'sp\xc4m'  # Non-ASCII Unicode text
print(S)
print(S[2])  # Sequence of characters

file = open('unidata.txt', 'w', encoding='utf-8')  # Write/encode UTF-8 text
file.write(S)
file.close()

text = open('unidata.txt', encoding='utf-8').read()  # Read/decode UTF-8 text
print(text)
print(len(text))

raw = open('unidata.txt', 'rb').read()  # Read raw encoded bytes
print(raw)
print(len(raw))  # Really 5 bytes in UTF-8

print(text.encode('utf-8'))  # Manual encode to bytes
print(raw.decode('utf-8'))  # Manual decode to str
