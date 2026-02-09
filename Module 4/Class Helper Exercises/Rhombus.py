class Rhombus:
    __side_length: None
    __daig_1: None
    __diag_2: None

    def __init__(self, side_length, daig_1, diag_2):
        self.set_side_length(side_length)
        self.set_daig_1(daig_1)
        self.set_diag_2(diag_2)

    # helpers
    def compare_to(self, incoming):
        a1 = self.get_area()
        a2 = incoming.get_area()
        if a1 > a2:
            return -1
        elif a1 < a2:
            return 1
        elif a1 == a2:
            return 0

    def equal_to(self, incoming):
        equal = False
        if self.get_side_length() == incoming.get_side_length()\
            and self.get_daig_1() == incoming.get_daig_1()\
            and self.get_diag_2() == incoming.get_diag_2():
            equal = True
        return equal

    def get_perimeter(self):
        return self.get_side_length() * 4

    def get_area(self):
        return (self.get_daig_1() * self.get_diag_2()) / 2

    # getters
    def get_side_length(self):
        return self.__side_length

    def get_daig_1(self):
        return self.__daig_1

    def get_diag_2(self):
        return self.__diag_2

    # setters
    def set_side_length(self, side_length):
        self.__side_length = side_length

    def set_daig_1(self, daig_1):
        self.__daig_1 = daig_1

    def set_diag_2(self, diag_2):
        self.__diag_2 = diag_2


    def __str__(self):
        return (
            "Rhombus:  side_length= " + str(self.get_side_length()) \
            + "daig_1= " + str(self.get_daig_1()) \
            + "diag_2= " + str(self.get_diag_2())
        )
