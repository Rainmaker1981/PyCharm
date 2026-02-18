from Automobile import Automobile

class Car(Automobile):
    __doors = -1

    def __init__(self, make, model, year, weight, acceleration, doors):
        super().__init__(make, model, year, weight, acceleration)
        self.__doors = None
        self.set_doors(doors)

    # getters
    def get_doors(self):
        return self.__doors

    # setters
    def set_doors(self, doors):
        self.__doors = doors

    def __str__(self):
        return super().__str__() + "\tDoors: " + str(self.__doors)
