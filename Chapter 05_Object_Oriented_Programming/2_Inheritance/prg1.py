class Animal:
    def __init__(self):
        print('Animal Created')

    def who_am_i(self):
        return 'I am an animal'

    def eat(self):
        return 'Eating'

    def __repr__(self):
        return "Animal Object"


class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__()
        print('Dog Created')

    def bark(self):
        return "Wowwww!"

    def who_am_i(self):
        return "I am a Dog!!!"


myanimal = Animal()
print(myanimal.eat())

mydog = Dog()
print(mydog.eat())
print(mydog.who_am_i())
