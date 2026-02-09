class Airplane:
    # attributes
    __brand = None
    __model = None
    __engine_number = None
    __passenger_number = None
    __top_speed = None

    def __init__(self,brand, model, engine_number, passenger_number, top_speed):
        self.set_brand(brand)
        self.set_model(model)
        self.set_engine_number(engine_number)
        self.set_passenger_number(passenger_number)
        self.set_top_speed(top_speed)

    # getters
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_engine_number(self):
        return self.__engine_number

    def get_passenger_number(self):
        return self.__passenger_number

    def get_top_speed(self):
        return self.__top_speed

    # setters
    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_engine_number(self, engine_number):
        self.__engine_number = engine_number

    def set_passenger_number(self, passenger_number):
        self.__passenger_number = passenger_number

    def set_top_speed(self, top_speed):
        self.__top_speed = top_speed

    # helpers
    def compare_to(self, incoming):
        compare = -2
        if incoming.get_top_speed() > self.get_top_speed():
            compare = 1
        elif incoming.get_top_speed() == self.get_top_speed():
            compare = 0
        elif incoming.get_top_speed() < self.get_top_speed():
            compare = -1
        return compare

    def equal_to(self, incoming):
        is_equal = False
        if self.get_brand() == incoming.get_brand() \
            and self.get_model() == incoming.get_model() \
            and self.get_engine_number() == incoming.get_engine_number() \
            and self.get_passenger_number() == incoming.get_passenger_number() \
            and self.get_top_speed() == incoming.get_top_speed():
            is_equal = True
        return is_equal

    def time_to_arrive(self, distance):
        # hours = miles / (miles per hour)
        time = distance / self.get_top_speed()
        return time

    def __str__(self):
        return (
            "Airplane: \nBrand= " + str(self.get_brand()) + "\n" \
            "Model= " + str(self.get_model()) + "\n" \
            "Engine Number= " + str(self.get_engine_number()) + "\n" \
            "Number of Passengers= " +str(self.get_passenger_number()) + "\n" \
            "Top Speed= " + str(self.get_top_speed()) +" mph"
        )
