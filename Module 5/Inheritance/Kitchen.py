from Room import Room

class Kitchen(Room):
    __appliance_brand = None

    def __init__(self, width, length, appliance_brand):
        super().__init__(width, length)
        self.set_appliance_brand(appliance_brand)

# helpers

# getters
    def get_appliance_brand(self):
        return self.__appliance_brand

# setters
    def set_appliance_brand(self, appliance_brand):
        self.__appliance_brand = appliance_brand

# string
    def __str__(self):
        return "Kitchen:" + super().__str__()[5:] + "\tBrand: " + str(self.get_appliance_brand()) + "\n"