class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal sound")

    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")


dog = Dog("Buddy")
cat = Cat("Luns")

dog.speak()
cat.speak()
