from Appliance import Appliance

class Dishwasher(Appliance):
    __capacity = None

    def __init__(self, type, brand, capacity):
        super().__init__(type, brand)
        self.set_capacity(capacity)

# helpers

# getters
    def get_capacity(self):
        return self.__capacity

# setters
    def set_capacity(self, capacity):
        self.__capacity = capacity

# string
    def __str__(self):
        return "Dishwasher:" + super().__str__()[10:] + "\tCapacity: " + str(self.get_capacity()) + "\n"