class Car:
    __MAX: 100
    __acceleration: 5
    __deceleration: 5
    __owner: ""
    __current_speed: -1
    __distance_traveled: -1
    __trip_time: -1
    __max_speed: -1
    __speeds: []

    def __init__(self, owner, cur_speed=0, dist=0, trip_time=0.0, max_speed=0.0):
        self.__owner = owner
        self.__acceleration = 5
        self.__deceleration = 5
        self.__current_speed = cur_speed
        self.__distance_traveled = dist
        self.__trip_time = trip_time
        self.__max_speed = max_speed
        self.__speeds = []

    # helper
    def move(self):
        if self.__current_speed > 0:
            self.__distance_traveled += 1
            self.__trip_time += 60 / self.__current_speed

    def acceleration(self, target_speed):
        if target_speed > self.__max_speed:
            target_speed = self.__max_speed

        while self.__current_speed < target_speed:
            self.__current_speed += 5
            self.__speeds.append(self.__current_speed)

    def brake(self):
        new_speed = self.__current_speed - self.__deceleration
        if new_speed < 0:
            new_speed = 0
        self.set_current_speed(new_speed)

    def get_avg_speed(self):
        if len(self.__speeds) == 0:
            return 0
        return sum(self.__speeds) / len(self.__speeds)

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
        return "Car Description:\n" + \
            "\tOwner:\t\t\t" + str(self.get_owner()) + "\n" + \
            "\tCurrent Speed:\t" + str(self.get_current_speed()) + " Mph\n" + \
            "\tDistance:\t\t" + str(self.get_distance_traveled()) + " Miles\n" + \
            "\tTime:\t\t\t" + str(self.get_trip_time()) + " Minutes\n" + \
            "\tMax Speed:\t\t" + str(self.get_max_speed()) + " Mph\n" + \
            "\tAvg Speed:\t\t" + str(self.get_avg_speed()) + " Mph"
