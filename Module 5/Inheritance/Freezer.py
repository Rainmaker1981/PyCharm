from Appliance import Appliance

class Freezer(Appliance):
    __low_temp = None

    def __init__(self, type, brand, low_temp):
        super().__init__(type, brand)
        self.set_low_temp(low_temp)

# helpers

# getters
    def get_low_temp(self):
        return self.__low_temp

# setters
    def set_low_temp(self, low_temp):
        self.__low_temp = low_temp

# string
    def __str__(self):
        return "Freezer:" + super().__str__()[10:] + "\tLow Temp: " + str(self.get_low_temp()) + "\n"