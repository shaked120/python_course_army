class Animal:
    counter = 0

    def __init__(self, name="octavio"):
        self._name = name
        self._age = 0
        Animal.counter += 1

    def Birthday(self):
        self._age += 1

    def getBirthday(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def greet(self, name):
        print("welcome", name)


def main():
    animal1 = Animal("snorlax")
    animal1.greet(animal1.get_name())
    print("age:", animal1.get_age())
    animal2 = Animal()
    animal2.greet(animal2.get_name())
    print("age:", animal2.get_age())
    animal2.set_name("muller")
    print(animal2.get_name())
    print(Animal.counter)


main()
