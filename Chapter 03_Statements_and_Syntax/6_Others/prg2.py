#!/usr/bin/python

"""
Generators
"""

G = (x ** 2 for x in range(999999999))
print(G)
print(G.__next__())
print(G.__next__())
print(G.__next__())
print(G.__next__())


def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


# n = int(input("Enter a number less than 50:"))
# print("The first", n, "Fibonacci numbers are:", fibon(n))


def fibon_g(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


n = int(input("Enter a number greater than 100000:"))

G = fibon_g(n)
G.__next__()

print('Generator', G)
for obj in fibon_g(n):
    print(obj)
