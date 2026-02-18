class Room:
    __width = None
    __length = None

    def __init__(self, width, length):
        self.set_width(width)
        self.set_length(length)

# helpers

# getters
    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

# setters
    def set_width(self, width):
        self.__width = width

    def set_length(self, length):
        self.__length = length

# string
    def __str__(self):
        return "Room:\n\tWidth: " + str(self.get_width()) + "\n\tLength: " + str(self.get_length()) + "\n"