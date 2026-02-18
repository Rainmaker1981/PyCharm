class Car:
    __MAX: 100
    __acceleration: None
    __deceleration: None
    __owner: None
    __current_speed: None
    __distance_traveled: None
    __trip_time: None
    __max_speed: None
    __speeds: []

    def __init__( owner, cur_speed, dist, trip_time, max_speed):
        Pass

    # helper
    def move(self):
        pass
    def acceleration(self):
        pass
    def brake(self):
        pass
    def get_avg_speed(self):
        pass

    # getters
    def get_owner(self):
        return self.__owner
    def get_current_speed(self):
        return self.__current_speed
    def get_distance_traveled(self):
        return self.__distance_traveled
    def get_trip_time(self):
        return self.__trip_time
    def get_max_speed(self):
        return self.__max_speed

    # setters
    def set_owner(self, owner):
        self.__owner = owner
    def set_current_speed(self, speed):
        self.__current_speed = speed
    def set_distance_traveled(self, distance):
        self.__distance_traveled = distance
    def set_trip_time(self, trip_time):
        self.__trip_time = trip_time
    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    # string
    def __str__(self):
        return "Car Description: \n\t Owner: \t\t" + str(self.get_owner()) + \
            "Current Speed: \t" + str(self.get_current_speed()) + " Mph" + \
            "Distance: \t" + str(self.get_distance_traveled()) +" Miles" + \
            "Time: \t\t" + str(self.get_trip_time()) + " Minutes" + \
            "Max Speed: \t" + str(self.get_max_speed()) + " Mph" + \
            "Avg Speed: \t" + str(self.get_avg_speed()) + " Mph"
