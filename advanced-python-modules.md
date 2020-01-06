# Advanced Python Modules

## List Comprehensions

## Generators

## Decorators

```python
def adder(func):
    def inner(whatever):
        return func(whatever) + 1

    return inner

def hi(n):
    return n

obj = adder(hi)

print obj(1)
```

```python
# defining a decorator
def outer(func):
    print("Outer")

    def inner1():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behavior
_function = outer(function_to_be_used)

# calling the function
_function()
```

