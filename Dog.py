from animals import Animals


class Dog(Animals):
    def __init__(self, name, fur_color):
        Animals.__init__(self, name)
        self.fur_color = fur_color

    def go_for_a_walk(self):
        self.fun += 2
        print("woff woff! my fun level is rising, and its: ", self.fun)

    def __str__(self):
        return "my name is {} and i am a dog!".format(self.name)

    def eat(self):
        super().eat()
        print("eating a bone!")


def main():
    dog1 = Dog("Flupy", "Brown")
    dog1.play()
    dog1.eat()
    dog1.go_for_a_walk()
    print(isinstance(2, int))
    print(issubclass(Dog, Animals))
    ofir = Dog("sumo", "brown")
    print(ofir)


main()


class A:
    def one(self):
        return self.two()

    def two(self):
        print('A')


class B(A):
    def two(self):
        print('B')


def main():
    my_object = B()
    my_object.two()


main()
