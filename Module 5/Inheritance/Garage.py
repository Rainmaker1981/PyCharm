from Room import Room

class Garage(Room):
    __bay_numbers = None

    def __init__(self, width, length, bay_numbers):
        super().__init__(width, length)
        self.set_bay_numbers(bay_numbers)

# helpers

# getters
    def get_bay_numbers(self):
        return self.__bay_numbers

# setters
    def set_bay_numbers(self, bay_numbers):
        self.__bay_numbers = bay_numbers

# string
    def __str__(self):
        return "Garage:" + super().__str__()[5:] + "\tBays: " + str(self.get_bay_numbers()) + "\n"