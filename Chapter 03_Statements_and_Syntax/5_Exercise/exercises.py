"""
1. Write a short Python function, ismultiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
"""


def ismultiple(n, m):
    if n % m == 0:
        return True
    else:
        return False


# print(ismultiple(8, 3))

"""
2. Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""


def iseven(n):
    binary = bin(n)
    if binary[-1] == '1':
        print("odd", n)
    else:
        print("even", n)


# iseven(37)

"""
3. Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""


def minmax(data):
    _min = data[0]
    _max = data[0]
    for i in range(1, len(data)):
        if data[i] < _min:
            _min = data[i]
        elif data[i] > _max:
            _max = data[i]
    return _min, _max


# print(minmax([1,4,66,7,9,99]))


"""
4. Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""


def sumofsquare(n):
    total = 0
    for i in range(1, n):
        square = i ** 2
        total = total + square
    return total


# print(sumofsquare(5))


"""
5. Give a single command that computes the sum from Exercise 4, relying
on Python’s comprehension syntax and the built-in sum function.
"""
# n=4
# data=[i**2 for i in range(1,n)]
# print(sum(data))


"""
6. Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""


def sumofoddsquare(n):
    total = 0
    for i in range(1, n):
        if i % 2 != 0:
            square = i ** 2
            total = total + square
    return total


# print(sumofoddsquare(7))

"""
7. Give a single command that computes the sum from Exercise 6, relying
on Python’s comprehension syntax and the built-in sum function.
"""
# n=7
# data = [i**2 for i in range(1,n) if i % 2!=0]
# print(sum(data))

"""
8. Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index
−n≤k<0, what is the equivalent index j ≥0 such that s[j] references
the same element?
"""

# S = "equivalent"
# print(S[3])
# print(S[3-len(S)])


"""
9. What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
"""
# _list = list(range(50, 81, 10))
# print(_list)

"""
10. What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
"""
# _list = list(range(8, -9, -2))
# print(_list)

"""
11. Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""


# data = [i*2 for i in range(1,)]
def expo(n):
    a, r = 1, 2
    result = []
    for i in range(1, n + 1):
        tn = a * (r ** (i - 1))
        result.append(tn)
    return result


# print(expo(9))

# a,r, n =1,2,9
# data = [a*(r**(i-1)) for i in range(1,n+1)]
# print(data)
