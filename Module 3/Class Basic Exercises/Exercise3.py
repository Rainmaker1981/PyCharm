class Student:
    # data attributes
    __first_name = None
    __last_name = None
    __middle_name = None
    __birthday = None

    # init
    def __init__(self, first_name, middle_name, last_name, birthday):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_middle_name(middle_name)
        self.set_birthday(birthday)

    # helpers

    # getters
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_middle_name(self):
        return self.__middle_name
    def get_birthday(self):
        return self.__birthday

    #setters
    def set_first_name(self, first_name):
        self.__first_name = first_name
    def set_last_name(self, last_name):
        self.__last_name = last_name
    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name
    def set_birthday(self, birthday):
        self.__birthday = birthday

    # string
    def __str__(self):
        return "Student: " + str(self.get_first_name()) + " " + \
            str(self.get_middle_name()) + " " +  \
            str(self.get_last_name()) + \
            "\n\t\t Birthday: " + str(self.get_birthday())  + "\n"
