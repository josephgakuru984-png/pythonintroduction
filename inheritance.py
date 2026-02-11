
#parent clas/base class/super class
class Animal:
    isMammal = True

    def speek(self):
        print("Animal is speaking")

   # child class/derived class/sub class
class Cat(Animal):
    def meow(self):
        print("Cat is meow")

    def climb(self):
        print("Cat is climbing a tree")

class Donkey:
    hasTail = True

    def move(self):
     print("Donkey is moving")

a = Animal()

c = Cat()


d = Donkey()