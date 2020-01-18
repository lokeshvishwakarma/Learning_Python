#!/usr/bin/python

"""
Exception Handling
"""

mylist = [1, 2, 3, 4, 5, 6]

try:
    print(mylist[20])
except Exception as e:
    print("Exception:", e)


def test():
    try:
        import pandas
    except ModuleNotFoundError as e:
        print("Exception:", e)
        raise e


print(test())
