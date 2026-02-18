from Appliance import Appliance

class Refrigerator(Appliance):
    __volume = None

    def __init__(self, type, brand, volume):
        super().__init__(type, brand)
        self.set_volume(volume)

# helpers

# getters
    def get_volume(self):
        return self.__volume

# setters
    def set_volume(self, volume):
        self.__volume = volume

# string
    def __str__(self):
        return "Refrigerator:" + super().__str__()[10:] + "\tVolume: " + str(self.get_volume()) + "\n"