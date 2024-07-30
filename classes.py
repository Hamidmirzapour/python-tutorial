class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I'm {self.age} years old.")

    def get_age(self):
        return self.age
    
user1 = Person("Hamid", 28)
user1.introduce()
print(user1.get_age())

user2 = Person("Zahra", 25)
user2.introduce()
print(user2.get_age())