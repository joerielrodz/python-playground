class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")


dog1 = Dog("Buddy", 3)


print(dog1.name)
print(dog1.age)
dog1.bark()
