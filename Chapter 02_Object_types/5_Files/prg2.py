#!/usr/bin/python

# Title: Binary Byte Files

import struct

packed = struct.pack('>i4sh', 7, b'spam', 8)  # Create packed binary data
print(packed)
file = open('data.bin', 'wb')  # Open binary output file
file.write(packed)  # Write packed binary data
file.close()

data = open('data.bin', 'rb').read()  # Open/read binary data file
print(data)
print(data[4:8])  # Slice bytes in the middle
print(list(data))  # A sequence of 8-bit bytes
print(struct.unpack('>i4sh', data))  # Unpack into objects again
