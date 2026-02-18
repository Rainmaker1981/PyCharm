from Room import Room

class Bedroom(Room):
    __color = None

    def __init__(self, width, length, color):
        super().__init__(width, length)
        self.set_color(color)

# helpers

# getters
    def get_color(self):
        return self.__color

# setters
    def set_color(self, color):
        self.__color = color

# string
    def __str__(self):
        return "Bedroom:" + super().__str__()[5:] + "\tColor: " + str(self.get_color()) + "\n"