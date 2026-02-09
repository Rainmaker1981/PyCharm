import math

class Circle:
    __radius = None

    def __init__(self, radius):
        self.set_radius(radius)

    # helpers
    def get_area(self):
        area = math.pi * self.get_radius() **2
        circumference = math.pi * (self.get_radius() + self.get_radius())
        return circumference, area

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

    # getters
    def get_radius(self):
        return self.__radius

    def __str__(self):
        return ("Circle: radius= " + str(self.get_radius()))
