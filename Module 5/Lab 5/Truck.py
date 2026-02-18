from Automobile import Automobile

class Truck(Automobile):
    __drive_type = -1

    def __init__(self, make, model, year, weight, acceleration, drive_type):
        super().__init__(make, model, year, weight, acceleration)
        self.__drive_type = None
        self.set_drive_type(drive_type)

    # getters
    def get_drive_type(self):
        return self.__drive_type

    # setters
    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type

    def __str__(self):
        return super().__str__() + "\tDrive Type: " + str(self.__drive_type) + "WD"