class Animals:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.fun = 0

    def play(self):
        self.fun += 1

    def eat(self):
        if self.hunger > 0:
            self.hunger -= 1

    def go_to_toilet(self):
        self.hunger += 1


def main():
    animal1 = Animals("ofir")
    animal1.play()


main()
