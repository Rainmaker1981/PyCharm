
class Name:
    # data attributes
    __attribute = None

    # init
    def __init__(self, attribute):
        self.set_attribute(attribute)

    # helpers
    def get_help(self):
        return self.get_attribute()

    # getters
    def get_attribute(self):
        return self.__attribute

    # setters
    def set_attribute(self, attribute):
        self.__attribute = attribute

    # string
    def __str__(self):
        return "This was the attribute entered: " + str(self.get_attribute()) + "\n"