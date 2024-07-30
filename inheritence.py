class Mamal:
    def walk(self):
        print("Walking")

class Dog(Mamal):
    def bark(self):
        print("Barking ...")

class Cat(Mamal):
    def meow(self):
        print("Meow meow meow ...")

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.meow()