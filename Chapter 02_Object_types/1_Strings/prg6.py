#!/usr/bin/python

#Title: Other ways to code strings
from _sitebuiltins import _Printer

S='spam'
print(len(S))

S='A\nB\tC'	#\n is end of line,\t is tab
print(len(S))	#Each stands for just each character

print(ord('\r'))    #\r is a byte with binary value 13 in ASCII
print(ord('\f'))    #\f is a byte with binary value 12 in ASCII
print(ord('\v'))    #\f is a byte with binary value 11 in ASCII
print(ord('\n'))	#\n is a byte with binary value 10 in ASCII
print(ord('\t'))    #\t is a byte with binary value 9 in ASCII
print(ord('\b'))    #\b is a byte with binary value 8 in ASCII
print(ord('\a'))    #\f is a byte with binary value 7 in ASCII


S='A\0B\0C'	#\0, a binary zero byte does not terminate string
print(S)    # Non-printables are displayed as \xNN hex escapes
print(len(S))	#Each stands for just each character

#####output#######
#4
#5
#10
#5
