from os import name


class Dog:

    def __init__(self,name,breed,hasFur):
        self.name = name
        self.breed = breed
        self.hasFur = hasFur


    def bark(self):
        print(self.name, "Woof!! Woof!!")

    def locomotive(self):
        print("Dog is walking")

Dog1 = Dog("Jj","BullDog",True)
print(Dog1.name,Dog1.breed,Dog1.hasFur)
Dog1.bark()
Dog2 = Dog("Tony","Alabai",True)
print(Dog2.name,Dog2.breed,Dog2.hasFur)
Dog2.bark()
Dog3 = Dog("Ann","chihuahua",True)
print(Dog3.name,Dog3.breed,Dog3.hasFur)
Dog3.bark()