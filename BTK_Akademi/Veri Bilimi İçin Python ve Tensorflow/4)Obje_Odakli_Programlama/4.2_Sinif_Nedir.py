class Animal():
    def __init__(self):
        print("Animal Class is Called!")

    def func1(self):
        print("func1 Function is Called in Animal Class!")

class Cat(Animal):
    def __init__(self, yas):
        Animal.__init__(self)
        print("Cat Class is Called!")
        self.yas = yas

    def func1(self):  # override
        print("func1 Function is Called in Cat Class!")


class Dog(Animal):
    def __init__(self, yas):
        Animal.__init__(self)
        print("Dog Class is Called!")
        self.yas = yas

    def humanage(self):
        return self.yas * 7


print("--------------")

myDog = Dog(3)
print(myDog.yas)
print(myDog.humanage())
print("--------------")

myCat = Cat(3)
myCat.func1()
myDog.func1()
print("--------------")
