class Dog:
    AnimalType = "Mammals"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __repr__(self):
        return "Dog Name: {}, Breed: {} Created".format(self.name, self.breed)


mydog = Dog("Tommy", "Husky")
mydog2 = Dog("Loki", "Lab")
print(mydog.name)
print(mydog.AnimalType,type)
print(mydog2.name)
