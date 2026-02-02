class My_Circle:
    # attributes
    __radius = None
    __name = None
    x = 5

    def __init__(self, name, radius):
        self.set_radius(radius)
        self.set_name(name)

    # setters
    def set_radius(self, radius):
        self.__radius = radius

    def set_name(self, name):
        self.__name = name

    # getters
    def get_radius(self):
        return self.__radius

    def get_name(self):
        return self.__name

    # string function
    def __str__(self):
        return "My_Circle: name=" + str(self.get_name()) + ", radius=" + str(self.get_radius())