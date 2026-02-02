
class Rectangle:
    # data attributes
    __length = None
    __height = None

    # init
    def __init__(self, length, height):
        self.set_length(length)
        self.set_height(height)

    # helpers
    def get_area(self):
        return self.get_length() * self.get_height()

    def get_peri(self):
        return self.get_length() * 2 + self.get_height() * 2

    # getters
    def get_length(self):
        return self.__length

    def get_height(self):
        return self.__height

    # setters
    def set_length(self, length):
        self.__length = length

    def set_height(self, height):
        self.__height = height

    # string
    def __str__(self):
        return "Rectangle:\n\tHeight: " + str(self.get_height()) + "\n\tLength: " + str(self.get_length()) + \
        "\n\tArea: " + str(self.get_area()) + "\n\tPerimeter: " + str(self.get_peri()) + "\n"


