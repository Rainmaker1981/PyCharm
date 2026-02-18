class User:
    __first_name = None
    __last_name = None

    def __init__(self, first_name, last_name):
        self.set_first_name(first_name)
        self.set_last_name(last_name)

    # helpers

    # getters
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name

    # setters
    def set_first_name(self, first_name):
        self.__first_name = first_name
    def set_last_name(self, last_name):
        self.__last_name = last_name

    # string
    def __str__(self):
        return "User:\n\tFirst: " + str(self.get_first_name()) + "\n\tLast: " + str(self.get_last_name()) + "\n"
