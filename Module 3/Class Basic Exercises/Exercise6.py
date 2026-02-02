class House:
    # data attributes
    __num_rooms = None
    __num_bathrooms = None
    __total_square_foot = None
    __current_price = None

    # init
    def __init__(self, num_rooms, num_bathrooms, total_square_foot, current_price):
        self.set_num_rooms(num_rooms)
        self.set_num_bathrooms(num_bathrooms)
        self.set_total_square_foot(total_square_foot)
        self.set_current_price(current_price)

    # helpers

    # getters
    def get_num_rooms(self):
        return self.__num_rooms
    def get_num_bathrooms(self):
        return self.__num_bathrooms
    def get_total_square_foot(self):
        return self.__total_square_foot
    def get_current_price(self):
        return self.__current_price

    # setters
    def set_num_rooms(self, num_rooms):
        self.__num_rooms = num_rooms
    def set_num_bathrooms(self, num_bathrooms):
        self.__num_bathrooms = num_bathrooms
    def set_total_square_foot(self, total_square_foot):
        self.__total_square_foot = total_square_foot
    def set_current_price(self, current_price):
        self.__current_price = current_price

    # string
    def __str__(self):
        return "This house has " + str(self.get_num_rooms()) + " rooms and " + str(self.get_num_bathrooms()) + \
            " bathrooms with a total square feet of " + str(self.get_total_square_foot()) + " sq ft. It is currently listed at $" + \
            str(self.get_current_price()) + ".\n"