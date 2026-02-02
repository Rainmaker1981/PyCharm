class Triangle:
    # data attributes
    __length = None
    __height = None

    # init
    def __init__(self, length, height):
        self.set_length(length)
        self.set_height(height)

    # helpers

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
        return "Triangle:\n\tHeight: " + str(self.get_height()) + "\n\tLength: " + str(self.get_length()) + "\n"


