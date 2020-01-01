# Write a function which takes a number and checks whether it is prime number or not

def prime(number):
    for i in range(2, number):
        if number % i == 0:
            print("Not a prime Number")
            break
    else:
        print("is a prime number")


# user_num = int(input("please enter a number"))
# prime(user_num)

# D = {'a': 1, 'b': 2, 'c': 3}
# for i, j in D.items():
#     print(i, j)

_list = ['loki', 'datta', 'sid']
# for i in range(len(_list)):
#     print(i, _list[i])

for i, j in enumerate("datta", start=1):
    print(i, j)
