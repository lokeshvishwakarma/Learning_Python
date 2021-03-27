from mymaths.vectors import Vector

a = Vector(2, 3, 5)
b = Vector(2, 4, 6)

# c = a.add(b)

c = a + b   # operator overloading
d = b - a
print(c, type(c))
print(d, type(c))
