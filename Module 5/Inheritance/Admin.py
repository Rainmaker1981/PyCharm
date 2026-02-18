from User import User

class Admin(User):
    __security_level= None

    def __init__(self, first_name, last_name, security_level):
        super().__init__(first_name, last_name)
        self.set_security_level(security_level)

# helpers

# getters
    def get_security_level(self):
        return self.__security_level

# setters
    def set_security_level(self, security_level):
        self.__security_level = security_level

# string
    def __str__(self):
        return "Admin:" + super().__str__()[5:] + "\tSecurity: " + str(self.get_security_level()) + "\n"
