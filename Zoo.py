class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name):
        self._name = name
        self._hunger = 0

    def get_name(self):
        return self._name

    def set_hunger(self, hunger):
        self._hunger = hunger

    def is_hungry(self):
        if self._hunger > 0:
            return True
        else:
            return False

    def feed(self):
        self._hunger -= 1

    @property
    def hunger(self):
        return self._hunger


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir")


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.stink_count = 6

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!	")


class Unicorn(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.color = "Green"

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$	")


def main():
    dog = Dog("Brownie")
    cat = Cat("Zelda")
    skunk = Skunk("Stinky")
    unicorn = Unicorn("Keith")
    dragon = Dragon("Lizzy")
    dog.set_hunger(10)
    cat.set_hunger(3)
    skunk.set_hunger(0)
    unicorn.set_hunger(7)
    dragon.set_hunger(1450)
    zoo_lst = [dog, cat, skunk, unicorn, dragon]
    dog1 = Dog("Doggo")
    cat1 = Cat("Kitty")
    skunk1 = Skunk("Stinky Jr.	")
    unicorn1 = Unicorn("Clair")
    dragon1 = Dragon("McFly")
    dog1.set_hunger(80)
    cat1.set_hunger(80)
    skunk1.set_hunger(80)
    unicorn1.set_hunger(80)
    dragon1.set_hunger(80)
    zoo_lst.append(dog1)
    zoo_lst.append(skunk1)
    zoo_lst.append(cat1)
    zoo_lst.append(unicorn1)
    zoo_lst.append(dragon1)
    for animal in zoo_lst:
        if animal.hunger > 0:
            print(animal.__class__, animal.get_name())
            animal.talk()
            if isinstance(animal, Dog):
                animal.fetch_stick()
            else:
                if isinstance(animal, Cat):
                    animal.chase_laser()
                else:
                    if isinstance(animal, Skunk):
                        animal.stink()
                    else:
                        if isinstance(animal, Unicorn):
                            animal.sing()
                        else:
                            animal.breath_fire()
            while animal.is_hungry():
                animal.feed()
    print(Animal.zoo_name)


main()
