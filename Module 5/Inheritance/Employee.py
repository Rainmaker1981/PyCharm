from User import User

class Employee(User):
    __position_title = None

    def __init__(self, first_name, last_name, position_title):
        super().__init__(first_name, last_name)
        self.set_position_title(position_title)

# helpers

# getters
    def get_position_title(self):
        return self.__position_title

# setters
    def set_position_title(self, position_title):
        self.__position_title = position_title

# string
    def __str__(self):
        return "Employee:" + super().__str__()[5:] + "\tID #: " + str(self.get_position_title()) + "\n"
