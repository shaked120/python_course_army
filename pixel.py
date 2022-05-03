class Pixel:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.red = 0
        self.green = 0
        self.blue = 0

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def set_grayscale(self):
        average = (self.red + self.blue + self.green) // 3
        self.green = average
        self.blue = average
        self.red = average

    def print_pixel_info(self):
        if self.blue == 0 & self.green == 0:
            print("x: ", self.x, "y: ", self.y, "Color: ", "(", self.red, ",", self.green, ",", self.blue, ")",
                  "Red")
        else:
            if self.blue == 0 & self.red == 0:
                print("x: ", self.x, "y: ", self.y, "Color: ", "(", self.red, ",", self.green, ",", self.blue, ")",
                      "Green")
            else:
                if self.red == 0 & self.green == 0:
                    print("x: ", self.x, "y: ", self.y, "Color: ", "(", self.red, ",", self.green, ",", self.blue,
                          ")", "Blue")
                else:
                    print("x: ", self.x, "y: ", self.y, "Color: ", "(", self.red, ",", self.green, ",", self.blue,
                          ")")


def main():
    pixel1 = Pixel()
    pixel1.x = 5
    pixel1.y = 6
    pixel1.red = 250
    pixel1.green = 0
    pixel1.blue = 0
    pixel1.print_pixel_info()
    pixel1.set_grayscale()
    pixel1.print_pixel_info()


main()
