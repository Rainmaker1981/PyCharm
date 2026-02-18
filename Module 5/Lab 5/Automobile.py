class Automobile:
    __make= None
    __model= None
    __year= None
    __weight= None
    __acceleration= None

    def __init__(self,make,model,year,weight,acceleration):
        self.set_make(make)
        self.set_model(model)
        self.set_year(year)
        self.set_weight(weight)
        self.set_acceleration(acceleration)

    # helpers

    # setters
    def set_make(self,make):
        self.__make = make
    def set_model(self,model):
        self.__model = model
    def set_year(self,year):
        self.__year = year
    def set_weight(self,weight):
        self.__weight = weight
    def set_acceleration(self,acceleration):
        self.__acceleration = acceleration

    # getters
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
    def get_weight(self):
        return self.__weight
    def get_acceleration(self):
        return self.__acceleration

    def __str__(self):
        return ("Auto: \n \t"
                "Make: " + str(self.__make) + "\n \t"
                "Model: " + str(self.__model) + "\n \t"
                "Year: " + str(self.__year) + "\n \t"
                "Weight: " + str(self.__weight) + " kg\n \t"
                "Acceleration: " + str(self.__acceleration) + "m/s\n")
