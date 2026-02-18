class Appliance:
    __type = None
    __brand = None

    def __init__(self, type, brand):
        self.set_type(type)
        self.set_brand(brand)

# helpers

# getters
    def get_type(self):
        return self.__type

    def get_brand(self):
        return self.__brand

# setters
    def set_type(self, type):
        self.__type = type

    def set_brand(self, brand):
        self.__brand = brand

# string
    def __str__(self):
        return "Appliance:\n\tType: " + str(self.get_type()) + "\n\tBrand: " + str(self.get_brand()) + "\n"