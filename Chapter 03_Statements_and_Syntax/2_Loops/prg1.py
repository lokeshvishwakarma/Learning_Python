#!/usr/bin/python

# Title: Loops

# For loop
n = int(input("Please enter a number"))
fac = 1
for i in range(1, n + 1):
    fac = fac * i
print(fac)

# While loop
secret_word = 'guest'

while True:
    word = input("Guess the secret word: ")
    if word == secret_word:
        print("Success!!")
        break
    else:
        print("Please try again ")
