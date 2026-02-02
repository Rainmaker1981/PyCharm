class Animal:
    # data attributes
    __type = None
    __legs = None
    __size = None
    __name = None

    # init
    def __init__(self, type, legs, size, name):
        self.set_type(type)
        self.set_legs(legs)
        self.set_size(size)
        self.set_name(name)

    # helpers

    # getters
    def get_type(self):
        return self.__type
    def get_legs(self):
        return self.__legs
    def get_size(self):
        return self.__size
    def get_name(self):
        return self.__name

    # setters
    def set_type(self, type):
        self.__type = type
    def set_legs(self, legs):
        self.__legs = legs
    def set_size(self, size):
        self.__size = size
    def set_name(self, name):
        self.__name = name

    # string
    def __str__(self):
        return str(self.get_name()) + " has " + str(self.get_legs()) + " legs and is " + \
            str(self.get_size()) + " sized " + str(self.get_type()) + ".\n"