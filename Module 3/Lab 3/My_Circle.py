import math

from setuptools.dist import invalid_unless_false


class My_Circle:
    # attributes
    __radius = None
    __name = None
    x = 5

    def __init__(self, name, radius):
        self.set_radius(radius)
        self.set_name(name)

    # helpers
    def get_area(self):
        area = math.pi * self.get_radius() **2
        return area

    def get_diameter(self):
        diameter = self.get_radius() * 2
        return diameter

    def get_circumference(self):
        circumference = math.pi * self.get_diameter()
        return circumference

    def compare_to(self, incoming):
        compare = -2
        if incoming.get_radius() > self.get_radius():
            compare = 1
        elif incoming.get_radius() == self.get_radius():
            compare = 0
        elif incoming.get_radius() < self.get_radius():
            compare = -1
        return compare

    def equal_to(self, incoming):
        is_equal = False
        if incoming.get_radius() == self.get_radius() and incoming.get_name() == self.get_name():
            is_equal = True
        return is_equal

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
        return ("Circle Name: " + str(self.get_name()) + "\n\tRadius: " + str(self.get_radius())) \
            + "\n\tArea: " + str(round(self.get_area(), 2)) \
            + "\n\tDiameter: " + str(self.get_diameter()) \
            + "\n\tCircumference: " + str(round(self.get_circumference(), 2))
