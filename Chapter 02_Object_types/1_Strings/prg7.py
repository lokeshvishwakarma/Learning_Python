#!/usr/bin/python

# Title: Unicode Strings

S = 'Sp\xc4m'  # normal strings
print(S)
S = 'Sp\xcam'  # normal strings
print(S)

S = r'C:\home\loki'  # raw strings
print(S)

print(u'sp\xc4m')  # 2.X: Unicode strings are a distinct type
S = b'a\x01c'  # byte strings are byte based data
print(S)

S = 'spam'.encode('utf8')  # Encoded to 4 bytes in UTF-8 in files
print(S)

S = 'spam'.encode('utf16')  # Encoded to 10 bytes in UTF-16 in files
print(S)

'''bytearray type strings are in-place mutable strings.
b"loki" here 'b' before the string indicates a byte-string.
r"C:\home\loki" here 'r' before the string indicates a raw-string'''

# u'x' + b'y'
# u'x' + 'y'      # Works in 2.X (where b is optional and ignored)
# Works in 2.X: u'xy'
# u'x' + b'y'
# u'x' + 'y'      # Fails in 3.3 (where u is optional and ignored)
# Works in 3.3: 'xy'
S = 'x' + b'y'.decode()
print(S)

'''To write the bytearray type string we need to decode it using decode method'''
S = 'x'.encode() + b'y'
print(S)
# Works in 3.X if decode bytes to str: 'xy'
# Works in 3.X if encode str to bytes: b'xy'
