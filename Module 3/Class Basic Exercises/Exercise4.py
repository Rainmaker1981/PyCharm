class Employee:
    # data attributes
    __employee_id = None
    __first_name = None
    __last_name = None
    __email = None

    # init
    def __init__(self, employee_id, first_name, last_name, email):
        self.set_employee_id(employee_id)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)

    # helpers

    # getters
    def get_employee_id(self):
        return self.__employee_id
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_email(self):
        return self.__email

    # setters
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id
    def set_first_name(self, first_name):
        self.__first_name = first_name
    def set_last_name(self, last_name):
        self.__last_name = last_name
    def set_email(self, email):
        self.__email = email

    # string

    def __str__(self):
        return ("Employee: ID:    " + str(self.get_employee_id()) + \
            "\n\t\t  Name:  " + str(self.get_first_name()) + " " + str(self.get_last_name()) + \
            "\n\t\t  Email: " + str(self.get_email())  + "\n")

